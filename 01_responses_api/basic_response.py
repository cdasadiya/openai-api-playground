"""
File: basic_response.py

Purpose:
Demonstrates a basic OpenAI Responses API call using Python.

Concepts Covered:
- Shared OpenAI client usage
- Simple text generation
- Centralized configuration
- Basic error handling

Run:
python 01_responses_api/basic_response.py
"""

from utils.openai_client import client


try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Explain the importance of API design in software engineering."
    )

    print("\n=== MODEL RESPONSE ===\n")
    print(response.output_text)

except Exception as error:
    print(f"OpenAI API request failed: {error}")
