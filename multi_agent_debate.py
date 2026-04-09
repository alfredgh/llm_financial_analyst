# agents/debate_agents.py
from agents.llm import call_llm

def bull_case(context):
    return call_llm(f"Make a strong bull case:\n{context}")

def bear_case(context):
    return call_llm(f"Make a strong bear case:\n{context}")

def judge(bull, bear):
    return call_llm(f"""
    Bull case:
    {bull}

    Bear case:
    {bear}

    Decide final rating and justify.
    """)
