"""
File: structured_json_output.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates structured JSON generation using OpenAI Responses API.

Concepts Covered:
- Structured outputs
- JSON generation
- Reliable machine-readable responses
- Shared OpenAI client usage
- Portable import handling for Codespaces

Run:
python 01_responses_api/structured_json_output.py

OR from inside the folder:
python structured_json_output.py
"""

import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client


PROMPT = """
Generate a JSON object containing:
- project_name
- programming_language
- difficulty_level
- estimated_hours

The topic is: Build a REST API using FastAPI.
Return only valid JSON.
"""


try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=PROMPT,
    )

    parsed_json = json.loads(response.output_text)

    print("\n=== STRUCTURED OUTPUT ===\n")
    print(json.dumps(parsed_json, indent=4))

except Exception as error:
    print(f"Structured output generation failed: {error}")
