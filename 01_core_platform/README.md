# Core Platform

Author: Chaitanya Dasadiya  
GitHub: https://github.com/cdasadiya

Production-focused OpenAI platform examples for authentication, secrets, organization and project scoping, usage tracking, billing concepts, rate limits, model discovery, tokens, and cost optimization.

---

## Setup

Install dependencies from the repository root:

```bash
pip install -r requirements.txt
```

Set the required API key in GitHub Codespaces secrets, your shell, or a local `.env` file:

```bash
OPENAI_API_KEY=sk-...
```

Optional platform scoping variables:

```bash
OPENAI_ORG_ID=org_...
OPENAI_PROJECT_ID=proj_...
```

Secrets should stay in environment variables, Codespaces secrets, CI/CD secrets, or a dedicated secret manager. Do not commit `.env` files or hard-code keys in Python source files.

---

## Examples

Run from the repository root:

```bash
python 01_core_platform/authentication.py
python 01_core_platform/api_keys.py
python 01_core_platform/organizations.py
python 01_core_platform/projects.py
python 01_core_platform/usage_tracking.py
python 01_core_platform/billing.py
python 01_core_platform/rate_limits.py
python 01_core_platform/models.py
python 01_core_platform/tokens.py
python 01_core_platform/pricing_optimization.py
```

Each script also supports running from inside `01_core_platform/` because it adds the repository root to `sys.path` before importing shared utilities.

---

## File Guide

- `authentication.py` — validates secure authentication with `OPENAI_API_KEY` and performs a small authenticated request.
- `api_keys.py` — demonstrates safe API key loading, `.env` usage, key masking, and secret management guidance.
- `organizations.py` — explains multi-organization scoping with optional `OPENAI_ORG_ID`.
- `projects.py` — explains project-based isolation with optional `OPENAI_PROJECT_ID`.
- `usage_tracking.py` — extracts input, output, and total token usage from a Responses API result.
- `billing.py` — explains billing concepts and includes a placeholder structure for future billing integrations.
- `rate_limits.py` — demonstrates retry logic with exponential backoff for graceful rate-limit handling.
- `models.py` — lists available models and prints model metadata in a clean terminal format.
- `tokens.py` — estimates prompt tokens and compares estimates with actual API usage metadata.
- `pricing_optimization.py` — demonstrates model selection, token reduction, batching, caching, and cost optimization practices.
