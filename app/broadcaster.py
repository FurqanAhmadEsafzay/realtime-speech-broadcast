import asyncio
import websockets
from app.logger import get_logger
from app.config import WS_HOST, WS_PORT

logger = get_logger("Broadcaster")


class Broadcaster:
    def __init__(self):
        self.clients = set()

    async def handler(self, websocket):
        logger.info("Client connected")
        self.clients.add(websocket)

        try:
            async for _ in websocket:
                pass
        finally:
            self.clients.remove(websocket)
            logger.info("Client disconnected")

    async def broadcast(self, message: str):
        if not self.clients:
            return

        await asyncio.gather(
            *(client.send(message) for client in self.clients),
            return_exceptions=True
        )

    async def start(self):
        logger.info(f"WebSocket server listening on {WS_HOST}:{WS_PORT}")

        async with websockets.serve(self.handler, WS_HOST, WS_PORT):
            await asyncio.Future()  # run forever
