"""
File: system_prompting.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates how to use system instructions with the OpenAI Responses API.

Concepts Covered:
- System prompts
- Instruction hierarchy
- Controlled response behavior
- Shared OpenAI client usage
- Portable import handling for Codespaces
- Production-style debugging

Run:
python 01_responses_api/system_prompting.py

OR from inside the folder:
python system_prompting.py
"""

import sys
import traceback
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client


SYSTEM_PROMPT = """
You are a senior software architect.
Provide concise, production-focused, and technically accurate answers.
Focus on scalability, observability, reliability, and maintainability.
"""


USER_PROMPT = "How should microservices communicate in production systems?"


try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=SYSTEM_PROMPT,
        input=USER_PROMPT
    )

    print("\n=== SYSTEM PROMPT RESPONSE ===\n")
    print(response.output_text)

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nRequest failed: {error}")
