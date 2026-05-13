"""
File: live_streaming.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates token-by-token streaming responses with latency metrics.

Concepts Covered:
- Responses API streaming
- Async-ready architecture with the shared async OpenAI client
- Progressive chunk rendering
- Stream completion handling
- Time-to-first-token and total latency measurement
- Full traceback debugging support

Run:
python 03_realtime_apis/live_streaming.py

OR from inside the folder:
python live_streaming.py
"""

import asyncio
import sys
import time
import traceback
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import async_client


PROMPT = "Explain three practical techniques for lowering latency in AI applications."
MODEL = "gpt-4.1-mini"


async def stream_response() -> None:
    """Stream text deltas progressively and report latency measurements."""
    started_at = time.perf_counter()
    first_delta_at: float | None = None
    chunk_count = 0

    print("\n=== LIVE STREAMING RESPONSE ===\n")

    stream = await async_client.responses.create(
        model=MODEL,
        input=PROMPT,
        stream=True,
    )

    async for event in stream:
        if event.type == "response.output_text.delta":
            if first_delta_at is None:
                first_delta_at = time.perf_counter()

            chunk_count += 1
            print(event.delta, end="", flush=True)

        elif event.type == "response.completed":
            print("\n\nStream completed successfully.")

        elif event.type == "response.failed":
            print("\n\nStream failed. Inspect the event payload for details.")

    completed_at = time.perf_counter()
    first_token_ms = (
        (first_delta_at - started_at) * 1000 if first_delta_at is not None else 0.0
    )
    total_ms = (completed_at - started_at) * 1000

    print("\n=== STREAMING METRICS ===")
    print(f"Model: {MODEL}")
    print(f"Chunks received: {chunk_count}")
    print(f"Time to first text delta: {first_token_ms:.2f} ms")
    print(f"Total stream duration: {total_ms:.2f} ms")


async def main() -> None:
    """Application entry point with full traceback debugging."""
    try:
        await stream_response()
    except Exception as error:
        print("\n=== FULL ERROR TRACEBACK ===\n")
        traceback.print_exc()
        print(f"\nLive streaming request failed: {error}")


if __name__ == "__main__":
    asyncio.run(main())
