from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os
from pathlib import Path

from app.settings import UPLOAD_DIR
from app.agent import build_knowledge_base, answer_question

app = FastAPI(title="Document RAG API")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

@app.on_event("startup")
def startup_event():
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = Path(__file__).parent / "index.html"
    return html_path.read_text(encoding="utf-8")

@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.pdf', '.txt')):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos .pdf o .txt")
    
    file_path = UPLOAD_DIR / file.filename
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        build_knowledge_base()
        
        return {"status": "success", "message": f"Archivo '{file.filename}' procesado correctamente."}
    except Exception as e:
        if file_path.exists(): file_path.unlink()
        return {"status": "error", "message": str(e)}

@app.post("/api/ask")
def ask_document(query: QuestionRequest):
    try:
        respuesta = answer_question(query.question)
        return {"status": "success", "answer": respuesta}
    except Exception as e:
        return {"status": "error", "message": str(e)}
