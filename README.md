# OpenAI API Playground

A production-focused collection of OpenAI API examples built with Python.

This repository is designed for developers who want more than quick-start snippets. It demonstrates how to build reliable, scalable, and maintainable AI applications using modern OpenAI APIs and engineering patterns.

---

## Author

**Chirag Dasadiya**

- GitHub: https://github.com/cdasadiya
- Focus Areas: AI Engineering, Python Development, OpenAI APIs, Automation

---

## What You’ll Learn

- Responses API workflows
- Chat Completions and multi-turn conversations
- Streaming responses
- Function calling and tool usage
- Structured outputs with JSON schemas
- Embeddings and semantic search
- Retrieval-Augmented Generation (RAG)
- Image generation pipelines
- Speech-to-text and text-to-speech
- Realtime API integrations
- AI agents and orchestration
- Evaluation frameworks
- Guardrails and safety patterns
- Batch processing
- Fine-tuning workflows
- MCP server integrations
- Cost optimization strategies
- Production deployment patterns

---

## Repository Structure

```text
01_responses_api/
02_chat_completions/
03_streaming/
04_function_calling/
05_structured_outputs/
06_embeddings/
07_rag/
08_image_generation/
09_audio_transcription/
10_text_to_speech/
11_realtime_api/
12_agents/
13_eval_frameworks/
14_guardrails/
15_batch_processing/
16_fine_tuning/
17_mcp_servers/
18_cost_optimization/
19_production_patterns/
20_full_projects/
```

Each folder focuses on one domain and contains practical examples that can be adapted for real-world applications.

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.12+ |
| AI Platform | OpenAI API |
| Environment | Virtualenv / dotenv |
| Patterns | Async IO, Structured Outputs, Streaming |
| Focus | Production-ready AI engineering |

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/cdasadiya/openai-api-playground.git
cd openai-api-playground
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Example Workflow

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain Retrieval-Augmented Generation in simple terms."
)

print(response.output_text)
```

---

## Engineering Principles

This repository prioritizes practical software engineering patterns instead of isolated toy examples.

### Included Standards

- Clear separation of concerns
- Typed and structured outputs
- Error handling and retries
- Logging and observability
- Environment-based configuration
- Async support where applicable
- Scalable project organization
- Reusable utility patterns

---

## Recommended Learning Path

If you are new to OpenAI APIs, follow this order:

1. Responses API
2. Chat Completions
3. Streaming
4. Function Calling
5. Structured Outputs
6. Embeddings
7. RAG
8. Agents
9. Production Patterns
10. Full Projects

---

## Use Cases

This repository can be used for:

- AI engineering interview preparation
- Internal company AI tooling
- Rapid AI prototyping
- Developer education
- Production AI architecture references
- Building SaaS AI products
- Learning advanced OpenAI API capabilities

---

## Security Notes

- Never commit API keys
- Use environment variables for secrets
- Add rate limiting in production systems
- Validate model outputs before execution
- Monitor token usage and costs

---

## Contributing

Contributions are welcome.

Suggested contribution areas:

- Additional API examples
- Benchmarking workflows
- Agent orchestration patterns
- Testing strategies
- CI/CD automation
- Deployment examples
- Performance optimization

---

## License

This repository is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
