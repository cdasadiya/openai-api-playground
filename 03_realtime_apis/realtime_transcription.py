"""
File: realtime_transcription.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates realtime speech-to-text workflow design with live transcript events.

Concepts Covered:
- Realtime transcription sessions
- Incremental transcript deltas
- Audio buffer append events
- Streaming transcription architecture
- Full traceback debugging support

Run:
python 03_realtime_apis/realtime_transcription.py

OR from inside the folder:
python realtime_transcription.py
"""

import asyncio
import base64
import json
import sys
import traceback
from pathlib import Path
from typing import Any, AsyncIterator



PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from utils.openai_client import client


TRANSCRIPTION_MODEL = "gpt-4o-mini-transcribe"
REALTIME_URL = "wss://api.openai.com/v1/realtime?intent=transcription"


async def live_audio_chunks() -> AsyncIterator[bytes]:
    """Placeholder for microphone, telephony, or media-stream audio frames."""
    if False:
        yield b""
    return


async def configure_transcription_session(websocket: Any) -> None:
    """Configure transcription-only mode with incremental transcript events."""
    session_event = {
        "type": "transcription_session.update",
        "session": {
            "type": "transcription",
            "input_audio_transcription": {
                "model": TRANSCRIPTION_MODEL,
                "language": "en",
            },
            "turn_detection": {"type": "server_vad"},
        },
    }
    await websocket.send(json.dumps(session_event))
    print(f"Configured realtime transcription model={TRANSCRIPTION_MODEL}")


async def stream_audio(websocket: Any) -> None:
    """Append audio chunks to the transcription input buffer."""
    async for chunk in live_audio_chunks():
        event = {
            "type": "input_audio_buffer.append",
            "audio": base64.b64encode(chunk).decode("utf-8"),
        }
        await websocket.send(json.dumps(event))

    print("Audio placeholder completed without sending microphone frames.")


async def handle_transcription_events(websocket: Any) -> None:
    """Print incremental and completed transcript events as they arrive."""
    transcripts_by_item: dict[str, str] = {}

    async for raw_message in websocket:
        event = json.loads(raw_message)
        event_type = event.get("type", "unknown")

        if event_type == "conversation.item.input_audio_transcription.delta":
            item_id = event.get("item_id", "unknown_item")
            transcripts_by_item[item_id] = transcripts_by_item.get(item_id, "") + event.get(
                "delta", ""
            )
            print(f"\r[{item_id}] {transcripts_by_item[item_id]}", end="", flush=True)

        elif event_type == "conversation.item.input_audio_transcription.completed":
            item_id = event.get("item_id", "unknown_item")
            transcript = event.get("transcript", "")
            transcripts_by_item[item_id] = transcript
            print(f"\ncompleted [{item_id}]: {transcript}")

        elif event_type == "error":
            print(f"\nTranscription error event: {event}")

        else:
            print(f"server event: {event_type}")


async def run_transcription_architecture_demo(connect_to_api: bool = False) -> None:
    """Describe the realtime transcription pipeline or run it when devices exist."""
    print("\n=== REALTIME TRANSCRIPTION PIPELINE ===\n")
    print("1. Capture microphone or media-stream audio in small chunks.")
    print("2. Base64 encode each chunk and send input_audio_buffer.append.")
    print("3. Use server VAD or manual commits to segment speech turns.")
    print("4. Render delta events as captions before completion events arrive.")
    print("5. Store completed transcripts by item_id for correct turn ordering.")

    if not connect_to_api:
        print("\nCodespaces-safe mode: audio capture placeholder only.")
        return

    import websockets

    headers = {"Authorization": f"Bearer {client.api_key}"}
    async with websockets.connect(REALTIME_URL, additional_headers=headers) as websocket:
        await configure_transcription_session(websocket)
        await asyncio.gather(stream_audio(websocket), handle_transcription_events(websocket))


async def main() -> None:
    """Application entry point with full traceback debugging."""
    try:
        await run_transcription_architecture_demo()
    except Exception as error:
        print("\n=== FULL ERROR TRACEBACK ===\n")
        traceback.print_exc()
        print(f"\nRealtime transcription example failed: {error}")


if __name__ == "__main__":
    asyncio.run(main())
