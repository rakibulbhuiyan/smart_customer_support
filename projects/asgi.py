from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import conversations.routing

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),

        "websocket": AuthMiddlewareStack(
            URLRouter(
                conversations.routing.websocket_urlpatterns
            )
        ),
    }
)