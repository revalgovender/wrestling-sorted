#!/bin/sh

python manage.py wait_for_db

python manage.py migrate

python manage.py loaddata initial_data.json

if [ "$DJANGO_ENV" = "development" ]; then
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn wrestling_sorted.wsgi:application --timeout=3000 --bind=0.0.0.0:8000
fi
