"""
File: interrupt_handling.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates safe cancellation and cleanup for active realtime streams.

Concepts Covered:
- Cancelling active streaming requests
- Keyboard interruption handling
- Async task cancellation
- Session cleanup and graceful shutdown
- Full traceback debugging support

Run:
python 03_realtime_apis/interrupt_handling.py

OR from inside the folder:
python interrupt_handling.py
"""

import asyncio
import sys
import traceback
from contextlib import suppress
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import async_client


MODEL = "gpt-4.1-mini"
PROMPT = "Slowly explain how graceful shutdown works in realtime AI systems."


async def consume_stream(stop_event: asyncio.Event) -> None:
    """Consume a streaming response until completion or cancellation."""
    stream = await async_client.responses.create(
        model=MODEL,
        input=PROMPT,
        stream=True,
    )

    async for event in stream:
        if stop_event.is_set():
            print("\nStop requested. Exiting stream consumer.")
            return

        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)

        if event.type in {"response.completed", "response.failed"}:
            print("\nStream finished.")
            return


async def cleanup_session() -> None:
    """Release local resources before the process exits."""
    # For WebSocket Realtime sessions, this is where you would send:
    # - response.cancel to stop generation
    # - input_audio_buffer.clear to drop queued microphone audio
    # - output_audio_buffer.clear to stop playback on supported clients
    # - websocket.close to terminate the network session
    await async_client.close()
    print("Cleanup complete: OpenAI async client closed.")


async def main() -> None:
    """Run a cancellable stream with robust KeyboardInterrupt handling."""
    stop_event = asyncio.Event()
    stream_task = asyncio.create_task(consume_stream(stop_event))

    try:
        await stream_task
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received. Cancelling active realtime work...")
        stop_event.set()
        stream_task.cancel()
        with suppress(asyncio.CancelledError):
            await stream_task
    except asyncio.CancelledError:
        print("\nStream task was cancelled by the runtime.")
        raise
    except Exception as error:
        print("\n=== FULL ERROR TRACEBACK ===\n")
        traceback.print_exc()
        print(f"\nInterrupt handling example failed: {error}")
    finally:
        await cleanup_session()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nShutdown completed after keyboard interruption.")
