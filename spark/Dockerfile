# Используем базовый образ с Apache Spark
FROM bitnami/spark:3.4.0

# Устанавливаем Java и Python зависимости
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install pyspark clickhouse-driver

# Копируем наш Python скрипт в контейнер
COPY app.py /app/

# Устанавливаем рабочую директорию
WORKDIR /app

# Указываем команду для запуска Spark-приложения
CMD ["spark-submit", "/app/app.py"]
