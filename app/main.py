import argparse
from app.agent import answer_question

def main():
    parser = argparse.ArgumentParser(description="Agente RAG para documentos")
    parser.add_argument("--docs_path", required=True, help="Ruta a documentos PDF/TXT")
    parser.add_argument("--question", required=True, help="Pregunta a responder")
    parser.add_argument("--rebuild", action="store_true", help="Reconstruir base vectorial")
    
    args = parser.parse_args()
    
    answer = answer_question(
        question=args.question,
        docs_path=args.docs_path,
        rebuild=args.rebuild
    )
    
    print("\n🔍 Respuesta:")
    print(answer)

if __name__ == "__main__":
    main()
