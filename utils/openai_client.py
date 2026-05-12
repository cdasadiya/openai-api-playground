"""
File: openai_client.py

Purpose:
Reusable centralized OpenAI client configuration.

Concepts Covered:
- Shared API client
- Centralized SDK initialization
- Cleaner architecture
"""

from openai import OpenAI

from utils.config import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)
