import os

import django
from channels.routing import get_default_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from social_network.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')
django.setup()
application = ProtocolTypeRouter({
    'http': get_default_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
