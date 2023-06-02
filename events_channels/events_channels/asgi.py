from app.routing import websocket_urlpatterns
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'events_channels.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(websocket_urlpatterns)
})
