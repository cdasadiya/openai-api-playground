"""
File: tool_calling.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates tool calling workflows using OpenAI Responses API.

Run:
python 05_tool_calling/tool_calling.py
"""

import sys
import traceback
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.openai_client import client

TOOLS = [
    {
        "type": "web_search_preview"
    }
]

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Find the latest trends in AI agents.",
        tools=TOOLS
    )

    print("\n=== TOOL CALLING RESPONSE ===\n")
    print(response.output_text)

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nTool calling request failed: {error}")
