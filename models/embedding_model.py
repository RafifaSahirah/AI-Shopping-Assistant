import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import pandas as pd
import pickle

# Load product data
df = pd.read_csv("cleaned_amazon_products.csv")

# Normalize price and ratings to a scale (0-1)
max_price = df["actual_price"].max()
normalized_price = df["actual_price"] / max_price

max_rating = df["ratings"].max()  
normalized_rating = df["ratings"] / max_rating  # Scale ratings between 0-1

# Load pre-trained sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings for product names
product_embeddings = model.encode(df["name"].tolist(), convert_to_tensor=True)

# Convert embeddings to NumPy
product_embeddings = product_embeddings.cpu().numpy()

# Append price and rating as extra features
price_embeddings = normalized_price.values.reshape(-1, 1)  
rating_embeddings = normalized_rating.values.reshape(-1, 1)  

# Combine text embeddings with price & rating
combined_embeddings = np.hstack((product_embeddings, price_embeddings, rating_embeddings))

# Create FAISS index
index = faiss.IndexFlatL2(combined_embeddings.shape[1])
index.add(combined_embeddings)

# Save index and data
with open("embeddings_faiss.pkl", "wb") as f:
    pickle.dump((df, combined_embeddings), f)

print("✅ FAISS Index with price & rating saved!")
