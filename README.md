# 🚀 OpenAI API Playground

> A **production-focused** collection of comprehensive OpenAI API examples built with Python. Learn scalable, maintainable, and production-ready AI systems using modern OpenAI APIs, structured engineering patterns, and real-world architecture best practices.

<div align="center">

[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![OpenAI API](https://img.shields.io/badge/OpenAI-API-412991?style=flat-square&logo=openai)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

</div>

---

## 👨‍💻 About This Repository

This repository is a **comprehensive, production-grade reference** for OpenAI API engineering. It provides:

- ✅ **20+ fully implemented examples** across all major OpenAI API categories
- ✅ **Production-ready patterns** for authentication, error handling, and configuration
- ✅ **Structured examples** showing how to build scalable AI systems
- ✅ **Real-world use cases** including RAG, agents, realtime systems, and more
- ✅ **Best practices** for security, cost optimization, and deployment

**Perfect for:**
- 🎓 AI engineering interview preparation
- 📚 Learning OpenAI API fundamentals
- 🏗️ Production AI architecture reference
- 🤖 Building AI SaaS products
- 🔧 Internal AI tooling and automation

---

## 👤 Author

**Chaitanya Dasadiya**

- 🔗 GitHub: [@cdasadiya](https://github.com/cdasadiya)
- 🎯 Focus Areas: AI Engineering, Python Development, OpenAI APIs, Production Systems

---

## 📋 Repository Goals

This repository aims to become a **complete professional OpenAI engineering reference** covering:

| Category | Coverage |
|----------|----------|
| **Core Platform** | Authentication, API keys, organizations, projects, usage, billing, rate limits |
| **Text & Reasoning** | Responses API, streaming, structured outputs, function calling, tool calling |
| **Realtime Systems** | WebSocket, live streaming, voice, transcription, interrupt handling |
| **Audio & Vision** | Speech-to-text, translation, TTS, image understanding, OCR |
| **AI Agents** | Multi-agent systems, orchestration, memory, MCP integration |
| **Infrastructure** | RAG pipelines, embeddings, fine-tuning, deployment, monitoring |

---

## 📁 Repository Structure

```
openai-api-playground/
├── 01_core_platform/          # Authentication, billing, rate limits, tokens
├── 02_responses_api/          # Chat, streaming, structured outputs, tool calling
├── 03_realtime_apis/          # WebSocket, voice, low-latency systems
├── 04_audio_apis/             # Transcription, translation, TTS (coming soon)
├── 05_vision_apis/            # Image understanding, OCR (coming soon)
├── utils/                     # Shared OpenAI client and utilities
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
└── README.md                 # This file
```

### 📚 Folder Guide

| Folder | Purpose |
|--------|---------|
| **`01_core_platform/`** | Production foundations: authentication, API keys, organizations, projects, usage tracking, billing, rate limits, models, tokens, pricing optimization |
| **`02_responses_api/`** | Complete text API examples: basic responses, structured output, streaming, function calling, tool calling, multi-turn conversations, reasoning models |
| **`03_realtime_apis/`** | Realtime API examples: WebSocket connections, live streaming, voice systems, transcription, interrupt handling, low-latency architectures |
| **`04_audio_apis/`** | Audio API examples: transcription, translation, text-to-speech, voice workflows (⏳ coming soon) |
| **`05_vision_apis/`** | Vision API examples: image understanding, OCR, multi-image analysis, reasoning (⏳ coming soon) |
| **`utils/`** | Shared configuration, OpenAI client factory, and helper utilities |

---

## ✅ Implementation Status

### 🟢 Core Platform

All Core Platform examples are **fully implemented** in `01_core_platform/`:

```
✓ authentication.py          - Secure authentication validation
✓ api_keys.py                - Safe API key management
✓ organizations.py           - Multi-organization scoping
✓ projects.py                - Project-based isolation
✓ usage_tracking.py          - Token usage analysis
✓ billing.py                 - Billing concepts and tracking
✓ rate_limits.py             - Rate limit handling with exponential backoff
✓ models.py                  - Model discovery and metadata
✓ tokens.py                  - Token estimation and comparison
✓ pricing_optimization.py    - Cost optimization strategies
```

### 🟢 Responses API

All Responses API examples are **fully implemented** in `02_responses_api/`:

```
✓ basic_response.py               - Simple text generation
✓ structured_json_output.py       - Structured outputs with schema
✓ system_prompting.py             - System instructions
✓ streaming_responses.py          - Real-time streaming
✓ function_calling.py             - Function invocation
✓ tool_calling.py                 - Tool orchestration
✓ multi_turn_conversation.py      - Conversational AI
✓ reasoning_models.py             - Advanced reasoning models
```

### 🟢 Realtime APIs

All Realtime API examples are **fully implemented** in `03_realtime_apis/`:

```
✓ websocket_connections.py    - WebSocket fundamentals
✓ live_streaming.py           - Audio stream handling
✓ realtime_voice.py           - Voice interaction systems
✓ realtime_transcription.py   - Real-time speech-to-text
✓ interrupt_handling.py       - User interruption patterns
✓ low_latency_systems.py      - Optimized latency architecture
```

### 🟡 Audio APIs (Coming Soon)

```
⏳ Speech-to-text
⏳ Transcription
⏳ Translation
⏳ Text-to-speech
⏳ Voice synthesis
⏳ Audio generation
```

### 🟡 Vision APIs (Coming Soon)

```
⏳ Image understanding
⏳ OCR
⏳ Multi-image analysis
⏳ Vision reasoning
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- OpenAI API key from [platform.openai.com](https://platform.openai.com)
- Git and basic terminal knowledge

### 1. Clone the Repository

```bash
git clone https://github.com/cdasadiya/openai-api-playground.git
cd openai-api-playground
```

### 2. Choose Your Setup Method

#### **Option A: Local Development** (Recommended)

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate          # macOS/Linux
# or
.venv\Scripts\activate             # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "OPENAI_API_KEY=sk-proj-your_api_key_here" > .env

# Run an example
python 02_responses_api/basic_response.py
```

#### **Option B: GitHub Codespaces** (No setup required)

1. Click **Code** → **Codespaces** → **Create codespace on main**
2. Add GitHub Codespaces secret:
   - Settings → Secrets and variables → Codespaces
   - Name: `OPENAI_API_KEY`
   - Value: Your OpenAI API key
   - Grant access to `openai-api-playground`
3. Run: `python 02_responses_api/basic_response.py`

### 3. Run Your First Example

```bash
# Run a simple Responses API example
python 02_responses_api/basic_response.py

# Or run a Core Platform example
python 01_core_platform/authentication.py
```

---

## 🔐 API Key Setup Guide

### Local Development with `.env`

```bash
# 1. Create .env file in repository root
OPENAI_API_KEY=sk-proj-your_api_key_here

# Optional: Set organization and project scope
OPENAI_ORG_ID=org-...
OPENAI_PROJECT_ID=proj-...
```

### GitHub Codespaces with Secrets

```
Settings → Codespaces → Secrets → New repository secret
Name: OPENAI_API_KEY
Value: sk-proj-your_api_key_here
Repository access: openai-api-playground
```

### 🔒 Security Best Practices

**✅ DO:**
- ✔️ Store API keys in `.env` files locally
- ✔️ Use GitHub Codespaces secrets for cloud development
- ✔️ Use environment variables in production
- ✔️ Add `.env` to `.gitignore`
- ✔️ Rotate compromised keys immediately

**❌ DON'T:**
- ❌ Commit API keys to GitHub
- ❌ Hardcode keys in Python files
- ❌ Push `.env` files to repositories
- ❌ Expose keys in screenshots/logs
- ❌ Store secrets in public repositories

### Recommended `.gitignore`

```gitignore
# Environment
.env
.env.*
!.env.example

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual Environment
.venv/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
```

---

## 📊 Complete API Coverage Checklist

### ✅ Implemented

- [x] **Core Platform** — 10/10 topics covered
- [x] **Responses API** — 8/8 topics covered  
- [x] **Realtime APIs** — 6/6 topics covered

### 🟡 Planned

- [ ] **Audio APIs** — 0/6 topics covered
- [ ] **Vision APIs** — 0/4 topics covered
- [ ] **Image APIs** — 0/5 topics covered
- [ ] **Embeddings & Search** — 0/5 topics covered
- [ ] **Fine-Tuning** — 0/5 topics covered
- [ ] **Assistants & Agents** — 0/6 topics covered
- [ ] **Files & Data** — 0/4 topics covered
- [ ] **Safety & Moderation** — 0/4 topics covered
- [ ] **Production Engineering** — 0/9 topics covered
- [ ] **AI Architecture** — 0/6 topics covered
- [ ] **Deployment** — 0/6 topics covered
- [ ] **Ecosystem Integrations** — 0/6 topics covered
- [ ] **Advanced Systems** — 0/9 topics covered

---

## 🏗️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Language** | Python 3.12+ |
| **AI Platform** | OpenAI API (latest) |
| **Environment** | Python Venv, Python-dotenv |
| **Patterns** | Async/await, Streaming, Structured outputs |
| **Focus** | Production-ready, secure, scalable |

---

## 💡 Engineering Principles

This repository follows **production-grade standards**:

- 🔐 **Secure Architecture** — Centralized client, environment-based configuration
- 📦 **Structured Outputs** — Type-safe, schema-validated responses
- 🔄 **Error Handling** — Graceful failures, exponential backoff retry logic
- 📊 **Observability** — Logging, debugging support, usage tracking
- ⚡ **Performance** — Streaming support, async operations, caching patterns
- 🚀 **Scalability** — Reusable utilities, modular design
- 🛡️ **Security** — Secret management, no hardcoded keys
- 🐳 **Compatibility** — Codespaces-ready, Docker-compatible

---

## 📚 Recommended Learning Path

Follow this progression to master OpenAI APIs:

1. **Start Here** → `01_core_platform/authentication.py` — Validate setup
2. **Basics** → `02_responses_api/basic_response.py` — Text generation
3. **Structured** → `02_responses_api/structured_json_output.py` — Typed outputs
4. **Real-time** → `02_responses_api/streaming_responses.py` — Live responses
5. **Tools** → `02_responses_api/function_calling.py` — API integration
6. **Advanced** → `02_responses_api/tool_calling.py` — Tool orchestration
7. **Conversation** → `02_responses_api/multi_turn_conversation.py` — Memory
8. **Reasoning** → `02_responses_api/reasoning_models.py` — Complex tasks
9. **Voice** → `03_realtime_apis/realtime_voice.py` — Voice systems
10. **Production** → Scale to production with monitoring and optimization

---

## 💼 Use Cases

This repository can accelerate development for:

- 🎓 **Interview Prep** — AI engineering interview preparation and problem solving
- 📖 **Learning** — Understanding OpenAI API capabilities and best practices
- 🏛️ **Architecture** — Reference implementations for production AI systems
- 🚀 **SaaS** — Building AI-powered SaaS products and platforms
- 🔧 **Internal Tools** — Creating internal AI tooling and automation
- 🎨 **Prototyping** — Rapid AI prototyping and experimentation
- 🤖 **Agents** — Multi-agent systems and orchestration
- 🎬 **Multimodal** — Combining text, voice, vision, and audio

---

## 🤝 Contributing

Contributions are **welcome and appreciated!** We're looking for help in these areas:

- ✨ **New Examples** — Additional OpenAI API examples
- 🏗️ **Architecture** — RAG systems, workflow patterns, agent orchestration
- 🔄 **Realtime** — Voice, video, and low-latency applications
- 🤖 **Agents** — Multi-agent systems, tool orchestration
- 🚀 **Deployment** — CI/CD, Docker, Kubernetes, serverless
- ⚡ **Performance** — Optimization, benchmarking, caching
- 🛡️ **Production** — Monitoring, logging, observability
- 📚 **Documentation** — Improving guides and examples

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

This repository is licensed under the **MIT License**.

See [LICENSE](LICENSE) file for complete details.

---

## 🔗 Quick Links

- 📖 [OpenAI API Documentation](https://platform.openai.com/docs)
- 🔑 [Get Your API Key](https://platform.openai.com/account/api-keys)
- 🐦 [OpenAI on Twitter/X](https://twitter.com/OpenAI)
- 🚀 [OpenAI Blog](https://openai.com/blog)
- 💬 [OpenAI Community](https://community.openai.com)

---

<div align="center">

**Made with ❤️ by [Chaitanya Dasadiya](https://github.com/cdasadiya)**

⭐ If this helped you, please star this repository! ⭐

</div>
