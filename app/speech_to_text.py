import json
import threading
from vosk import Model, KaldiRecognizer
from app.logger import get_logger
from app.config import SAMPLE_RATE, MODEL_PATH

logger = get_logger("SpeechToText")


class SpeechToText(threading.Thread):
    def __init__(self, audio_queue, text_queue):
        super().__init__(daemon=True)

        self.audio_queue = audio_queue
        self.text_queue = text_queue

        logger.info("Loading Vosk model...")
        self.model = Model(MODEL_PATH)
        self.recognizer = KaldiRecognizer(self.model, SAMPLE_RATE)

    def run(self):
        logger.info("Speech-to-text thread started")

        while True:
            audio_chunk = self.audio_queue.get()

            # Convert float32 audio to int16 PCM
            pcm16 = (audio_chunk * 32767).astype("int16")

            if self.recognizer.AcceptWaveform(pcm16.tobytes()):
                result = json.loads(self.recognizer.Result())
                text = result.get("text", "").strip()

                if text:
                    logger.info(f"Recognized: {text}")
                    self.text_queue.put(text)
