# Используем базовый образ с установленной Java
FROM openjdk:11-slim  # Легковесный образ с Java 11, необходимый для работы Apache Spark

# Устанавливаем Python и другие необходимые пакеты
RUN apt-get update && apt-get install -y --no-install-recommends \  # Обновляем список пакетов и устанавливаем минимальный набор
    python3 \  # Устанавливаем Python 3
    python3-pip \  # Устанавливаем менеджер пакетов pip
    build-essential \  # Устанавливаем инструменты сборки (необходимы для некоторых зависимостей)
    && rm -rf /var/lib/apt/lists/*  # Удаляем кэш apt, чтобы уменьшить размер образа

# Указываем рабочую директорию
WORKDIR /app  # Все дальнейшие команды будут выполняться из каталога /app

# Устанавливаем curl, загружаем ClickHouse JDBC-драйвер, удаляем временные файлы
RUN apt-get update && apt-get install -y curl && \  # Устанавливаем curl для загрузки драйвера
    curl -fL -o /app/clickhouse-jdbc-0.4.6-all.jar \  # Скачиваем ClickHouse JDBC-драйвер в рабочую директорию
    https://repo1.maven.org/maven2/com/clickhouse/clickhouse-jdbc/0.4.6/clickhouse-jdbc-0.4.6-all.jar && \  # Указываем URL драйвера
    apt-get remove -y curl && apt-get autoremove -y && \  # Удаляем curl и связанные с ним временные файлы
    rm -rf /var/lib/apt/lists/*  # Очищаем кэш apt, чтобы уменьшить размер образа

# Копируем файл приложения в контейнер
COPY app.py /app/  # Копируем локальный файл app.py в рабочую директорию контейнера

# Устанавливаем зависимости для Python
RUN pip3 install pyspark clickhouse-driver  # Устанавливаем библиотеки PySpark и ClickHouse Python драйвер

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1  # Указываем Python не буферизовать вывод (полезно для логирования)

# Запускаем приложение через spark-submit
CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0", "--jars", "/app/clickhouse-jdbc-0.4.6-all.jar", "/app/app.py"]  
# Используем spark-submit для запуска app.py
# --packages: подключаем библиотеку Kafka для Spark
# --jars: указываем путь к драйверу ClickHouse JDBC