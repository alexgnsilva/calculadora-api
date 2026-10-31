from fastapi.testclient import TestClient

from app import __version__
from app.main import app

client = TestClient(app) 
  
  
def test_health(): 
    resposta = client.get("/health") 
    assert resposta.status_code == 200 
    assert resposta.json() == {"status": "ok", "version": __version__} 

def test_soma(): 
    resposta = client.get("/soma", params={"a": 2, "b": 3}) 
    assert resposta.status_code == 200 
    assert resposta.json()["resultado"] == 5 
  
  
def test_soma_parametro_invalido(): 
    resposta = client.get("/soma", params={"a": "dois", "b": 3}) 
    assert resposta.status_code == 422    