release: python manage.py migrate
web: daphne -e ssl:443:privateKey=key.pem:certKey=crt.pem social_network.asgi:application --port $PORT --bind 0.0.0.0 -v2 --proxy-headers --access-log -
worker: python manage.py runworker channels --settings=social_network.settings -v2
