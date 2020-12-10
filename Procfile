release: python manage.py migrate
web: gunicorn social_network.wsgi:application -w 4 -k uvicorn.workers.UvicornWorker --log-file -