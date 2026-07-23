# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Copy Requirements
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files
COPY . .

# Expose Port
EXPOSE 5000

# Start Application
CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]
