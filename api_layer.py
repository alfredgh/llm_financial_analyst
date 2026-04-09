# app.py
from fastapi import FastAPI
from pipelines.full_analysis import run_full_analysis

app = FastAPI()

@app.post("/analyze")
def analyze(report_text: str):
    result = run_full_analysis(report_text)
    return result
