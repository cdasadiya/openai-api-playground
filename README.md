# OpenAI API Playground

A production-focused collection of OpenAI API examples built with Python.

This repository demonstrates how to build scalable, maintainable, and production-ready AI systems using modern OpenAI APIs, structured engineering patterns, and real-world architecture practices.

---

# Author

**Chaitanya Dasadiya**

- GitHub: https://github.com/cdasadiya
- Focus Areas: AI Engineering, Python Development, OpenAI APIs, Automation

---

# Repository Goals

This repository is designed to become a complete professional OpenAI engineering reference covering:

- OpenAI APIs
- AI agents
- Multi-modal systems
- Production AI architectures
- RAG pipelines
- Realtime systems
- Fine-tuning
- Deployment systems
- AI infrastructure engineering

---

# Repository Structure

The examples are grouped by API area so related scripts stay together:

```text
01_core_platform/
02_responses_api/
03_realtime_apis/
04_audio_apis/
05_vision_apis/
utils/
```

## Folder Guide

- `01_core_platform/` — production platform foundations such as authentication, API keys, organizations, projects, usage tracking, billing, rate limits, models, tokens, and pricing optimization.
- `02_responses_api/` — all Responses API examples, including basic responses, structured output, prompting, streaming, function calling, tool calling, multi-turn conversations, and reasoning prompts.
- `03_realtime_apis/` — realtime API examples and low-latency systems.
- `04_audio_apis/` — audio API examples for transcription, translation, text-to-speech, and voice workflows.
- `05_vision_apis/` — vision API examples for image understanding, OCR, and vision reasoning.
- `utils/` — shared configuration and OpenAI client utilities used by runnable examples.

---

# Current Implemented Examples

## Core Platform

All implemented Core Platform examples live in `01_core_platform/`.

- [x] `01_core_platform/authentication.py`
- [x] `01_core_platform/api_keys.py`
- [x] `01_core_platform/organizations.py`
- [x] `01_core_platform/projects.py`
- [x] `01_core_platform/usage_tracking.py`
- [x] `01_core_platform/billing.py`
- [x] `01_core_platform/rate_limits.py`
- [x] `01_core_platform/models.py`
- [x] `01_core_platform/tokens.py`
- [x] `01_core_platform/pricing_optimization.py`

## Running Core Platform Examples

Install dependencies:

```bash
pip install -r requirements.txt
```

Set `OPENAI_API_KEY` in your environment, GitHub Codespaces secret, or local `.env` file. Optionally set `OPENAI_ORG_ID` and `OPENAI_PROJECT_ID` when you need explicit organization or project scoping. Then run examples from the repository root:

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

Each example also supports running from inside its own folder because it adds the repository root to `sys.path` before importing shared utilities.

## Responses API

All implemented Responses API examples live in `02_responses_api/`.

- [x] `02_responses_api/basic_response.py`
- [x] `02_responses_api/structured_json_output.py`
- [x] `02_responses_api/system_prompting.py`
- [x] `02_responses_api/streaming_responses.py`
- [x] `02_responses_api/function_calling.py`
- [x] `02_responses_api/tool_calling.py`
- [x] `02_responses_api/multi_turn_conversation.py`
- [x] `02_responses_api/reasoning_models.py`

## Running Responses API Examples

Install dependencies:

```bash
pip install -r requirements.txt
```

Set `OPENAI_API_KEY` in your environment, GitHub Codespaces secret, or local `.env` file. Then run examples from the repository root:

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

Each example also supports running from inside its own folder because it adds the repository root to `sys.path` before importing shared utilities.

---

# Complete OpenAI API Topics Checklist

## Core Platform

- [x] Authentication
- [x] API keys
- [x] Organizations
- [x] Projects
- [x] Usage tracking
- [x] Billing
- [x] Rate limits
- [x] Models
- [x] Tokens
- [x] Pricing optimization

---

## Text & Reasoning APIs

- [x] Responses API
- [x] Streaming
- [x] Structured outputs
- [x] JSON schema outputs
- [x] Function calling
- [x] Tool calling
- [x] Multi-turn conversations
- [x] Reasoning models
- [ ] Chat Completions

---

## Realtime APIs

- [ ] WebSocket connections
- [ ] Live streaming
- [ ] Realtime voice
- [ ] Realtime transcription
- [ ] Interrupt handling
- [ ] Low-latency systems

---

## Audio APIs

- [ ] Speech-to-text
- [ ] Transcription
- [ ] Translation
- [ ] Text-to-speech
- [ ] Voice synthesis
- [ ] Audio generation

---

## Vision APIs

- [ ] Image understanding
- [ ] OCR
- [ ] Multi-image analysis
- [ ] Vision reasoning

---

## Image APIs

- [ ] Image generation
- [ ] Image editing
- [ ] Variations
- [ ] Inpainting
- [ ] Style transfer

---

## Embeddings & Search

- [ ] Embeddings
- [ ] Semantic search
- [ ] Similarity search
- [ ] RAG pipelines
- [ ] Vector databases

---

## Fine-Tuning

- [ ] Dataset preparation
- [ ] Training jobs
- [ ] Hyperparameters
- [ ] Evaluation
- [ ] Deployment

---

## Assistants & Agents

- [ ] Agents SDK
- [ ] Tool orchestration
- [ ] Memory
- [ ] Sessions
- [ ] MCP
- [ ] Multi-agent systems

---

## File & Data APIs

- [ ] Files API
- [ ] Uploads
- [ ] Batch processing
- [ ] Vector stores

---

## Safety & Moderation

- [ ] Moderation API
- [ ] Safety systems
- [ ] Guardrails
- [ ] Prompt injection prevention

---

## Production Engineering

- [ ] Scaling
- [ ] Monitoring
- [ ] Observability
- [ ] Logging
- [ ] Retry systems
- [ ] Queue systems
- [ ] Caching
- [ ] Load balancing
- [ ] Cost optimization

---

## AI Architecture

- [ ] RAG systems
- [ ] AI workflows
- [ ] Agent systems
- [ ] Multi-modal systems
- [ ] Hybrid AI architectures
- [ ] Autonomous systems

---

## Deployment

- [ ] Docker
- [ ] Kubernetes
- [ ] Serverless
- [ ] Edge deployment
- [ ] CI/CD
- [ ] Cloud deployment

---

## Ecosystem Integrations

- [ ] LangChain
- [ ] LlamaIndex
- [ ] Pinecone
- [ ] Weaviate
- [ ] Supabase
- [ ] Vercel AI SDK

---

## Advanced Systems

- [ ] Long-context systems
- [ ] AI memory systems
- [ ] Planning systems
- [ ] Reflection loops
- [ ] Self-improving agents
- [ ] Tool ecosystems
- [ ] Computer-use agents
- [ ] Browser agents
- [ ] Coding agents

---

# Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.12+ |
| AI Platform | OpenAI API |
| Environment | Virtualenv / dotenv |
| Patterns | Async IO, Structured Outputs, Streaming |
| Focus | Production-ready AI engineering |

---

# Quick Start

## Clone the Repository

```bash
git clone https://github.com/cdasadiya/openai-api-playground.git
cd openai-api-playground
```

---

# OpenAI API Key Setup Guide

This repository supports:

1. Local machine development
2. GitHub Codespaces development

---

# Method 1: Local Machine Setup

## Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create `.env` File

```env
OPENAI_API_KEY=sk-proj-your_api_key_here
```

---

## Run the Project

```bash
python 02_responses_api/basic_response.py
```

---

# Method 2: GitHub Codespaces Setup

## Create Codespaces Secret

Go to:

```text
GitHub → Settings → Codespaces → Secrets
```

Create:

```text
Name: OPENAI_API_KEY
Value: sk-proj-your_api_key_here
```

Grant access to:

```text
openai-api-playground
```

---

## Verify API Key

```bash
echo $OPENAI_API_KEY
```

---

## Run the Project

```bash
python 02_responses_api/basic_response.py
```

---

# API Key Security Best Practices

## Never Do These

❌ Never commit API keys to GitHub

❌ Never hardcode API keys inside Python files

❌ Never push `.env` files

❌ Never expose API keys in screenshots

❌ Never store secrets in public repositories

---

## Correct Secure Approach

✅ Use `.env` locally

✅ Use GitHub Secrets for Codespaces and Actions

✅ Add `.env` to `.gitignore`

✅ Rotate compromised keys immediately

✅ Validate AI outputs before execution

---

# Recommended `.gitignore`

```gitignore
.env
.env.*
__pycache__/
*.pyc
.venv/
venv/
```

---

# Engineering Principles

This repository follows production-focused engineering standards:

- Centralized OpenAI client architecture
- Environment-based configuration
- Structured outputs
- Reusable utilities
- Debugging support
- Error handling
- Secure secret management
- Codespaces compatibility
- Production-safe patterns

---

# Recommended Learning Path

1. Responses API
2. Structured Outputs
3. Streaming
4. Function Calling
5. Embeddings
6. RAG
7. Agents
8. Realtime APIs
9. Fine-Tuning
10. Production AI Systems

---

# Use Cases

This repository can be used for:

- AI engineering interview preparation
- OpenAI API learning
- Production AI architecture references
- AI SaaS development
- Internal AI tooling
- Rapid AI prototyping
- Agent system experimentation
- Multi-modal AI systems

---

# Contributing

Contributions are welcome.

Suggested contribution areas:

- New OpenAI API examples
- RAG systems
- Realtime applications
- AI agent orchestration
- CI/CD automation
- Deployment examples
- Performance optimization
- Production monitoring

---

# License

This repository is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
