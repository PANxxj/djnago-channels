from app.routing import websocket_urlpatterns
from channels.routing import ProtocolTypeRouter,URLRouter
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'routing_channels.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(websocket_urlpatterns)
})
