#!/bin/sh

echo "Starting entrypoint.sh..."
echo "Waiting for database db... Sleep 1 sec..."

while ! nc -z "db" 5432; do
  sleep 1
  echo "Sleep 1 sec.."
done

echo "database db started"
echo "Exiting entrypoint.sh..."

exec "$@"