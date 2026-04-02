# dRAGan

### Proyecto actualizado para implementación Backend
Actualización limpia del proyecto _dragan-agent-rag_.
___

## Cambios
- Agente expuesto a una API para consumo facilitado 
- Consumo de API por parte de LLM: Groq, para evitar descargas locales de LLM
___
## Enlaces
Repositorio con el proyecto base: https://github.com/c4mdax/dragan-agent-rag (ejecución local)
URL: 
___
## Ejecución
Clonar el proyecto 
```bash
git clone https://github.com/c4mdax/dr4gan-rag
cd dr4gan-rag/
```
Activar entorno virtual e instalar requerimientos
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Ejecutar servidor 
```bash
uvicorn app.main:app --reload
```
