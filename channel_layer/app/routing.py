from django.urls import path
from .consumers import *

websocket_urlpatterns=[
    path('ws/sc',MySyncConsumer.as_asgi()),
    # path('ws/ac',MyAsyncConsumer.as_asgi()),
]