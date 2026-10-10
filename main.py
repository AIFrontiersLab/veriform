from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

class AnalysisRequest(BaseModel):
    raw_text: str
    form_fields: Dict[str, str]

class AnalysisResponse(BaseModel):
    status: str
    matched_fields: list

def check_match(raw: str, value: str) -> bool:
    if not value:
        return False
    return value.lower() in raw.lower()

@app.post("/analyze", response_model=AnalysisResponse)
def analyze(req: AnalysisRequest):
    matched = []
    for key, value in req.form_fields.items():
        if check_match(req.raw_text, value):
            matched.append(key)
    
    if matched:
        return AnalysisResponse(status="RISK", matched_fields=matched)
    return AnalysisResponse(status="CLEAR", matched_fields=[])

def demo():
    from fastapi.testclient import TestClient
    client = TestClient(app)
    payload = {
        "raw_text": "Name: John Doe. Age: 30.",
        "form_fields": {"applicant_name": "John Doe"}
    }
    resp = client.post("/analyze", json=payload)
    print(f"Status: {resp.json()}")
