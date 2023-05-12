from django.urls import path, re_path

import room.consumers
import videocall.consumers


websocket_urlpatterns = [
    path('ws/<str:room_name>/', room.consumers.ChatConsumer.as_asgi()),
    re_path(r'', videocall.consumers.ChatConsumer.as_asgi()),
]

