# Responses API

Author: Chaitanya Dasadiya

This folder contains the complete Responses API examples. Each script uses the shared client from `utils/openai_client.py` and resolves imports from the repository root so it can run both from the repo root and inside GitHub Codespaces.

## Implemented Examples

- `basic_response.py` — basic text generation with the Responses API.
- `structured_json_output.py` — structured JSON generation with a strict schema.
- `system_prompting.py` — system-style instructions with input messages.
- `streaming_responses.py` — streaming Responses API output.
- `function_calling.py` — function call request payloads and argument inspection.
- `tool_calling.py` — hosted tool usage with the Responses API.
- `multi_turn_conversation.py` — follow-up turns using `previous_response_id`.
- `reasoning_models.py` — reasoning-oriented prompts.

## Run Examples

From the repository root:

```bash
python 02_responses_api/basic_response.py
python 02_responses_api/structured_json_output.py
python 02_responses_api/system_prompting.py
python 02_responses_api/streaming_responses.py
python 02_responses_api/function_calling.py
python 02_responses_api/tool_calling.py
python 02_responses_api/multi_turn_conversation.py
python 02_responses_api/reasoning_models.py
```

Or from inside this folder:

```bash
python basic_response.py
```
