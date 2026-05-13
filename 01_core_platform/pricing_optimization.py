"""
File: pricing_optimization.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates practical cost optimization patterns for production OpenAI systems.

Concepts Covered:
- Model selection
- Token reduction
- Batching concepts
- Caching strategy
- Cost-aware architecture
- Full traceback debugging support

Run:
python 01_core_platform/pricing_optimization.py

OR from inside the folder:
python pricing_optimization.py
"""

import sys
import traceback
from pathlib import Path

from openai import OpenAIError


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client  # noqa: E402


OPTIMIZATION_PRACTICES = [
    "Select the smallest model that meets quality, latency, and safety needs.",
    "Reduce prompt size by removing duplicate context and unused instructions.",
    "Batch compatible offline work to improve throughput and operational control.",
    "Cache deterministic or repeated answers behind stable cache keys.",
    "Track cost per feature, tenant, model, environment, and release version."
]


try:
    print("\n=== PRICING OPTIMIZATION PRACTICES ===\n")

    for index, practice in enumerate(OPTIMIZATION_PRACTICES, start=1):
        print(f"{index}. {practice}")

    prompt = """
    Create a concise cost optimization plan for an OpenAI-powered support chatbot.
    Include model selection, token reduction, batching, caching, and monitoring.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    print("\n=== COST OPTIMIZATION RESPONSE ===\n")
    print(response.output_text)

    usage = response.usage
    print("\n=== COST SIGNALS ===\n")
    print(f"Input Tokens: {getattr(usage, 'input_tokens', 0)}")
    print(f"Output Tokens: {getattr(usage, 'output_tokens', 0)}")
    print(f"Total Tokens: {getattr(usage, 'total_tokens', 0)}")

except OpenAIError as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nPricing optimization request failed: {error}")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nUnexpected pricing optimization example failure: {error}")
