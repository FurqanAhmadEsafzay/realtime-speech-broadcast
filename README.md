# Real-Time Speech Stream Processor

## Overview

This project is a real-time speech processing system built with **Python 3** that:

* Continuously records audio from a microphone
* Converts speech to text in real time
* Broadcasts the transcribed text over a WebSocket server
* Allows a JavaScript client to receive live text
* Saves raw audio to disk without interruption

---

## Architecture

The application is composed of four main components running in parallel:

1. **Audio Recorder**
   Continuously captures microphone input and writes raw audio data to disk without blocking other tasks.

2. **Speech-to-Text Processor**
   Consumes audio chunks and performs real-time transcription using the Vosk offline speech recognition engine.

3. **WebSocket Broadcaster**
   Hosts a WebSocket server that broadcasts newly generated text segments to all connected clients.

4. **Client Applications**
   A minimal JavaScript client connects to the WebSocket server and displays live transcription output.

Each component is isolated into its own module, making the system easy to extend or replace.

---

## Concurrency Model

The system uses **asyncio** as the primary concurrency model:

* Audio capture runs continuously without blocking the event loop.
* Speech recognition processes audio asynchronously.
* The WebSocket server handles multiple concurrent client connections.

---

## Project Structure

```
.
├── app/
│   ├── audio_recorder.py      # Microphone audio capture
│   ├── speech_to_text.py     # Speech recognition logic (Vosk)
│   ├── broadcaster.py        # WebSocket server
│   ├── config.py             # Central configuration
│   ├── logger.py             # Logging configuration
│   └── main.py               # Application entry point
│
├── client/
│   └── index.html             # JavaScript WebSocket client
│
│── recording/                # the audio will be store here
|
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/FurqanAhmadEsafzay/realtime-speech-broadcast.git
cd realtime-speech-broadcast
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## Installing the Vosk Model

This project uses the **Vosk offline speech recognition engine**. You must manually download and configure a Vosk model.

### 1. Download the model

Download **vosk-model-small-en-us-0.15** from the official Vosk models repository and extract it:

```
vosk-model-small-en-us-0.15/
```

### 2. Place the model on your system

Place the extracted folder in your project root directory, for example:

```
/realtime-speech-broadcast/vosk-model-small-en-us-0.15
```

### 3. Configure the model path

Open `app/config.py` and set the model path to the location where you extracted the model:

```python
MODEL_PATH = os.getenv(
    "VOSK_MODEL_PATH",
    "vosk-model-small-en-us-0.15"
)

```

Ensure the path is correct and accessible at runtime.

---

## Running the Application

### Start the Python server

Run the application as a module from the project root:

```bash
python -m app.main
```

### Run the JavaScript client

Open the following file in a browser:

```
client/index.html
```

Live transcription will appear as speech is detected.

---

## Known Limitations

* Speech recognition accuracy depends on microphone quality and background noise.
* JavaScript client UI is intentionally minimal.
* Language support depends on the selected Vosk model.

---

## Future Improvements

* Improved WebSocket reconnection handling
* Audio buffering and batching for higher transcription accuracy
* Unit and integration tests
* Enhanced frontend UI
