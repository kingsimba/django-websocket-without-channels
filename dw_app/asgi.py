"""
ASGI config for dw_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from dw_app.my_consumer import MyWebSocketConsumer
from dw_app.websocket import WebSocketConsumerRegistry, websocket_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dw_app.settings")

django_application = get_asgi_application()
WebSocketConsumerRegistry.consumer_class = MyWebSocketConsumer


async def application(scope, receive, send):
    if scope["type"] == "http":
        # Let Django handle HTTP requests
        await django_application(scope, receive, send)
    elif scope["type"] == "websocket":
        # We'll handle Websocket connections here
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
