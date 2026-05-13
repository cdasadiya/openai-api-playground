"""
File: models.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Lists available OpenAI models and prints model metadata cleanly.

Concepts Covered:
- Models API usage
- Model metadata inspection
- Centralized OpenAI client usage
- Operational model inventory
- Clean terminal formatting
- Full traceback debugging support

Run:
python 01_core_platform/models.py

OR from inside the folder:
python models.py
"""

import sys
import traceback
from pathlib import Path

from openai import OpenAIError


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client  # noqa: E402


try:
    models = client.models.list()

    print("\n=== AVAILABLE MODELS ===\n")

    for index, model in enumerate(models.data, start=1):
        created = getattr(model, "created", "unknown")
        owned_by = getattr(model, "owned_by", "unknown")

        print(f"{index}. {model.id}")
        print(f"   Created: {created}")
        print(f"   Owned By: {owned_by}")

    print("\nUse this inventory to choose models intentionally per workload.")

except OpenAIError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nModel listing failed: {error}")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUnexpected models example failure: {error}")
