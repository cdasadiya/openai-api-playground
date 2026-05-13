"""
File: structured_json_output.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates structured JSON generation using OpenAI Responses API.

Concepts Covered:
- Structured outputs
- JSON schema enforcement
- Reliable machine-readable responses
- Shared OpenAI client usage
- Portable import handling for Codespaces
- Production-safe structured generation

Run:
python 02_responses_api/structured_json_output.py

OR from inside the folder:
python structured_json_output.py
"""

import json
import sys
import traceback
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client


PROMPT = """
Generate project planning information for:
Build a REST API using FastAPI.
"""


try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=PROMPT,
        text={
            "format": {
                "type": "json_schema",
                "name": "project_schema",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "project_name": {
                            "type": "string"
                        },
                        "programming_language": {
                            "type": "string"
                        },
                        "difficulty_level": {
                            "type": "string"
                        },
                        "estimated_hours": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "project_name",
                        "programming_language",
                        "difficulty_level",
                        "estimated_hours"
                    ],
                    "additionalProperties": False
                }
            }
        }
    )

    parsed_json = json.loads(response.output_text)

    print("\n=== STRUCTURED OUTPUT ===\n")
    print(json.dumps(parsed_json, indent=4))

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nStructured output generation failed: {error}")
