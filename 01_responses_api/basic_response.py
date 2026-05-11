"""
File: basic_response.py

Purpose:
Demonstrates a basic OpenAI Responses API call using Python.

Concepts Covered:
- OpenAI client initialization
- Simple text generation
- Environment variable loading
- Basic error handling

Run:
python basic_response.py
"""

import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing from environment variables")


client = OpenAI(api_key=api_key)


try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Explain the importance of API design in software engineering."
    )

    print("\n=== MODEL RESPONSE ===\n")
    print(response.output_text)

except Exception as error:
    print(f"OpenAI API request failed: {error}")
