from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Инициализация SparkSession
spark = SparkSession.builder \
    .appName("Customer Purchase Analytics") \
    .getOrCreate()

# Загрузка данных из таблицы (или из источника данных)
df = spark.read.format("jdbc").options(
    url="jdbc:clickhouse://clickhouse:8123",
    dbtable="customers",  # Исходная таблица
    user="default",
    password="",
).load()

# Рассчитываем средний доход по возрасту
average_income_df = df.groupBy("age").agg({"income": "avg"})

# Переименовываем столбцы
average_income_df = average_income_df.withColumnRenamed("avg(income)", "avg_income")

# Сохраняем результаты в таблицу `customers_transformed`
average_income_df.write.format("jdbc").options(
    url="jdbc:clickhouse://clickhouse:8123",
    dbtable="customers_transformed",  # Результирующая таблица
    user="default",
    password="",
).mode("overwrite").save()

spark.stop()
