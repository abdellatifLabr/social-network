release: python manage.py migrate
web: daphne social_network.asgi:application --port 8001 --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2