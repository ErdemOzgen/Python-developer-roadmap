from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_returns_ok_payload() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["service"] == "starter-backend"
