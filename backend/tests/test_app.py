from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_health_check():
    response = client.get('/')
    assert response.json() == {'status': 'ok'}
