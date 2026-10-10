import pytest
from fastapi.testclient import TestClient
from main import app, AnalysisRequest

client = TestClient(app)

def test_startup():
    assert app is not None

def test_happy_path():
    payload = {
        "raw_text": "Name: John Doe. Age: 30.",
        "form_fields": {"applicant_name": "John Doe"}
    }
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "RISK"
    assert "applicant_name" in data["matched_fields"]

def test_no_match():
    payload = {
        "raw_text": "Name: Jane Doe. Age: 25.",
        "form_fields": {"applicant_name": "John Doe"}
    }
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "CLEAR"

def test_invalid_payload():
    response = client.post("/analyze", json={"raw_text": "test"})
    assert response.status_code == 422
