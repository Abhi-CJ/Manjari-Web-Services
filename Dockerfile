# ---- Build Stage ----
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---- Production Stage ----
FROM python:3.12-slim

# Create a non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app
ENV PYTHONPATH=/app/backend/src:/app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy project files
COPY . .

# Collect static files
RUN cd backend && python manage.py collectstatic --noinput 2>/dev/null || true

# Set ownership
RUN chown -R appuser:appuser /app

USER appuser

# Expose port
EXPOSE 8000

# Run Gunicorn
CMD ["sh", "-c", "python backend/manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120"]
