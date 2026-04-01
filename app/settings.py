import os
from pathlib import Path

VECTORDB_PATH = Path("./chroma_db")
UPLOAD_DIR = Path("./uploads")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_CONFIG = {
    "model_name": "llama3-8b-8192", 
    "temperature": 0.3
}

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50 
SCORE_THRESHOLD = 0.5
TOP_K = 3
