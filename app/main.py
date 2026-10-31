from fastapi import FastAPI

from app import __version__
from app.operations import somar

app = FastAPI(title="Calculadora API", version=__version__) 
  
  
@app.get("/health") 
def health() -> dict: 
    """Verifica se a API está ativa e devolve a versão.""" 
    return {"status": "ok", "version": __version__}

 
@app.get("/soma") 
def soma(a: float, b: float) -> dict: 
    """Soma dois números. Exemplo: /soma?a=2&b=3""" 
    return {"operacao": "soma", "a": a, "b": b, "resultado": somar(a, b)} 