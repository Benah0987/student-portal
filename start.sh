#!/usr/bin/env bash
set -e

echo "Starting startup script: running migrations and collectstatic if needed..."

# Activate virtualenv if present (Render uses a venv automatically when building)
# Run migrations and collectstatic (idempotent)
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."

# Use WEB_CONCURRENCY if set, otherwise default to 1
: ${WEB_CONCURRENCY:=1}

exec gunicorn Home.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers=${WEB_CONCURRENCY}
