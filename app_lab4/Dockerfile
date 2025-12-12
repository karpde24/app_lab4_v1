# Базовий образ
FROM python:3.11-slim

# Забираємо кеш і ставимо системні залежності
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Робоча директорія в контейнері
WORKDIR /app

# Копіюємо requirements окремо (для кешу)
COPY requirements.txt .

# Оновлюємо pip і ставимо залежності
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код
COPY . .

# Відкриваємо порт Flask
EXPOSE 5000

# ВАЖЛИВО: Flask має слухати 0.0.0.0
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Запуск
CMD ["python", "app.py"]
