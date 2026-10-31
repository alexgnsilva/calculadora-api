from fastapi.testclient import TestClient

from app import __version__
from app.main import app

client = TestClient(app) 
  
  
def test_health(): 
    resposta = client.get("/health") 
    assert resposta.status_code == 200 
    assert resposta.json() == {"status": "ok", "version": __version__} 
    