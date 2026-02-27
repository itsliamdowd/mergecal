FROM python:3.13-slim

WORKDIR /app

COPY requirements/ requirements/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements/production.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "echo '=== Starting migrations ===' && python manage.py migrate && echo '=== Migrations done ===' && echo '=== Starting gunicorn on port ${PORT:-8000} ===' && gunicorn --bind 0.0.0.0:${PORT:-8000} --timeout 120 --log-level debug --access-logfile - config.wsgi:application"]
