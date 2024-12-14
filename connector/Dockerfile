# Использование официального образа Python в качестве базового
FROM python:3.11-slim

# Установка рабочей директории
WORKDIR /app

# Установка системных зависимостей, необходимых для psycopg2
RUN apt-get update && apt-get install -y \
    gcc \  # Установка компилятора GCC
    libpq-dev \  # Установка библиотек для работы с PostgreSQL
    && rm -rf /var/lib/apt/lists/*  # Очистка кэша apt для уменьшения размера образа

# Копирование исходного кода приложения
COPY app.py /app

# Установка Python-зависимостей
RUN pip install --no-cache-dir psycopg2 kafka-python flask  # Установка библиотек psycopg2, Kafka и Flask

# Открытие порта Flask-приложения
EXPOSE 5000  # Экспонирование порта 5000 для внешнего доступа

# Указание команды по умолчанию
CMD ["python", "app.py"]  # Запуск Flask-приложения