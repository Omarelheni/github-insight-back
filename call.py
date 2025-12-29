import os
import requests
from typing import Optional
from starlette.concurrency import run_in_threadpool
from dotenv import load_dotenv
import re
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "meta-llama/llama-3.1-8b-instruct"

SYSTEM_PROMPT = """
You are a senior software architect helping a developer understand
an unfamiliar codebase.

Focus on:
- intent
- architecture
- responsibilities
- design trade-offs

Avoid:
- repeating obvious syntax
- guessing missing information
"""

SYSTEM_PROMPT = "answer simply"

def _call_llm_sync(prompt: str) -> str:

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 700,
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=60)

    response.raise_for_status()

    content = response.json()["choices"][0]["message"]["content"]

    return content

async def call_llm(
    prompt: str
) -> str:
    return await run_in_threadpool(
        _call_llm_sync,
        prompt
    )
