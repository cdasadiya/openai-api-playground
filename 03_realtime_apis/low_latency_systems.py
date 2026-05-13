"""
File: low_latency_systems.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates low-latency OpenAI architecture patterns with timing metrics.

Concepts Covered:
- Connection reuse through centralized clients
- Async processing
- Streaming optimization
- Token optimization
- Request batching
- Performance timing metrics
- Full traceback debugging support

Run:
python 03_realtime_apis/low_latency_systems.py

OR from inside the folder:
python low_latency_systems.py
"""

import asyncio
import sys
import time
import traceback
from pathlib import Path
from statistics import mean


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import async_client, client


MODEL = "gpt-4.1-mini"


async def timed_streaming_request(prompt: str) -> dict[str, float]:
    """Measure streaming latency for one optimized prompt."""
    started_at = time.perf_counter()
    first_delta_at: float | None = None
    chunks = 0

    stream = await async_client.responses.create(
        model=MODEL,
        instructions="Answer in at most two short bullet points.",
        input=prompt,
        max_output_tokens=120,
        stream=True,
    )

    async for event in stream:
        if event.type == "response.output_text.delta":
            if first_delta_at is None:
                first_delta_at = time.perf_counter()
            chunks += 1
            print(event.delta, end="", flush=True)

    completed_at = time.perf_counter()
    print("\n")

    return {
        "time_to_first_delta_ms": (
            (first_delta_at - started_at) * 1000 if first_delta_at is not None else 0.0
        ),
        "total_ms": (completed_at - started_at) * 1000,
        "chunks": float(chunks),
    }


async def run_async_batch() -> list[dict[str, float]]:
    """Run multiple small requests concurrently to demonstrate async batching."""
    prompts = [
        "Give one low-latency API design tip.",
        "Give one token optimization tip.",
        "Give one streaming UX tip.",
    ]
    tasks = [timed_streaming_request(prompt) for prompt in prompts]
    return await asyncio.gather(*tasks)


def print_architecture_notes() -> None:
    """Explain production latency patterns before running timed calls."""
    print("\n=== LOW-LATENCY OPENAI PATTERNS ===\n")
    print(f"Connection reuse: centralized client id={id(client)} async_client id={id(async_client)}")
    print("Async processing: run independent requests concurrently with asyncio.gather.")
    print("Streaming optimization: render response.output_text.delta immediately.")
    print("Token optimization: constrain instructions and max_output_tokens.")
    print("Request batching: batch independent short tasks when user experience allows.")
    print("Buffering: keep audio/text buffers small enough for low latency but large enough to avoid jitter.")


async def main() -> None:
    """Application entry point with timing metrics and traceback debugging."""
    try:
        print_architecture_notes()
        batch_started_at = time.perf_counter()
        metrics = await run_async_batch()
        batch_total_ms = (time.perf_counter() - batch_started_at) * 1000

        print("=== PERFORMANCE METRICS ===")
        print(f"Requests completed: {len(metrics)}")
        print(f"Batch wall-clock time: {batch_total_ms:.2f} ms")
        print(
            "Average time to first delta: "
            f"{mean(item['time_to_first_delta_ms'] for item in metrics):.2f} ms"
        )
        print(f"Average total request time: {mean(item['total_ms'] for item in metrics):.2f} ms")
        print(f"Average streamed chunks: {mean(item['chunks'] for item in metrics):.2f}")
    except Exception as error:
        print("\n=== FULL ERROR TRACEBACK ===\n")
        traceback.print_exc()
        print(f"\nLow-latency systems example failed: {error}")
    finally:
        await async_client.close()


if __name__ == "__main__":
    asyncio.run(main())
