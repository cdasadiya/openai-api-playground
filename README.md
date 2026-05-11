# OpenAI API Playground

Production-grade OpenAI API engineering examples using Python 3.

## Objectives

- Learn every major OpenAI API endpoint
- Build real-world Python examples
- Demonstrate production patterns
- Include structured outputs, streaming, embeddings, RAG, realtime APIs, and agents

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

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## Recommended Python Version

Python 3.12+

## Standards

- One concept per file
- Production-oriented examples
- Logging and validation
- Error handling
- Async support where appropriate
- Clear explanations inside every example
