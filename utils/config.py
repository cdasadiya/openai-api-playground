"""
File: config.py

Purpose:
Centralized configuration loader for the project.

Concepts Covered:
- Environment variable loading
- Secure API key management
- Shared configuration pattern
"""

import os
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is missing. Please configure your .env file."
    )
