#!/bin/sh

# Function to run Django development server or Gunicorn
run_server() {
    if [ "$DJANGO_ENV" = "development" ]; then
        python manage.py runserver 0.0.0.0:8000
    else
        gunicorn wrestling_sorted.wsgi:application --timeout=3000 --bind=0.0.0.0:8000
    fi
}

# Check if any arguments are passed
if [ $# -gt 0 ]; then
    # If arguments are passed, execute them
    exec "$@"
else
    # No arguments, proceed with initial setup and run server
    python manage.py wait_for_db
    python manage.py migrate
    python manage.py loaddata initial_data.json

    run_server
fi
