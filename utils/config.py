"""
File: config.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Centralized configuration loader for the project.

Concepts Covered:
- Environment variable loading
- Secure API key management
- GitHub Codespaces compatibility
- GitHub Actions compatibility
- Shared configuration pattern
- API key sanitization
"""

import os
from dotenv import load_dotenv


load_dotenv()


raw_api_key = os.getenv("OPENAI_API_KEY", "")

# Remove accidental spaces/newlines from Codespaces secrets or .env files
OPENAI_API_KEY = raw_api_key.strip()


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


if "\n" in OPENAI_API_KEY or "\r" in OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY contains invalid newline characters. "
        "Please recreate the secret without extra spaces or line breaks."
    )
