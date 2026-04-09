def cross_validate(financials, narrative):
    prompt = f"""
    Financials:
    {financials}

    Narrative:
    {narrative}

    Identify contradictions and earnings quality issues.
    """
    return call_llm(prompt)
