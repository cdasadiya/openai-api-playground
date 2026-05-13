"""
File: websocket_connections.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates a production-style OpenAI Realtime WebSocket connection.

Concepts Covered:
- Realtime WebSocket lifecycle management
- Centralized OpenAI client configuration
- Async connection handling
- Reconnect and backoff strategy
- Realtime event logging
- Full traceback debugging support

Run:
python 03_realtime_apis/websocket_connections.py

OR from inside the folder:
python websocket_connections.py
"""

import asyncio
import json
import sys
import time
import traceback
from pathlib import Path
from typing import Any



PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client


REALTIME_MODEL = "gpt-realtime"
REALTIME_URL = f"wss://api.openai.com/v1/realtime?model={REALTIME_MODEL}"
MAX_RECONNECT_ATTEMPTS = 3


def log_event(direction: str, event: dict[str, Any]) -> None:
    """Print a compact realtime event log suitable for local debugging."""
    event_type = event.get("type", "unknown")
    event_id = event.get("event_id", "no_event_id")
    print(f"[{direction}] type={event_type} event_id={event_id}")


async def send_session_update(websocket: Any) -> None:
    """Configure the realtime session immediately after the socket opens."""
    session_event = {
        "type": "session.update",
        "session": {
            "type": "realtime",
            "instructions": (
                "You are a concise realtime assistant. Prioritize short, "
                "low-latency answers suitable for interactive applications."
            ),
        },
    }
    await websocket.send(json.dumps(session_event))
    log_event("client", session_event)


async def request_text_response(websocket: Any) -> None:
    """Send a small text prompt so the lifecycle can be observed quickly."""
    conversation_event = {
        "type": "conversation.item.create",
        "item": {
            "type": "message",
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Give one sentence about why WebSockets help realtime AI apps.",
                }
            ],
        },
    }
    response_event = {
        "type": "response.create",
        "response": {
            "modalities": ["text"],
        },
    }

    await websocket.send(json.dumps(conversation_event))
    log_event("client", conversation_event)
    await websocket.send(json.dumps(response_event))
    log_event("client", response_event)


async def receive_events(websocket: Any) -> None:
    """Receive and log events until the response completes or fails."""
    async for raw_message in websocket:
        event = json.loads(raw_message)
        log_event("server", event)

        if event.get("type") == "response.output_text.delta":
            print(event.get("delta", ""), end="", flush=True)

        if event.get("type") in {"response.done", "response.failed"}:
            print("\nRealtime response lifecycle completed.")
            return


async def connect_once() -> None:
    """Open one authenticated WebSocket connection and run a minimal exchange."""
    start_time = time.perf_counter()
    headers = {"Authorization": f"Bearer {client.api_key}"}

    import websockets

    async with websockets.connect(
        REALTIME_URL,
        additional_headers=headers,
        ping_interval=20,
        ping_timeout=20,
        close_timeout=10,
        max_queue=32,
    ) as websocket:
        print(f"Connected to OpenAI Realtime API with model={REALTIME_MODEL}")
        await send_session_update(websocket)
        await request_text_response(websocket)
        await receive_events(websocket)

    elapsed_ms = (time.perf_counter() - start_time) * 1000
    print(f"WebSocket closed cleanly in {elapsed_ms:.2f} ms")


async def run_with_reconnects() -> None:
    """Reconnect with exponential backoff for transient network failures."""
    import websockets

    for attempt in range(1, MAX_RECONNECT_ATTEMPTS + 1):
        try:
            await connect_once()
            return
        except (OSError, websockets.WebSocketException) as error:
            print(f"Realtime connection attempt {attempt} failed: {error}")
            if attempt == MAX_RECONNECT_ATTEMPTS:
                raise

            backoff_seconds = min(2 ** attempt, 10)
            print(f"Reconnecting in {backoff_seconds} seconds...")
            await asyncio.sleep(backoff_seconds)


async def main() -> None:
    """Application entry point with production-grade traceback logging."""
    try:
        await run_with_reconnects()
    except Exception as error:
        print("\n=== FULL ERROR TRACEBACK ===\n")
        traceback.print_exc()
        print(f"\nRealtime WebSocket example failed: {error}")


if __name__ == "__main__":
    asyncio.run(main())
