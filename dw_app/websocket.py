from typing import Type


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
    consumer_class: Type[WebSocketConsumer]


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
