import environ

from social_network.settings.base import *

env = environ.Env(
    DEBUG=(bool, False),
    SECURE_SSL_REDIRECT=(bool, True),
    CORS_ALLOWED_ORIGINS=(list, []),
)

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')

SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT')

DATABASES = {
    'default': env.db(),
}
