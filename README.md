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

```text
01_responses_api/
02_chat_completions/
03_streaming/
04_structured_outputs/
05_function_calling/
06_reasoning_models/
07_realtime_api/
08_audio_apis/
09_vision_apis/
10_image_generation/
11_embeddings_and_search/
12_rag_systems/
13_fine_tuning/
14_agents_and_mcp/
15_file_and_vector_apis/
16_safety_and_guardrails/
17_production_engineering/
18_ai_architecture/
19_deployment/
20_ecosystem_integrations/
21_advanced_agent_systems/
22_full_projects/
utils/
```

---

# Current Implemented Examples

## Responses API

### Completed

- [x] basic_response.py
- [x] structured_json_output.py
- [x] system_prompting.py

### Planned

- [ ] Streaming responses
- [ ] Function calling
- [ ] Tool calling
- [ ] Multi-turn conversations
- [ ] Reasoning models

---

# Complete OpenAI API Topics Checklist

## Core Platform

- [ ] Authentication
- [ ] API keys
- [ ] Organizations
- [ ] Projects
- [ ] Usage tracking
- [ ] Billing
- [ ] Rate limits
- [ ] Models
- [ ] Tokens
- [ ] Pricing optimization

---

## Text & Reasoning APIs

- [x] Responses API
- [ ] Chat Completions
- [ ] Streaming
- [x] Structured outputs
- [x] JSON schema outputs
- [ ] Function calling
- [ ] Tool calling
- [ ] Reasoning models

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
python 01_responses_api/basic_response.py
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
python 01_responses_api/basic_response.py
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
