#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Function to wait for PostgreSQL to become available
wait_for_postgres() {
  echo "Waiting for PostgreSQL to become available..."
  while ! python -c "import psycopg2; psycopg2.connect(
      host='${DB_HOST}',
      port='${DB_PORT}',
      user='${DB_USER}',
      password='${DB_PASSWORD}',
      dbname='${DB_NAME}'
  )" 2>/dev/null; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 1
  done
  echo "PostgreSQL is up - continuing"
}

# Wait for DB
wait_for_postgres

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Create superuser only if DEBUG is True (Security Best Practice)
if [ "$DEBUG" = "True" ]; then
  if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "Creating superuser if it doesn't exist..."
    python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser(
        '${DJANGO_SUPERUSER_USERNAME}', 
        '${DJANGO_SUPERUSER_EMAIL}', 
        '${DJANGO_SUPERUSER_PASSWORD}'
    )
    print('Superuser created.')
else:
    print('Superuser already exists.')
"
  fi
fi

# Start the server
echo "Starting Django development server..."
exec "$@"