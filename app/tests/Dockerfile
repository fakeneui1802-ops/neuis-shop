# Verwende ein leichtes Python-Image
FROM python:3.11-slim

# Arbeitsverzeichnis
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Code kopieren
COPY . .

# Uvicorn mit Gunicorn ersetzen ist optional; hier einfacher uvicorn via "uvicorn" in port 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
