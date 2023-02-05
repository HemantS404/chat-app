from django.urls import path
from .consumers import *

websocket_urlpatterns =[
    path('chats/<room_name>/', ChatConsumer.as_asgi())
]