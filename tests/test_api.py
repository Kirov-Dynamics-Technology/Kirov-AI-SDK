from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.status_code == 200
    data = res.json()
    assert data["platform"] == "Kirov-AI-SDK"
    assert "llm" in data["modules"]

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "healthy"}

def test_generate():
    res = client.post("/api/v1/generate", json={"prompt": "test prompt", "mode": "general"})
    assert res.status_code == 200
    data = res.json()
    assert "response" in data
    assert "response_id" in data
    assert data["mode"] == "general"

def test_generate_threat_analysis():
    res = client.post("/api/v1/generate", json={"prompt": "Analyze this log", "mode": "threat_analysis"})
    assert res.status_code == 200
    data = res.json()
    assert "THREAT LEVEL" in data["response"]

def test_prompt():
    res = client.post("/api/v1/prompt", json={"domain": "cybersecurity", "template": "threat_triage", "kwargs": {"event": "test"}})
    assert res.status_code == 200
    data = res.json()
    assert "prompt" in data
    assert "MITRE ATT&CK" in data["prompt"]

def test_prompt_not_found():
    res = client.post("/api/v1/prompt", json={"domain": "unknown", "template": "missing", "kwargs": {}})
    assert res.status_code == 200
    assert "not found" in res.json()["prompt"]

def test_logs():
    res = client.get("/api/v1/logs?limit=5")
    assert res.status_code == 200
    data = res.json()
    assert "logs" in data

def test_vault():
    res = client.get("/api/v1/vault")
    assert res.status_code == 200
    assert "cybersecurity" in res.json()["domains"]
