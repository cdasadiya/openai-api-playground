"""
File: usage_tracking.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates how to extract token usage from OpenAI Responses API results.

Concepts Covered:
- Prompt/input token usage
- Completion/output token usage
- Total token usage
- Centralized OpenAI client usage
- Cost observability foundations
- Full traceback debugging support

Run:
python 01_core_platform/usage_tracking.py

OR from inside the folder:
python usage_tracking.py
"""

import sys
import traceback
from pathlib import Path

from openai import OpenAIError


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client  # noqa: E402


try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Summarize why token usage should be tracked in production AI systems."
    )

    usage = response.usage
    prompt_tokens = getattr(usage, "input_tokens", 0)
    completion_tokens = getattr(usage, "output_tokens", 0)
    total_tokens = getattr(usage, "total_tokens", 0)

    print("\n=== USAGE TRACKING RESPONSE ===\n")
    print(response.output_text)

    print("\n=== TOKEN USAGE ===\n")
    print(f"Prompt/Input Tokens: {prompt_tokens}")
    print(f"Completion/Output Tokens: {completion_tokens}")
    print(f"Total Tokens: {total_tokens}")

except OpenAIError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUsage tracking request failed: {error}")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUnexpected usage tracking example failure: {error}")
