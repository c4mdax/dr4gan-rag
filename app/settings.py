import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

VECTORDB_PATH = Path("./chroma_db")
UPLOAD_DIR = Path("./uploads")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("¡Falta la GROQ_API_KEY! Asegúrate de ponerla en tu archivo .env")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_CONFIG = {
    "model_name": "llama-3.1-8b-instant",
    "temperature": 0.3
}

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50 
SCORE_THRESHOLD = 0.5
TOP_K = 3
