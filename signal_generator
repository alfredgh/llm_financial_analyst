def generate_signals(context):
    prompt = f"""
    Based on analysis:

    {context}

    Generate:
    - 3 bullish signals
    - 3 bearish signals
    - rating (1-5)
    - confidence

    Return JSON.
    """
    return call_llm(prompt)
