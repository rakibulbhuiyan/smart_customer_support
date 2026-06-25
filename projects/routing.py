from channels.routing import URLRouter
from conversations.routing import websocket_urlpatterns

application = URLRouter(
    websocket_urlpatterns
)