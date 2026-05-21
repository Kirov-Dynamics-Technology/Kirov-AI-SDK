from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from kirov_ai import llm, telemetry, prompts

app = FastAPI(
    title="Kirov-AI-SDK API",
    description="Shared internal SDK for LLM orchestration, telemetry and prompt management.",
    version="1.0.0"
)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class GenerateRequest(BaseModel):
    prompt: str
    mode: Optional[str] = "general"

class PromptRequest(BaseModel):
    domain: str
    template: str
    kwargs: Optional[dict] = {}

@app.get("/")
def root():
    return {"platform": "Kirov-AI-SDK", "version": "1.0.0", "modules": ["llm", "telemetry", "prompts"]}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/v1/generate")
def generate(req: GenerateRequest):
    telemetry.log_event("INFO", "kirov-llm", f"Generating response for mode: {req.mode}")
    return llm.generate_safe_response(req.prompt, req.mode)

@app.post("/api/v1/prompt")
def get_prompt(req: PromptRequest):
    return {"prompt": prompts.get_prompt(req.domain, req.template, **req.kwargs)}

@app.get("/api/v1/logs")
def get_logs(limit: int = 20):
    return {"logs": telemetry.get_logs(limit)}

@app.get("/api/v1/vault")
def vault_index():
    return {"domains": list(prompts.PROMPT_VAULT.keys())}
