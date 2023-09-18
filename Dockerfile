# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Navigate to the right directory where manage.py is located
WORKDIR /app/BusMaintenanceDashboard

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r ../requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["gunicorn", "BusMaintenanceDashboard.wsgi:application", "--bind", "0.0.0.0:8000"]
