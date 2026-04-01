from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.settings import *

def get_vectorstore(docs: list, rebuild: bool = False):
    if rebuild and VECTORDB_PATH.exists():
        import shutil
        shutil.rmtree(VECTORDB_PATH)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = text_splitter.split_documents(docs)    
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(VECTORDB_PATH)
    )

def get_retriever():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectordb = Chroma(
        persist_directory=str(VECTORDB_PATH),
        embedding_function=embeddings
    )
    return vectordb.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": TOP_K,
            "score_threshold": SCORE_THRESHOLD
        }
    )
