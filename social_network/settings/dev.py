from decouple import config

from social_network.settings.base import *

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

SECRET_KEY = 'n568u-4y-xj^*wppqg1+vwvubo=ms94z^4cz=o#9l1*i+-b)$y'

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
