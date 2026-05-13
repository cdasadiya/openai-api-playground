"""
File: tokens.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates token counting concepts and lightweight token estimation.

Concepts Covered:
- Approximate token counting
- Prompt sizing
- Response token budgeting
- Centralized OpenAI client usage
- Cost and latency awareness
- Full traceback debugging support

Run:
python 01_core_platform/tokens.py

OR from inside the folder:
python tokens.py
"""

import sys
import traceback
from pathlib import Path

from openai import OpenAIError


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client  # noqa: E402


PROMPT = """
Explain token budgeting for production OpenAI API applications in three bullets.
"""


def estimate_tokens(text: str) -> int:
    """
    Estimate token count without adding extra dependencies.

    This simple rule of thumb is useful for quick planning. Production systems
    can add a tokenizer library when exact model-specific counts are required.
    """
    return max(1, len(text) // 4)


try:
    estimated_prompt_tokens = estimate_tokens(PROMPT)

    print("\n=== TOKEN ESTIMATION ===\n")
    print(f"Estimated Prompt Tokens: {estimated_prompt_tokens}")
    print("Note: exact token counts are available after an API response in response.usage.")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=PROMPT
    )

    usage = response.usage

    print("\n=== TOKEN CONCEPT RESPONSE ===\n")
    print(response.output_text)

    print("\n=== ACTUAL API TOKEN USAGE ===\n")
    print(f"Input Tokens: {getattr(usage, 'input_tokens', 0)}")
    print(f"Output Tokens: {getattr(usage, 'output_tokens', 0)}")
    print(f"Total Tokens: {getattr(usage, 'total_tokens', 0)}")

except OpenAIError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nToken example request failed: {error}")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUnexpected token example failure: {error}")
