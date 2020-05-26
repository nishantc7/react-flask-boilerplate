#!/bin/sh

echo "Waiting for database"
while ! nc -z users-db 5432; do
    sleep 0.1
done

echo "PostgreSQL Started"

python manage.py run -h 0.0.0.0