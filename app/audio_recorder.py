import sounddevice as sd
import soundfile as sf
from app.logger import get_logger
from app.config import SAMPLE_RATE, CHANNELS, AUDIO_FILE

logger = get_logger("AudioRecorder")


class AudioRecorder:
    def __init__(self, audio_queue):
        self.audio_queue = audio_queue

        self.file = sf.SoundFile(
            AUDIO_FILE,
            mode="w",
            samplerate=SAMPLE_RATE,
            channels=CHANNELS
        )

        self.stream = None

    def _callback(self, indata, frames, time, status):
        if status:
            logger.warning(status)

        # Send audio to queue for later processing
        self.audio_queue.put(indata.copy())

        # Persist raw audio to disk
        self.file.write(indata)

    def start(self):
        logger.info("Starting microphone recording")

        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            callback=self._callback
        )

        self.stream.start()

    def stop(self):
        logger.info("Stopping microphone recording")

        if self.stream:
            self.stream.stop()
            self.stream.close()

        self.file.close()

