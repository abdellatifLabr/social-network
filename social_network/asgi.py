import os

from channels.routing import get_default_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

application = get_default_application()
