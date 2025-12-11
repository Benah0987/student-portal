echo "Starting startup script: running migrations and collectstatic if needed..."
echo "Starting Gunicorn..."
#!/usr/bin/env bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."

# Default to 1 worker if WEB_CONCURRENCY is not set
: ${WEB_CONCURRENCY:=1}

exec gunicorn Home.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers=${WEB_CONCURRENCY}
