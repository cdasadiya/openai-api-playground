"""
File: realtime_voice.py

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Purpose:
Demonstrates realtime voice interaction architecture for OpenAI Realtime APIs.

Concepts Covered:
- Voice session configuration
- Microphone input placeholders
- Streaming audio output structure
- Realtime session events
- Voice AI pipeline design
- Full traceback debugging support

Run:
python 03_realtime_apis/realtime_voice.py

OR from inside the folder:
python realtime_voice.py
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


REALTIME_MODEL = "gpt-realtime"
REALTIME_URL = f"wss://api.openai.com/v1/realtime?model={REALTIME_MODEL}"
VOICE_NAME = "alloy"


async def microphone_audio_chunks() -> AsyncIterator[bytes]:
    """
    Placeholder for microphone PCM16 chunks.

    In production, replace this generator with PyAudio, sounddevice, WebRTC,
    browser media capture, SIP media frames, or another audio source that yields
    small PCM16 frames. Keep chunks small to reduce input latency.
    """
    if False:
        yield b""
    return


async def send_voice_session_update(websocket: Any) -> None:
    """Configure a speech-to-speech realtime session."""
    session_event = {
        "type": "session.update",
        "session": {
            "type": "realtime",
            "instructions": (
                "You are a friendly voice assistant. Keep spoken answers brief, "
                "natural, and interruptible."
            ),
            "audio": {
                "input": {
                    "format": {"type": "audio/pcm", "rate": 24000},
                    "turn_detection": {"type": "server_vad"},
                },
                "output": {
                    "format": {"type": "audio/pcm", "rate": 24000},
                    "voice": VOICE_NAME,
                },
            },
        },
    }
    await websocket.send(json.dumps(session_event))
    print("Configured realtime voice session.")


async def stream_microphone_audio(websocket: Any) -> None:
    """Stream microphone chunks into the Realtime input audio buffer."""
    async for chunk in microphone_audio_chunks():
        append_event = {
            "type": "input_audio_buffer.append",
            "audio": base64.b64encode(chunk).decode("utf-8"),
        }
        await websocket.send(json.dumps(append_event))

    # For this runnable educational example, no real microphone is attached.
    # A production app would commit after user speech or rely on server VAD.
    print("Microphone placeholder completed without sending audio.")


async def handle_voice_events(websocket: Any) -> None:
    """Handle text and audio deltas emitted by the realtime model."""
    async for raw_message in websocket:
        event = json.loads(raw_message)
        event_type = event.get("type", "unknown")
        print(f"server event: {event_type}")

        if event_type == "response.audio.delta":
            audio_bytes = base64.b64decode(event.get("delta", ""))
            print(f"received {len(audio_bytes)} audio bytes for playback buffer")

        if event_type == "response.output_text.delta":
            print(event.get("delta", ""), end="", flush=True)

        if event_type in {"response.done", "response.failed"}:
            return


async def run_voice_architecture_demo(connect_to_api: bool = False) -> None:
    """
    Demonstrate the voice pipeline.

    The default mode prints the architecture without opening a socket, making it
    safe in Codespaces where no microphone or speaker device is usually present.
    Set connect_to_api=True from code when real audio devices are wired in.
    """
    print("\n=== REALTIME VOICE PIPELINE ===\n")
    print("1. Capture microphone audio as small PCM16 frames.")
    print("2. Append frames with input_audio_buffer.append events.")
    print("3. Let server VAD detect turns or manually commit buffers.")
    print("4. Receive response.audio.delta chunks from the model.")
    print("5. Buffer and play audio immediately while handling interruptions.")

    if not connect_to_api:
        print("\nCodespaces-safe mode: microphone and speaker placeholders only.")
        return

    import websockets

    headers = {"Authorization": f"Bearer {client.api_key}"}
    async with websockets.connect(REALTIME_URL, additional_headers=headers) as websocket:
        await send_voice_session_update(websocket)
        await asyncio.gather(
            stream_microphone_audio(websocket),
            handle_voice_events(websocket),
        )


async def main() -> None:
    """Application entry point with full traceback debugging."""
    try:
        await run_voice_architecture_demo()
    except Exception as error:
        print("\n=== FULL ERROR TRACEBACK ===\n")
        traceback.print_exc()
        print(f"\nRealtime voice example failed: {error}")


if __name__ == "__main__":
    asyncio.run(main())
