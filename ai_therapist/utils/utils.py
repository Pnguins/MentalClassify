import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging
import re
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, PointStruct, VectorParams, Distance
from sentence_transformers import SentenceTransformer
import torch
from tqdm import tqdm


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
if not GOOGLE_API_KEY:
    logger.error("GOOGLE_API_KEY not found in environment variables")
    raise RuntimeError("GOOGLE_API_KEY not found in environment variables")

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model once at module level
MODEL_NAME = 'gemini-1.5-flash'
model = None
try:
    model = genai.GenerativeModel(MODEL_NAME)
    logger.info("Gemini Model initialized successfully")
except Exception as e:
    logger.error(f"Error initializing Gemini model: {e}")
    logger.error(f"Please make sure the API Key is correct and the Gemini API is reachable")


# Device configuration
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Using device: {device}")

# Load Sentence Transformer model
try:
   embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device=device)
   logger.info("Sentence Transformer model loaded successfully")
except Exception as e:
   logger.error(f"Error loading Sentence Transformer model: {e}")
   embedding_model = None
   
# Initialize Qdrant Client
QDRANT_URL = os.getenv("QDRANT_URL", "https://35612626-619b-40d3-90db-e71a27a12e38.eu-west-1-0.aws.cloud.qdrant.io:6333")
try:
    qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    logger.info("Qdrant client initialized successfully")
except Exception as e:
       logger.error(f"Error initializing Qdrant client: {e}")
       qdrant_client = None
   
def get_gemini_embeddings(text: str):
    try:
        if model is None:
           logger.error("Gemini Model is not initialized")
           return None
        
        gemini_embedding = model.embed_content(
            content = text,
            model = "models/embedding-001"
        ).embedding.values
        return gemini_embedding
    except Exception as e:
        logger.error(f"Error generating embedding: {e}")
        return None

def generate_gemini_response(prompt: str, generation_config:dict = None) -> str:
    try:
        if model is None:
            logger.error("Gemini Model is not initialized")
            return None
        if generation_config is None:
           generation_config = {
               "temperature": 1,
               "top_p": 0.8,
               "top_k": 40,
               "max_output_tokens": 800
           }

        response = model.generate_content(
            contents=[
                {
                    "role": "user",
                    "parts": prompt
                }
            ],
            generation_config=generation_config
        )
        logger.info("Gemini response generated successfully!")
        return response.text if response.text else ""

    except Exception as e:
      logger.error(f"Error generating response: {e}")
      return ""
   
def clean_gemini_response(response_text: str) -> str:
     """Cleans the Gemini response by removing backticks and other unwanted characters."""
     cleaned_response = response_text.replace("```json", "").replace("```", "").strip()
     return cleaned_response
   
def generate_sentence_transformer_embeddings(texts, batch_size=32):
    """
    Generate embeddings for a list of texts in batches using sentence transformers.
        
    Args:
        texts (List[str]): List of texts to embed
        batch_size (int): Size of batches for processing
        
    Returns:
        List[numpy.ndarray]: List of embeddings
    """
    try:
        if embedding_model is None:
            logger.error("Sentence Transformer Model is not initialized")
            return None

        embeddings = []
        
        with tqdm(total=len(texts), desc="Generating embeddings") as pbar:
            for i in range(0, len(texts), batch_size):
                batch_texts = texts[i:i+batch_size]
                # Generate embeddings for the batch
                batch_embeddings = embedding_model.encode(batch_texts)
                embeddings.extend(batch_embeddings)
                pbar.update(len(batch_texts))
            
        return embeddings
    except Exception as e:
        logger.error(f"Error generating sentence transformer embedding: {e}")
        return None
    
def upload_to_qdrant(collection_name, texts, embeddings, payload_extras=None):
    """
    Upload documents and their embeddings to Qdrant.
        
    Args:
        collection_name (str): Name of the collection
        texts (List[str]): List of documents
        embeddings (List[numpy.ndarray]): List of embeddings
        payload_extras (List[dict], optional): Additional payload information
    """
    try:
        if qdrant_client is None:
            logger.error("Qdrant client is not initialized")
            return False
        # Create collection if it doesn't exist
        vector_size = len(embeddings[0])
        try:
            qdrant_client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE
                )
            )
        except Exception as e:
            logger.info(f"Collection might already exist: {e}")

        # Prepare points for upload
        points = []
        for idx, (text, embedding) in enumerate(zip(texts, embeddings)):
            payload = {"content": text}
            if payload_extras and idx < len(payload_extras):
                payload.update(payload_extras[idx])
                    
            points.append(PointStruct(
                id=idx,
                vector=embedding.tolist(),
                payload=payload
            ))

        # Upload in batches
        batch_size = 100
        for i in range(0, len(points), batch_size):
            batch = points[i:i+batch_size]
            qdrant_client.upsert(
                collection_name=collection_name,
                points=batch
            )
        logger.info("Successfully uploaded to Qdrant")
        return True
    except Exception as e:
        logger.error(f"Error uploading to qdrant: {e}")
        return False

def retrieve_context(collection_name, query_text, top_k=5):
    """
    Retrieves relevant documents from Qdrant for a given query using sentence transformer embeddings.
        
    Args:
        collection_name (str): Name of the collection
        query_text (str): Query text
        top_k (int): Number of documents to retrieve
        
    Returns:
        str: Concatenated context from relevant documents
    """
    try:
        if qdrant_client is None or embedding_model is None:
            logger.error("Qdrant client or embedding model is not initialized")
            return ""
        # Generate query embedding
        query_embedding = embedding_model.encode([query_text])[0]
            
        # Search for similar documents
        search_result = qdrant_client.search(
            collection_name=collection_name,
            query_vector=query_embedding.tolist(),
            limit=top_k
        )

        # Extract and join relevant texts
        context = " ".join([item.payload.get("content", "") for item in search_result])
        return context
    except Exception as e:
        logger.error(f"Error retrieving context: {e}")
        return ""