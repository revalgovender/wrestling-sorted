FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR .

# Install dependencies
COPY ./requirements.txt ./app/requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

# Copy the Django project into the container
COPY . .

ENTRYPOINT ["./entrypoint.sh"]