import os

# Audio configuration
SAMPLE_RATE = int(os.getenv("SAMPLE_RATE", 16000))
CHANNELS = 1
AUDIO_FILE = os.getenv("AUDIO_FILE", "recordings/audio.wav")

# Speech-to-text model path
MODEL_PATH = os.getenv(
    "VOSK_MODEL_PATH",
    "vosk-model-small-en-us-0.15"
)

# MODEL_PATH = "vosk-model-small-en-us-0.15"
# MODEL_PATH = os.getenv("VOSK_MODEL_PATH", "model")

# WebSocket server configuration
WS_HOST = os.getenv("WS_HOST", "0.0.0.0")
WS_PORT = int(os.getenv("WS_PORT", 8765))
