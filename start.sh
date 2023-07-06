#!/bin/bash

# Migrate
echo "======================== MIGRATE"
python manage.py migrate

# Static
echo "======================== COLLECT STATICS"
python manage.py collectstatic --noinput

# Run
if [ -n "$DOCKER" ]; then
  DOCKER_ENV=$(echo "$ENV_VERSION" | tr '[:upper:]' '[:lower:]')
  if [ "$DOCKER_ENV" = "prod" ]; then
    echo "======================== LAUNCHING PRODUCTION [DOCKER]"
    gunicorn project.wsgi:application --timeout 300 --bind 0.0.0.0:8000 --reload --access-logfile '-' --error-logfile '-'

    # # # Gunicorn Speed Up
    # gunicorn project.wsgi:application --timeout 300 --workers ${GUNICORN_WORKERS} --threads ${GUNICORN_THREADS} --max-requests ${GUNICORN_MAX_REQUESTS} --bind 0.0.0.0:8000 --access-logfile '-' --error-logfile '-'
  else
    echo "======================== LAUNCHING DEV [DOCKER]"
    python manage.py runserver 0.0.0.0:8000
  fi
else
  echo "======================== LAUNCHING DEV [RUNSERVER]"
  python manage.py runserver 0.0.0.0:8000
fi

