"""
File: system_prompting.py

Purpose:
Demonstrates how to use system instructions with the OpenAI Responses API.

Concepts Covered:
- System prompts
- Instruction hierarchy
- Controlled response behavior
- Shared OpenAI client usage

Run:
python 01_responses_api/system_prompting.py
"""

from utils.openai_client import client


SYSTEM_PROMPT = """
You are a senior software architect.
Provide concise and production-focused answers.
"""


try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=SYSTEM_PROMPT,
        input="How should microservices communicate in production systems?"
    )

    print("\n=== SYSTEM PROMPT RESPONSE ===\n")
    print(response.output_text)

except Exception as error:
    print(f"Request failed: {error}")
