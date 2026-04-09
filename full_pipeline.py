# pipelines/full_analysis.py
from tools.parser import extract_financials
from agents.analyst_agent import analyze_narrative, cross_validate, generate_signals
from agents.debate_agents import bull_case, bear_case, judge

def run_full_analysis(document):
    financials = extract_financials(document)
    narrative = analyze_narrative(document)

    validation = cross_validate(financials, narrative)

    context = f"""
    Financials: {financials}
    Narrative: {narrative}
    Validation: {validation}
    """

    signals = generate_signals(context)

    bull = bull_case(context)
    bear = bear_case(context)
    final = judge(bull, bear)

    return {
        "financials": financials,
        "narrative": narrative,
        "validation": validation,
        "signals": signals,
        "bull_case": bull,
        "bear_case": bear,
        "final_decision": final
    }
