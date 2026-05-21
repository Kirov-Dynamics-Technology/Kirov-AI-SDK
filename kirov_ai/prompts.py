PROMPT_VAULT = {
    "cybersecurity": {
        "threat_triage": "You are a Tier-3 SOC Analyst. Classify the following event by MITRE ATT&CK framework: {event}",
        "anomaly_summary": "Summarize these anomalous network behaviors and suggest countermeasures: {data}"
    },
    "finance": {
        "anomaly_detection": "Analyze this volume spike and determine if it signals a market event: {data}",
        "portfolio_advice": "Given this portfolio composition and risk tolerance of {risk}, suggest rebalancing actions."
    },
    "data_science": {
        "eda_summary": "Summarize the key findings of this exploratory data analysis: {stats}",
        "model_interpretation": "Interpret these model metrics and suggest improvements: {metrics}"
    },
    "rag": {
        "query_expansion": "Expand this user query into semantic search terms: {query}",
        "context_synthesis": "Synthesize these {n} retrieved document chunks into a coherent answer."
    }
}

def get_prompt(domain: str, template: str, **kwargs) -> str:
    try:
        raw = PROMPT_VAULT[domain][template]
        return raw.format(**kwargs)
    except KeyError:
        return f"Template '{domain}/{template}' not found in Prompt Vault."
