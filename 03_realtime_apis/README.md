# Realtime APIs

Author: Chaitanya Dasadiya
GitHub: https://github.com/cdasadiya

Production-focused examples for building low-latency OpenAI applications with WebSockets, streaming text, realtime voice, live transcription, interrupt handling, and performance optimization.

---

## What Realtime APIs Enable

Realtime AI systems reduce the delay between user input and model output. They are useful for:

- Voice assistants that speak naturally while users talk.
- Live captioning and transcription systems.
- Customer support copilots that stream partial answers.
- Telephony, contact center, and meeting intelligence workflows.
- Low-latency product experiences where waiting for a full response is too slow.

The examples in this folder are designed to run in GitHub Codespaces and follow the shared repository pattern:

- Add the repository root to `sys.path` for portable imports.
- Use `utils/openai_client.py` for centralized OpenAI client configuration.
- Avoid hardcoded secrets and rely on environment variables.
- Include async-ready structure, robust exception handling, and traceback debugging.

---

## Files

```text
03_realtime_apis/
├── websocket_connections.py
├── live_streaming.py
├── realtime_voice.py
├── realtime_transcription.py
├── interrupt_handling.py
├── low_latency_systems.py
└── README.md
```

| File | Focus |
| --- | --- |
| `websocket_connections.py` | Realtime WebSocket setup, lifecycle events, reconnects, and event logging. |
| `live_streaming.py` | Token-by-token streaming with progressive rendering and latency metrics. |
| `realtime_voice.py` | Voice assistant architecture with microphone and speaker pipeline placeholders. |
| `realtime_transcription.py` | Realtime speech-to-text workflow with incremental transcript event handling. |
| `interrupt_handling.py` | Cancelling active streams, keyboard interruption, and cleanup patterns. |
| `low_latency_systems.py` | Connection reuse, async concurrency, streaming optimization, token control, batching, and timing metrics. |

---

## Installation

Install dependencies from the repository root:

```bash
pip install -r requirements.txt
```

Set your OpenAI API key securely:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

For GitHub Codespaces, prefer repository or account-level Codespaces secrets instead of storing keys in source files.

Optional platform scoping:

```bash
export OPENAI_ORG_ID="org_optional"
export OPENAI_PROJECT_ID="project_optional"
```

---

## Execution Examples

Run from the repository root:

```bash
python 03_realtime_apis/websocket_connections.py
python 03_realtime_apis/live_streaming.py
python 03_realtime_apis/realtime_voice.py
python 03_realtime_apis/realtime_transcription.py
python 03_realtime_apis/interrupt_handling.py
python 03_realtime_apis/low_latency_systems.py
```

Or from inside the folder:

```bash
cd 03_realtime_apis
python websocket_connections.py
python live_streaming.py
python realtime_voice.py
python realtime_transcription.py
python interrupt_handling.py
python low_latency_systems.py
```

`realtime_voice.py` and `realtime_transcription.py` default to Codespaces-safe architecture demonstrations because Codespaces usually has no microphone or speaker device attached. Their functions include placeholders that can be connected to PyAudio, `sounddevice`, WebRTC media streams, SIP audio, or browser media capture in a production app.

---

## Architecture: WebSocket Realtime Session

```text
+---------------------+       JSON events        +--------------------------+
| Python application  | <----------------------> | OpenAI Realtime API      |
|                     |                          |                          |
| session.update      | -----------------------> | Configure instructions   |
| conversation item   | -----------------------> | Add user input           |
| response.create     | -----------------------> | Start model response     |
| event loop          | <----------------------- | Stream deltas + lifecycle|
+---------------------+                          +--------------------------+
```

Production notes:

- Keep WebSocket connections on trusted backend servers when using standard API keys.
- Use retry with exponential backoff for transient network failures.
- Log event types and IDs, but never log secrets or sensitive user data.
- Keep audio and text buffers bounded so slow consumers do not exhaust memory.

---

## Architecture: Streaming Text

```text
User request
    |
    v
OpenAI Responses API stream=True
    |
    +--> response.output_text.delta --> render immediately
    +--> response.completed ---------> finalize UI and metrics
    +--> response.failed ------------> show fallback/error state
```

Streaming improves perceived latency because users see useful output before the full answer is complete. Production systems should track:

- Time to first delta.
- Total stream duration.
- Chunks received.
- Error and cancellation rates.
- User interruption frequency.

---

## Architecture: Voice AI Pipeline

```text
Microphone / media stream
    |
    v
Small PCM audio frames
    |
    v
input_audio_buffer.append events
    |
    v
Realtime model + turn detection
    |
    +--> response.audio.delta -----> playback buffer -----> speaker
    +--> text/transcript events ---> captions/logging -----> UI
```

Production voice systems need careful buffering:

- Smaller chunks reduce latency but can increase overhead.
- Larger chunks improve throughput but can feel delayed.
- Jitter buffers smooth playback when networks fluctuate.
- Interrupt handling should stop playback and cancel model generation quickly.

---

## Architecture: Realtime Transcription

```text
Audio source
    |
    v
Base64 encoded audio chunks
    |
    v
input_audio_buffer.append
    |
    v
Realtime transcription session
    |
    +--> conversation.item.input_audio_transcription.delta
    +--> conversation.item.input_audio_transcription.completed
```

Use incremental transcript deltas for live captions, then replace or reconcile them with completed transcript events. Store transcript state by `item_id` so multiple speech turns can be ordered and updated correctly.

---

## Low-Latency Engineering Notes

### Connection Reuse

Create OpenAI clients once and reuse them. This repository exposes both `client` and `async_client` from `utils/openai_client.py`, allowing HTTP connection pooling and consistent configuration.

### Async Concurrency

Use `asyncio` for independent requests, live streams, audio input, audio output, and cancellation coordination. Keep CPU-heavy work out of the event loop or move it to worker threads/processes.

### Retry Systems

Retries should be targeted and bounded:

- Retry transient network failures.
- Use exponential backoff with a maximum delay.
- Avoid blindly retrying validation or authentication errors.
- Preserve idempotency when replaying user events.

### Streaming Architectures

Stream deltas to the UI as they arrive. For robust UX:

- Render partial text incrementally.
- Keep a finalization path for completion events.
- Add a cancellation path for interrupts.
- Track latency and stream health metrics.

### Token Optimization

Latency is strongly affected by generated token count. Use concise system instructions, explicit output limits, and `max_output_tokens` where appropriate.

### Realtime Buffering

Realtime audio systems usually need multiple buffers:

- Input capture buffer.
- Network send queue.
- Model output receive buffer.
- Playback jitter buffer.
- Transcript aggregation buffer.

Bound every buffer and define overflow behavior.

---

## Future Roadmap

- Add browser WebRTC examples with ephemeral client secrets.
- Add real microphone capture using `sounddevice` or PyAudio.
- Add audio playback examples with jitter buffering.
- Add SIP/telephony integration notes.
- Add observability examples with structured logs and metrics.
- Add load testing scripts for concurrent realtime sessions.
- Add WebSocket integration tests with mocked realtime server events.
