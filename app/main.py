from fastapi import FastAPI 
  
from app import __version__ 
  
app = FastAPI(title="Calculadora API", version=__version__) 
  
  
@app.get("/health") 
def health() -> dict: 
    """Verifica se a API está ativa e devolve a versão.""" 
    return {"status": "ok", "version": __version__}