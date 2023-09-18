
# Bus Maintenance Dashboard

## Overview
This project is a Bus Maintenance Dashboard built using Django, integrated with AdminLTE for the frontend, and uses PostgreSQL for the database. It also includes pgAdmin4 for database management.

## Directory Structure
```
- BusMaintenanceDashboard/
  - BusMaintenanceDashboard/
  - MaintenanceApp/
  - custom_script/
  - static/
  - staticfiles/
  - templates/
  - manage.py
  - requirements.txt
  - Dockerfile
  - run_dockers.sh
```

## Prerequisites
- Docker

## How to Run

### Build Docker Images
Run the following command to build the Docker image for the Django app:
```bash
docker build -t rapid_bus_maintenance_app .
```

### Run Containers
Use the `run_dockers.sh` script to start both the Django and PostgreSQL containers.
```bash
./run_dockers.sh
```

### Access the App
Open your web browser and go to `http://localhost:8000` to access the Django app.

## Technologies Used
- Django
- AdminLTE
- PostgreSQL
- Docker
- pgAdmin4

## Author
Abu
