from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.settings import LLM_CONFIG, UPLOAD_DIR
from app.vectorstore import get_vectorstore, get_retriever
from app.loader import list_valid_files, load_documents

PROMPT_TEMPLATE = """
Eres un asistente especializado en análisis de documentos. Responde en español usando ÚNICAMENTE la información proporcionada en el contexto, haciendo paráfrasis de la información evitando redundancias, cacofonias y enunciados sin sentido, dando una respuesta concisa y precisa.

Si el contexto no contiene información relevante a la pregunta, reporta agradablemente (si quieres puedes usar emojis) que no hay información suficiente en los documentos proporcionados, invitando al usuario a proporcionar más documentos relacionados.

Contexto:
{context}

Pregunta: 
{question}

Respuesta (en español):
"""

def setup_llm_chain():
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    llm = OllamaLLM(**LLM_CONFIG)
    
    return prompt | llm | StrOutputParser()

def build_knowledge_base():
    files = list_valid_files(str(UPLOAD_DIR))
    docs = load_documents(files)
    get_vectorstore(docs, rebuild=True)

def answer_question(question: str) -> str:
    retriever = get_retriever()
    
    relevant_docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content for d in relevant_docs]) if relevant_docs else None
    
    if not context:
        return "No encontré información relevante en los documentos proporcionados. ¡Sube más documentos por favor!"
    
    llm_chain = setup_llm_chain()
    return llm_chain.invoke({"context": context, "question": question})
