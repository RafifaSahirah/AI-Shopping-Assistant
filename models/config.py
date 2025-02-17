import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenRouter API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"

# FAISS index paths
INDEX_PATH = "data/faiss_index.bin"
METADATA_PATH = "data/embeddings_faiss.pkl"

# Model for embeddings
MODEL_NAME = "all-MiniLM-L6-v2"
