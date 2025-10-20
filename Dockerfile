# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install gunicorn

# Copy project files
COPY . .

# Ensure static folder exists
RUN mkdir -p static

# Collect static files
RUN python manage.py collectstatic --noinput || echo "Skipping collectstatic for now"

# Expose port 8000
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Home.wsgi:application"]
