import environ

env = environ.Env()

DEBUG = env('DEBUG')

if DEBUG:
    from social_network.settings.dev import *
else:
    from social_network.settings.prod import *
