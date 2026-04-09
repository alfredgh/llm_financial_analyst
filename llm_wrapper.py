# agents/llm.py
from openai import OpenAI

client = OpenAI()

def call_llm(prompt, model="gpt-4.1"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
