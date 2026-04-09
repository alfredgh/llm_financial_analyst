# agents/analyst_agent.py
from agents.llm import call_llm

def analyze_narrative(mda_text):
    prompt = f"""
    Decompose the MD&A:
    1. Key drivers
    2. Risks
    3. Hidden concerns
    4. Inconsistencies

    Text:
    {mda_text}
    """
    return call_llm(prompt)
