"""
File: config.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Centralized configuration loader for the project.

Concepts Covered:
- Environment variable loading
- Secure API key management
- Optional organization and project scoping
- GitHub Codespaces compatibility
- GitHub Actions compatibility
- Shared configuration pattern
- API key sanitization
"""

import os
from dotenv import load_dotenv


load_dotenv()


def read_secret(name: str, required: bool = False) -> str:
    """
    Read an environment variable safely and remove accidental whitespace.

    Secrets should never be hard-coded in source files. This helper supports
    local `.env` files, GitHub Codespaces secrets, and CI/CD environments.
    """
    value = os.getenv(name, "").strip()

    if required and not value:
        raise EnvironmentError(
            f"{name} is missing.\n\n"
            "For GitHub Actions:\n"
            "Repository -> Settings -> Secrets and variables -> Actions\n\n"
            "For GitHub Codespaces:\n"
            "https://github.com/settings/codespaces\n\n"
            f"Create a secret named {name} and grant access to this repository."
        )

    if "\n" in value or "\r" in value:
        raise ValueError(
            f"{name} contains invalid newline characters. "
            "Please recreate the secret without extra spaces or line breaks."
        )

    return value


OPENAI_API_KEY = read_secret("OPENAI_API_KEY", required=True)

# Optional platform-scoping values. Leave blank for the default organization or
# project attached to the API key.
OPENAI_ORG_ID = read_secret("OPENAI_ORG_ID")
OPENAI_PROJECT_ID = read_secret("OPENAI_PROJECT_ID")
