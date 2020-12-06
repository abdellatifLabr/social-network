import environ

from social_network.settings.base import *

env = environ.Env(
    SECURE_SSL_REDIRECT=(bool, True),
    CORS_ALLOWED_ORIGINS=(list, []),
)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

print('PROD SETTINGS', ALLOWED_HOSTS)

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')

SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT')

DATABASES = {
    'default': env.db(),
}
