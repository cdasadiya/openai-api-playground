"""
File: rate_limits.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates retry logic and graceful handling for OpenAI rate limits.

Concepts Covered:
- RateLimitError handling
- Exponential backoff
- Retry limits
- Centralized OpenAI client usage
- Production resilience practices
- Full traceback debugging support

Run:
python 01_core_platform/rate_limits.py

OR from inside the folder:
python rate_limits.py
"""

import sys
import time
import traceback
from pathlib import Path

from openai import OpenAIError, RateLimitError


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client  # noqa: E402


MAX_RETRIES = 3
BASE_DELAY_SECONDS = 2


try:
    print("\n=== RATE LIMIT SAFE REQUEST ===\n")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input="Explain how retry backoff protects production services."
            )

            print("\n=== RATE LIMIT EXAMPLE RESPONSE ===\n")
            print(response.output_text)
            break

        except RateLimitError as error:
            if attempt == MAX_RETRIES:
                raise

            delay = BASE_DELAY_SECONDS * (2 ** (attempt - 1))
            print(f"Rate limit hit on attempt {attempt}: {error}")
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)

except RateLimitError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nRate limit retry budget exhausted: {error}")

except OpenAIError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nOpenAI API request failed: {error}")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUnexpected rate limit example failure: {error}")
