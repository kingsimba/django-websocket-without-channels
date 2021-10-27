import json

from dw_app.websocket import WebSocketConsumer


class MyWebSocketConsumer(WebSocketConsumer):
    def __init__(self, send) -> None:
        super().__init__(send)

    def dispose(self):
        pass

    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        print("disconnect code = ", code)

    async def receive(self, text_data=None):
        if text_data == "ping":
            text = json.dumps({"name": "simba"})
            await self.send(text_data=text)
