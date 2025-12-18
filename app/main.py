import asyncio
import queue
from app.audio_recorder import AudioRecorder
from app.speech_to_text import SpeechToText
from app.broadcaster import Broadcaster
from app.logger import get_logger

logger = get_logger("Main")


async def main():
    audio_queue = queue.Queue()
    text_queue = queue.Queue()

    recorder = AudioRecorder(audio_queue)
    stt = SpeechToText(audio_queue, text_queue)
    broadcaster = Broadcaster()

    recorder.start()
    stt.start()

    async def forward_text():
        loop = asyncio.get_running_loop()
        while True:
            text = await loop.run_in_executor(None, text_queue.get)
            logger.info(f"Broadcasting text: {text}")
            await broadcaster.broadcast(text)

    await asyncio.gather(
        broadcaster.start(),
        forward_text()
    )


if __name__ == "__main__":
    asyncio.run(main())
