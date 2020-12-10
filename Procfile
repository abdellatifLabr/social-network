release: python manage.py migrate
web: daphne social_network.asgi:application --access-log - --port 8001 --bind 0.0.0.0
web: python manage.py runworker channels -v2