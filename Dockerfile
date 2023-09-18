# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Add the Django project folder into the container at /app
ADD ./BusMaintenanceDashboard /app

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set working directory to where manage.py is
WORKDIR /app

# Run manage.py when the container launches
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
