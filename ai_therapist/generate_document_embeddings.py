import pandas as pd
import numpy as np
import pickle
from utils.utils import get_gemini_embeddings
import os

# Load the CSV
data_path = "data/dreadit_rag.csv"
output_path = "database/embeddings/dreadit_embeddings.pkl"

# Ensure output folder exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

print("Loading dataset...")
df = pd.read_csv(data_path)

# Check for text column
if 'text' not in df.columns:
    raise ValueError("CSV file must contain a 'text' column")

# Generate embeddings for each row
embeddings = []
print("Generating embeddings...")
for idx, row in df.iterrows():
    text = row['text']
    embedding = get_gemini_embeddings(text)
    if embedding:
        embeddings.append((text, embedding))
    else:
        print(f"Warning: Failed to generate embedding for row {idx}")

# Save embeddings
print("Saving embeddings...")
with open(output_path, "wb") as f:
    pickle.dump(embeddings, f)

print(f"Embeddings saved to {output_path}")
