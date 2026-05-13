"""
File: openai_client.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Reusable centralized OpenAI client configuration.

Concepts Covered:
- Shared API client
- Centralized SDK initialization
- Cleaner architecture
- HTTP/2 compatibility handling for Codespaces
"""

import sys
from pathlib import Path

import httpx
from openai import OpenAI


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.config import OPENAI_API_KEY


http_client = httpx.Client(
    http2=False,
    timeout=60.0
)


client = OpenAI(
    api_key=OPENAI_API_KEY,
    http_client=http_client
)
