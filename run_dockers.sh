#!/bin/bash

# Stop any running containers of the same names
docker stop django_container
docker stop postgres_container
docker stop pgadmin_container

# Remove any existing containers of the same names
docker rm django_container
docker rm postgres_container
docker rm pgadmin_container

# Run Postgres container
docker run --name postgres_container -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres

# Wait for a bit to allow Postgres container to initialize
sleep 10

# Run Django container
docker run --name django_container --link postgres_container:postgres -p 8000:8000 -d django_image

# Run pgAdmin4 container
docker run --name pgadmin_container -p 8080:80 -e 'PGADMIN_DEFAULT_EMAIL=admin@admin.com' -e 'PGADMIN_DEFAULT_PASSWORD=admin' --link postgres_container:postgres -d dpage/pgadmin4
