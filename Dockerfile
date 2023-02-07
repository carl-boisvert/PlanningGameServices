# Use an official Python runtime as the base image
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable
ENV FLASK_APP=app.py

# Run the command to start the Gunicorn server
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "wsgi:app"]