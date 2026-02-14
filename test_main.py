from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_checksum():
    response = client.post(
        "/generate-checksum",
        json={"text": "hello"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "checksum" in data
