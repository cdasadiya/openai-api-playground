"""
File: reasoning_models.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates reasoning-oriented prompts using OpenAI Responses API.

Run:
python 07_reasoning_models/reasoning_models.py
"""

import sys
import traceback
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.openai_client import client

PROMPT = """
A company has:
- 3 backend engineers
- 2 frontend engineers
- 1 DevOps engineer

They can complete:
- 6 backend tasks/day
- 4 frontend tasks/day
- 2 deployment tasks/day

Estimate how many days are needed to complete:
- 42 backend tasks
- 20 frontend tasks
- 8 deployment tasks

Provide detailed reasoning.
"""

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=PROMPT
    )

    print("\n=== REASONING MODEL RESPONSE ===\n")
    print(response.output_text)

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nReasoning request failed: {error}")
