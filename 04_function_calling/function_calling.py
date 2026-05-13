"""
File: function_calling.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates OpenAI function calling patterns.

Run:
python 04_function_calling/function_calling.py
"""

import json
import sys
import traceback
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.openai_client import client

TOOLS = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get weather information for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string"
                }
            },
            "required": ["city"],
            "additionalProperties": False
        }
    }
]

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="What is the weather in Ahmedabad?",
        tools=TOOLS
    )

    print("\n=== FUNCTION CALLING RESPONSE ===\n")

    for output in response.output:
        if output.type == "function_call":
            print(f"Function Name: {output.name}")
            print("Arguments:")
            print(json.dumps(json.loads(output.arguments), indent=4))

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nFunction calling request failed: {error}")
