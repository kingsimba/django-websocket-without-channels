class WebSocketConsumer:
    def __init__(self, send) -> None:
        self.__send = send

    def dispose(self):
        pass

    async def send(self, text_data):
        return await self.__send({"type": "websocket.send", "text": text_data})

    async def accept(self):
        await self.__send({"type": "websocket.accept"})

    async def connect(self):
        pass

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None):
        pass


class WebSocketConsumerRegistry:
    consumer_class = None


async def websocket_application(_scope, receive, send):
    consumer = None

    while True:
        event = await receive()

        if event["type"] == "websocket.connect":
            consumer = WebSocketConsumerRegistry.consumer_class(send)
            await consumer.connect()

        if event["type"] == "websocket.disconnect":
            await consumer.disconnect(event["code"])
            consumer.dispose()
            consumer = None
            break

        if event["type"] == "websocket.receive":
            await consumer.receive(event["text"])


import json


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


WebSocketConsumerRegistry.consumer_class = MyWebSocketConsumer
