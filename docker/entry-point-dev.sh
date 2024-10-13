#!/bin/sh

APP_DIR=/app

if [ -z "$PORT" ]; then
  PORT=8000
fi

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:$PORT