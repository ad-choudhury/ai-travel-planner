from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_trip_validation():
    payload = {
        "origin": "Kolkata",
        "destination": "Thailand",
        "start_date": "2026-12-19",
        "end_date": "2026-12-12",
        "travelers": 2,
        "budget": 120000,
        "currency": "INR",
        "interests": ["beach"],
    }
    response = client.post("/api/v1/trips/plan", json=payload)
    assert response.status_code == 422
