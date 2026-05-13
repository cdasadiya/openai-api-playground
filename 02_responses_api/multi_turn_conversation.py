"""
File: multi_turn_conversation.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates multi-turn conversations using previous response IDs.

Run:
python 02_responses_api/multi_turn_conversation.py
"""

import sys
import traceback
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.openai_client import client

try:
    first_response = client.responses.create(
        model="gpt-4.1-mini",
        input="What is Retrieval-Augmented Generation?"
    )

    print("\n=== FIRST RESPONSE ===\n")
    print(first_response.output_text)

    second_response = client.responses.create(
        model="gpt-4.1-mini",
        previous_response_id=first_response.id,
        input="Can you explain it with a real-world example?"
    )

    print("\n=== FOLLOW-UP RESPONSE ===\n")
    print(second_response.output_text)

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nConversation request failed: {error}")
