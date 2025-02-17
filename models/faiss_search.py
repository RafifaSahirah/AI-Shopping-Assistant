import faiss
import pickle
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from models.config import INDEX_PATH, METADATA_PATH, MODEL_NAME
from models.chatbot import chatbot_response

# ✅ Fix: Disable parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Load product data and embeddings
df, embeddings = pickle.load(open(METADATA_PATH, "rb"))  # Load as Pandas DataFrame
max_price = df["actual_price"].max()  # Max price for normalization
max_rating = df["ratings"].max()  # Max rating for normalization

# Load FAISS index
try:
    faiss_index = faiss.read_index(INDEX_PATH)
except:
    faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
    faiss_index.add(embeddings)
    faiss.write_index(faiss_index, INDEX_PATH)

# Load sentence transformer model
embedding_model = SentenceTransformer(MODEL_NAME)

def generate_summary(results):
    """Generate a structured summary ensuring name, price, and ratings are included."""
    product_info = "\n".join([
        f"- {item['name']} (Price: ${item['actual_price']}, Rating: {item['ratings']}⭐)"
        for item in results
    ])
    
    prompt = (
        "Summarize these product recommendations in a friendly tone. "
        "Ensure each product includes its name, price (in ₹), and ratings. "
        "Do not omit any information:\n"
        f"{product_info}"
    )

    return chatbot_response(prompt)

def search_faiss(query, price=0, rating=0, top_k=5):
    """Search FAISS index using query, price, and rating normalization."""
    query_embedding = embedding_model.encode([query], convert_to_numpy=True).astype(np.float32)

    # Normalize price & rating (avoid division by zero)
    normalized_price = np.array([[price / max_price]], dtype=np.float32) if max_price > 0 else np.array([[0]], dtype=np.float32)
    normalized_rating = np.array([[rating / max_rating]], dtype=np.float32) if max_rating > 0 else np.array([[0]], dtype=np.float32)

    # Reshape to (1,1)
    normalized_price = normalized_price.reshape(1, -1)
    normalized_rating = normalized_rating.reshape(1, -1)

    # Append price & rating to query embedding
    query_embedding = np.hstack((query_embedding, normalized_price, normalized_rating))  # Shape (1, embedding_dim + 2)

    print("Query embedding shape:", query_embedding.shape)  # Debugging

    # FAISS search
    distances, indices = faiss_index.search(query_embedding, top_k)

    results = [
        {
            "name": df.iloc[idx]["name"],
            "actual_price": df.iloc[idx]["actual_price"],
            "ratings": df.iloc[idx]["ratings"],
            "score": float(distances[0][i]),
        }
        for i, idx in enumerate(indices[0]) if idx < len(df)
    ]
    
    return results
