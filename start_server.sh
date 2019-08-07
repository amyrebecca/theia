#!/bin/bash

while ! nc -z postgres 5432; do
  echo Waiting for Postgres
  sleep 3
done

echo Applying migrations
python manage.py migrate --noinput

if [ "$DJANGO_ENV" == "production" ]; then
  if [ ! -d "theia/static" ]; then
    echo Generating static files
    python manage.py collectstatic
  fi
  echo Starting production server
  exec gunicorn theia.wsgi -b 0:8080
else
  echo Starting development server
  exec python manage.py runserver 0:8080
fi
