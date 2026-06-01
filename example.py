"""
Example usage of the Kirov-AI-SDK.

Run: python example.py
"""

from kirov_ai import llm, telemetry, prompts


def main():
    telemetry.log_event("INFO", "example", "Starting Kirov-AI-SDK example")

    response = llm.generate_safe_response("Analyze this log entry", mode="threat_analysis")
    print("\nLLM Response (threat_analysis):")
    print(f"  Response: {response['response']}")
    print(f"  Confidence: {response['tokens_used']} tokens, {response['latency_ms']}ms")

    response = llm.generate_safe_response("What is 2+2?", mode="general")
    print("\nLLM Response (general):")
    print(f"  Response: {response['response']}")

    prompt = prompts.get_prompt("cybersecurity", "threat_triage", event="Phishing email detected")
    print(f"\nPrompt from vault:\n  {prompt}")

    prompt = prompts.get_prompt("finance", "portfolio_advice", risk="high")
    print(f"\nPortfolio advice prompt:\n  {prompt}")

    prompt = prompts.get_prompt("unknown", "missing")
    print(f"\nMissing template:\n  {prompt}")

    telemetry.log_event("WARN", "example", "Telemery test warning")
    logs = telemetry.get_logs(5)
    print(f"\nRecent telemetry logs ({len(logs)} entries):")
    for log in logs:
        print(f"  [{log['level']}] [{log['service']}] {log['message']}")

    print("\nAvailable prompt domains:", list(prompts.PROMPT_VAULT.keys()))
    print("Kirov-AI-SDK example completed successfully.")


if __name__ == "__main__":
    main()
