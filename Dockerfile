# syntax=docker/dockerfile:1

# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application and dependencies
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run the application
CMD ["python", "main.py"]
