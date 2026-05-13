"""
File: authentication.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates secure OpenAI authentication for production Python applications.

Concepts Covered:
- OPENAI_API_KEY validation
- Centralized OpenAI client usage
- Secure environment variable handling
- GitHub Codespaces compatibility
- Authentication error handling
- Full traceback debugging support

Run:
python 01_core_platform/authentication.py

OR from inside the folder:
python authentication.py
"""

import sys
import traceback
from pathlib import Path

from openai import AuthenticationError, OpenAIError


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.config import OPENAI_API_KEY  # noqa: E402
from utils.openai_client import client  # noqa: E402


try:
    # Never print the full API key. A masked preview is safe for debugging.
    masked_key = f"{OPENAI_API_KEY[:7]}...{OPENAI_API_KEY[-4:]}"

    print("\n=== AUTHENTICATION CHECK ===\n")
    print(f"OPENAI_API_KEY loaded securely: {masked_key}")
    print("Sending a small authenticated request to validate access...")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Reply with one sentence confirming authentication is configured."
    )

    print("\n=== AUTHENTICATED RESPONSE ===\n")
    print(response.output_text)

except AuthenticationError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nAuthentication failed. Check OPENAI_API_KEY permissions: {error}")

except OpenAIError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nOpenAI API request failed during authentication validation: {error}")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUnexpected authentication example failure: {error}")
