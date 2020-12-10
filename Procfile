release: python manage.py migrate
web: daphne social_network.asgi:application --port $PORT --bind 0.0.0.0 -v2 --proxy-headers
worker: python manage.py runworker channels --settings=social_network.settings -v2
