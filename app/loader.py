import os
from tqdm import tqdm
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from os.path import expanduser

def list_valid_files(folder: str) -> list[str]:
    expanded_path = expanduser(folder)
    if not os.path.isdir(expanded_path):
        raise ValueError(f"Ruta no válida: {expanded_path}")
    
    valid_files = []
    for file in os.listdir(expanded_path):
        if file.lower().endswith(('.pdf', '.txt')):
            valid_files.append(os.path.join(expanded_path, file))
    
    if not valid_files:
        raise ValueError("No se encontraron archivos PDF/TXT válidos")
    return valid_files

def load_documents(files: list[str]) -> list:
    docs = []
    for file in tqdm(files, desc="Cargando documentos"):
        try:
            if file.lower().endswith('.pdf'):
                docs.extend(PyPDFLoader(file).load())
            else:
                docs.extend(TextLoader(file, encoding='utf-8').load())
        except Exception as e:
            print(f"\nError al cargar {file}: {str(e)}")
            continue
    return docs
