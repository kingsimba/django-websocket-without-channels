# Add websocket to Django without extra dependency

## Motivation

[Django Channels](https://channels.readthedocs.io/en/stable/) is very large.
It dependence on `cryptography` which depends on Rust compiler(https://cryptography.io/en/latest/faq/#why-does-cryptography-require-rust) ...

I found a simple solution from https://jaydenwindle.com/writing/django-websockets-zero-dependencies/

I improve it so the API is very similar with Django Channels.

```python
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

```
