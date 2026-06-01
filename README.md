# Kirov-AI-SDK

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white&style=for-the-badge)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![CI](https://github.com/Raphasha27/Kirov-AI-SDK/actions/workflows/ci.yml/badge.svg)](https://github.com/Raphasha27/Kirov-AI-SDK/actions)

Shared internal SDK for LLM orchestration, telemetry, and prompt management across the Kirov Dynamics ecosystem.

## Features

- **LLM Orchestration** — Unified `generate_safe_response()` with domain-specific mock responses for isolated testing
- **Telemetry** — Lightweight in-memory event logging with levels, metadata, and retrieval
- **Prompt Vault** — Domain-organized prompt templates (`cybersecurity`, `finance`, `data_science`, `rag`) with `{kwargs}` interpolation
- **REST API** — FastAPI server exposing `/api/v1/generate`, `/api/v1/prompt`, `/api/v1/logs`, `/api/v1/vault`
- **Dockerized** — Production container with uvicorn

## Quick Start

```bash
cp .env.example .env
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

Or with Docker:

```bash
docker build -t kirov-ai-sdk .
docker run -p 8000:8000 kirov-ai-sdk
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Platform info |
| GET | `/health` | Health check |
| POST | `/api/v1/generate` | Generate LLM response (mode: general, threat_analysis, market_signal, rag_query, code_review) |
| POST | `/api/v1/prompt` | Get a prompt template by domain and template name |
| GET | `/api/v1/logs` | Retrieve telemetry logs |
| GET | `/api/v1/vault` | List available prompt domains |

## Prompt Vault Domains

| Domain | Templates |
|--------|-----------|
| cybersecurity | threat_triage, anomaly_summary |
| finance | anomaly_detection, portfolio_advice |
| data_science | eda_summary, model_interpretation |
| rag | query_expansion, context_synthesis |

## Project Structure

```
Kirov-AI-SDK/
├── kirov_ai/
│   ├── __init__.py
│   ├── llm.py          # LLM generation orchestration
│   ├── telemetry.py    # Event logging
│   └── prompts.py      # Prompt vault
├── tests/
│   ├── test_api.py     # API endpoint tests
│   └── test_sdk.py     # SDK unit tests
├── app.py              # FastAPI application
├── Dockerfile
├── .pre-commit-config.yaml
├── pyproject.toml
└── requirements.txt
```

## Using the SDK (Python)

```python
from kirov_ai import llm, telemetry, prompts

# Generate a response
response = llm.generate_safe_response("Analyze this log", mode="threat_analysis")

# Log telemetry
telemetry.log_event("INFO", "my-service", "Operation completed")

# Get a prompt template
prompt = prompts.get_prompt("finance", "portfolio_advice", risk="high")
```

## Testing

```bash
pytest
```

## Pre-commit

```bash
pip install pre-commit
pre-commit install
```

## License

MIT License. See [LICENSE](LICENSE) for details.

---

© 2026 **Kirov Dynamics Technology** | Built by **Koketso Raphasha (Raphasha27)**
