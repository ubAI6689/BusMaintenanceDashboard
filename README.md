
# Bus Maintenance Dashboard

## Overview
This project is a Bus Maintenance Dashboard built using Django, integrated with AdminLTE for the frontend, and uses PostgreSQL for the database. It also includes pgAdmin4 for database management.

## Directory Structure
```
- BusMaintenanceDashboard/
  - Dockerfile
  - docker-compose.yml
  - BusMaintenanceDashboard/
  - MaintenanceApp/
  - custom_script/
  - static/
  - staticfiles/
  - templates/
  - manage.py
  - requirements.txt
  
```

# Bus Maintenance Dashboard

## Introduction

This is a Django-based Bus Maintenance Dashboard. This README provides steps to set up and run the application using Docker Compose.

## Pre-requisites

- Docker installed
- Docker Compose installed

## Build & Run

1. **Clone the Repository**
   ```
   git clone https://github.com/ubAI6689/BusMaintenanceDashboard.git
   ```

2. **Navigate to Project Directory**
   ```
   cd BusMaintenanceDashboard
   ```

3. **Build the Docker Compose Setup**
   ```
   docker-compose build
   ```

4. **Run the Docker Compose Setup**
   ```
   docker-compose up
   ```

   This will start the Django app and the PostgreSQL database. The Django app will be accessible at `http://localhost:8000`.

## Stop

To stop the application and remove containers, networks, and volumes:

```
docker-compose down
```

## Troubleshooting

- **Port Conflicts**: If you encounter port conflicts, make sure no other services are running on the same ports. You can modify the `docker-compose.yml` to use different ports if needed.

- **Database Connection Issues**: Make sure that the PostgreSQL container has fully initialized before the Django app tries to connect to it. Check the logs for any issues.


## Technologies Used
- Django
- AdminLTE
- PostgreSQL
- Docker
- pgAdmin4

## Author
Abu
