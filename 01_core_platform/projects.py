"""
File: projects.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates project-based OpenAI API usage for production isolation.

Concepts Covered:
- Optional OPENAI_PROJECT_ID usage
- Project isolation concepts
- Per-application access boundaries
- Centralized OpenAI client usage
- Secure configuration practices
- Full traceback debugging support

Run:
python 01_core_platform/projects.py

OR from inside the folder:
python projects.py
"""

import sys
import traceback
from pathlib import Path

from openai import OpenAIError


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.config import OPENAI_PROJECT_ID  # noqa: E402
from utils.openai_client import client  # noqa: E402


try:
    print("\n=== PROJECT-BASED API USAGE ===\n")

    if OPENAI_PROJECT_ID:
        print(f"OPENAI_PROJECT_ID configured: {OPENAI_PROJECT_ID}")
    else:
        print("OPENAI_PROJECT_ID not set. The SDK will use the API key default project.")

    print("\nProject isolation concept:")
    print("Use separate projects for development, staging, production, or each product.")
    print("This helps isolate keys, usage, permissions, budgets, and operational risk.")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Give three reasons to isolate OpenAI workloads by project."
    )

    print("\n=== PROJECT ISOLATION RESPONSE ===\n")
    print(response.output_text)

except OpenAIError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nProject-scoped request failed: {error}")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUnexpected project example failure: {error}")
