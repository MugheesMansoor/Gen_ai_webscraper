from openai import OpenAI
import json
import os

# Set your OpenRouter API key directly here
os.environ["OPENROUTER_API_KEY"] = "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"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def extract_jobs(html):
    prompt = f"""
    Extract all job listings from this HTML.
    Return a strict JSON array only, no explanations, no extra text.
    Each job should have:
    - name
    - client
    - looking_for (list)
    - posted_on
    - categories (list)

    HTML:
    {html}
    """

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content.strip()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        print("ERROR: GenAI returned invalid JSON")
        print("Raw output:", raw)
        data = []

    return data