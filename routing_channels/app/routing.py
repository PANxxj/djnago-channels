from django.urls import path
from app.consumers import *

websocket_urlpatterns=[
    path('ws/sc/',MySyncconsumer.as_asgi()),
    path('ws/ac/',MyAsyncconsumer.as_asgi()),
]