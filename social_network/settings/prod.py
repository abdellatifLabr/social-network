import environ

from social_network.settings.base import *

env = environ.Env(
    SECURE_SSL_REDIRECT=(bool, True),
    CORS_ALLOWED_ORIGINS=(list, []),
)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')

SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT')

DATABASES = {
    'default': env.db(),
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = env.bool('AWS_S3_FILE_OVERWRITE')
AWS_DEFAULT_ACL = None
