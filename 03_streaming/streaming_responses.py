"""
File: streaming_responses.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates streaming responses using the OpenAI Responses API.

Run:
python 03_streaming/streaming_responses.py
"""

import sys
import traceback
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.openai_client import client

PROMPT = "Explain event-driven architecture in simple terms."

try:
    print("\n=== STREAMING RESPONSE ===\n")

    stream = client.responses.create(
        model="gpt-4.1-mini",
        input=PROMPT,
        stream=True
    )

    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)

    print("\n")

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nStreaming request failed: {error}")
