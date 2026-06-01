from kirov_ai import llm, telemetry, prompts

def test_llm_generate():
    res = llm.generate_safe_response("test", mode="general")
    assert "response_id" in res
    assert "response" in res
    assert "tokens_used" in res

def test_llm_generate_threat():
    res = llm.generate_safe_response("log entry", mode="threat_analysis")
    assert "THREAT LEVEL" in res["response"]

def test_telemetry_log():
    entry = telemetry.log_event("INFO", "test-service", "test message")
    assert entry["level"] == "INFO"
    assert entry["service"] == "test-service"

def test_telemetry_get_logs():
    telemetry.clear_logs()
    telemetry.log_event("WARN", "svc", "warning msg")
    logs = telemetry.get_logs(10)
    assert len(logs) >= 1
    assert logs[-1]["level"] == "WARN"

def test_telemetry_clear():
    telemetry.clear_logs()
    assert telemetry.get_logs() == []

def test_prompts_get():
    result = prompts.get_prompt("cybersecurity", "threat_triage", event="data breach")
    assert "data breach" in result

def test_prompts_not_found():
    result = prompts.get_prompt("unknown", "missing")
    assert "not found" in result
