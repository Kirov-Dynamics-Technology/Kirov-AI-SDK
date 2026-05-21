import json
from datetime import datetime
from typing import Any

_log_buffer = []

def log_event(level: str, service: str, message: str, metadata: Any = None):
    entry = {
        "level": level,
        "service": service,
        "message": message,
        "metadata": metadata,
        "timestamp": datetime.utcnow().isoformat()
    }
    _log_buffer.append(entry)
    print(f"[{level}] [{service}] {message}")
    return entry

def get_logs(limit: int = 50):
    return _log_buffer[-limit:]

def clear_logs():
    _log_buffer.clear()
    return {"status": "cleared"}
