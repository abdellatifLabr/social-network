release: python manage.py migrate
web: gunicorn social_network.asgi:application -w 4 -k uvicorn.workers.UvicornWorker --log-file -