"""
File: api_keys.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates secure API key loading and secret management practices.

Concepts Covered:
- .env based local development
- GitHub Codespaces secrets
- Centralized OpenAI client usage
- Safe key masking
- Secret rotation guidance
- Full traceback debugging support

Run:
python 01_core_platform/api_keys.py

OR from inside the folder:
python api_keys.py
"""

import sys
import traceback
from pathlib import Path

from openai import OpenAIError


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.config import OPENAI_API_KEY  # noqa: E402
from utils.openai_client import client  # noqa: E402


try:
    print("\n=== API KEY LOADING ===\n")
    print("Recommended local .env format:")
    print("OPENAI_API_KEY=sk-...")
    print("\nProduction practice: store secrets in Codespaces, CI/CD, or a vault.")
    print("Never commit .env files or paste full API keys into logs.")
    print(f"Loaded key length: {len(OPENAI_API_KEY)} characters")
    print(f"Safe preview: {OPENAI_API_KEY[:7]}...{OPENAI_API_KEY[-4:]}")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="List two best practices for API key security."
    )

    print("\n=== API KEY SECURITY RESPONSE ===\n")
    print(response.output_text)

except OpenAIError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nOpenAI API key example failed: {error}")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUnexpected API key example failure: {error}")
