import random
import uuid
from datetime import datetime
from typing import Optional

PROMPT_TEMPLATES = {
    "threat_analysis": "Analyze this security event and classify the threat level: {input}",
    "market_signal": "Based on these market indicators, generate a trading signal: {input}",
    "rag_query": "Based on the following retrieved context, answer the question: {input}",
    "code_review": "Review this code for security vulnerabilities and performance issues: {input}"
}

def generate_safe_response(prompt: str, mode: str = "general", context: Optional[str] = None) -> dict:
    """
    Mocked LLM generation for isolated testing across the Kirov Dynamics ecosystem.
    Returns a structured response with metadata.
    """
    response_id = str(uuid.uuid4())[:8]
    
    mock_responses = {
        "threat_analysis": f"THREAT LEVEL: HIGH. Classified as {random.choice(['SQL Injection', 'DDoS', 'APT Activity'])}. Recommend immediate containment.",
        "market_signal": f"SIGNAL: {random.choice(['BUY', 'SELL', 'HOLD'])}. Confidence: {round(random.uniform(0.7, 0.95), 2)}. RSI deviation detected.",
        "rag_query": f"Based on retrieved context (similarity: {round(random.uniform(0.82, 0.98), 2)}): The answer is derived from chunk {random.randint(1, 200)}.",
        "general": f"Processing complete. Confidence: {round(random.uniform(0.75, 0.99), 2)}."
    }

    return {
        "response_id": response_id,
        "mode": mode,
        "prompt": prompt[:100],
        "response": mock_responses.get(mode, mock_responses["general"]),
        "tokens_used": random.randint(150, 800),
        "latency_ms": random.randint(120, 900),
        "timestamp": datetime.utcnow().isoformat()
    }
