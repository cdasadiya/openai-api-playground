"""
File: basic_response.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates a basic OpenAI Responses API call using Python.

Concepts Covered:
- Shared OpenAI client usage
- Simple text generation
- Centralized configuration
- Basic error handling
- Portable import handling for Codespaces
- Full traceback debugging support

Run:
python 01_responses_api/basic_response.py

OR from inside the folder:
python basic_response.py
"""

import sys
import traceback
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client


try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Explain the importance of API design in software engineering."
    )

    print("\n=== MODEL RESPONSE ===\n")
    print(response.output_text)

except Exception as error:
    print("\n=== FULL ERROR TRACEBACK ===\n")
    traceback.print_exc()
    print(f"\nOpenAI API request failed: {error}")
