FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Command to run on container start
CMD python manage.py wait_for_db \
&& python manage.py migrate \
&& python manage.py loaddata initial_data.json \
&& gunicorn wrestling_sorted.wsgi:application -b 0.0.0.0:8000