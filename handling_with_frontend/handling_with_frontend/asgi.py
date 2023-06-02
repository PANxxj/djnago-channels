from channels.routing import ProtocolTypeRouter,URLRouter
from app.routing import websocket_urlpatterns
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'handling_with_frontend.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(websocket_urlpatterns)
})
