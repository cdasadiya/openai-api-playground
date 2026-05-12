"""
File: config.py

Purpose:
Centralized configuration loader for the project.

Concepts Covered:
- Environment variable loading
- Secure API key management
- GitHub Codespaces compatibility
- GitHub Actions compatibility
- Shared configuration pattern
"""

import os
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if not OPENAI_API_KEY:
    raise EnvironmentError(
        "OPENAI_API_KEY is missing.\n\n"
        "For GitHub Actions:\n"
        "Repository -> Settings -> Secrets and variables -> Actions\n\n"
        "For GitHub Codespaces:\n"
        "https://github.com/settings/codespaces\n\n"
        "Create a Codespaces secret named OPENAI_API_KEY\n"
        "and grant access to this repository."
    )
