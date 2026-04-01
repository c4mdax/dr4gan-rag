from pathlib import Path

VECTORDB_PATH = Path("./chroma_db")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_CONFIG = {
    "model": "phi3:mini",
    "temperature": 0.3,
    "num_ctx": 4096
}

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50 
SCORE_THRESHOLD = 0.5
TOP_K = 3 
