from channels.routing import ProtocolTypeRouter
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'(?P<jail_name>\w+)/websocket', consumers.VNCConsumer)
]
