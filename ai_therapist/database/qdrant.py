from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
from typing import List, Tuple
import numpy as np

def load_embedding_model():
    """
    Load the embedding model using SentenceTransformer.
    """
    return AutoTokenizer.from_pretrained("BAAI/bge-m3")

def setup_qdrant_client(api_key: str, url: str):
    """
    Set up the Qdrant client.
    """
    return QdrantClient(url=url, api_key=api_key)

def generate_embeddings(texts: List[str], model, batch_size: int = 32) -> List[List[float]]:
    """
    Generate embeddings for a list of texts in batches.
    """
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        batch_embeddings = model.encode(batch_texts)
        embeddings.extend(batch_embeddings)
    return embeddings

def upload_to_qdrant(
    client: QdrantClient,
    collection_name: str,
    texts: List[str],
    embeddings: List[List[float]]
):
    """
    Upload texts and their embeddings to Qdrant.
    """
    vector_size = len(embeddings[0])
    try:
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )
    except Exception as e:
        print(f"Collection might already exist: {e}")

    points = [
        PointStruct(id=idx, vector=embedding, payload={"text": text})
        for idx, (text, embedding) in enumerate(zip(texts, embeddings))
    ]

    client.upsert(collection_name=collection_name, points=points)
def pad_embedding(embedding, target_size):
    """
    Pads an embedding to the target size with zeros.

    Args:
        embedding (list of float): The original embedding.
        target_size (int): The desired dimensionality.

    Returns:
        list of float: Padded embedding.
    """
    return np.pad(embedding, (0, max(0, target_size - len(embedding))), mode='constant').tolist()
    
def retrieve_context(
    qdrant_client: QdrantClient,
    collection_name: str,
    query_text: str,
    embedding_model,
    top_k: int = 5
) -> Tuple[str, List[dict]]:
    """
    Retrieve relevant documents from Qdrant and remove duplicates by text content.
    """
    query_embedding = embedding_model(query_text, return_tensors="pt", truncation=True, padding=True)["input_ids"].numpy().flatten().tolist()
    padded_embedding = pad_embedding(query_embedding, 1024)

    search_result = qdrant_client.search(
        collection_name=collection_name,
        query_vector=padded_embedding,
        limit=top_k
    )

    unique_docs = {}
    relevant_docs = []

    for item in search_result:
        post = item.payload.get("post", "")
        label = item.payload.get("Label", "")
        score = item.score
        DS = item.payload.get("DS", "")

        if post not in unique_docs:
            unique_docs[post] = label
            relevant_docs.append({"text": post, "score": score, "DS": DS})

    context = [(post, label) for post, label in unique_docs.items()]

    return context, relevant_docs

