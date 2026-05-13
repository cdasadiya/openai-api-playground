"""
File: organizations.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates organization-aware OpenAI client configuration.

Concepts Covered:
- Optional OPENAI_ORG_ID usage
- Multi-organization account concepts
- Centralized client configuration
- Secure environment variable handling
- Production tenancy awareness
- Full traceback debugging support

Run:
python 01_core_platform/organizations.py

OR from inside the folder:
python organizations.py
"""

import sys
import traceback
from pathlib import Path

from openai import OpenAIError


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.config import OPENAI_ORG_ID  # noqa: E402
from utils.openai_client import client  # noqa: E402


try:
    print("\n=== ORGANIZATION-AWARE CLIENT SETUP ===\n")

    if OPENAI_ORG_ID:
        print(f"OPENAI_ORG_ID configured: {OPENAI_ORG_ID}")
    else:
        print("OPENAI_ORG_ID not set. The SDK will use the API key default organization.")

    print("\nMulti-org concept:")
    print("Use organization scoping when one developer account has access to multiple orgs.")
    print("Keep organization IDs in environment variables, not source code.")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Explain why organization scoping matters for production AI systems."
    )

    print("\n=== ORGANIZATION EXAMPLE RESPONSE ===\n")
    print(response.output_text)

except OpenAIError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nOrganization-scoped request failed: {error}")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUnexpected organization example failure: {error}")
