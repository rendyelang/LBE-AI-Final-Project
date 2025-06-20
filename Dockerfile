# Gunakan image Python 3.9
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt dulu untuk caching
COPY requirements.txt .

# Install dependensi (termasuk gunicorn untuk production)
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh project (kecuali yang di .dockerignore)
COPY . .

# Expose port Flask (sesuaikan dengan port di web1.py)
EXPOSE 5000

# Perintah untuk menjalankan Flask (development)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# Opsi Production (gunakan gunicorn):
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "web1:app"]