# Databricks notebook source
df = spark.table("samples.accuweather.forecast_daily_calendar_imperial")
df.show()

# COMMAND ----------

df_selected = df.select(
    "city_name",
    "country_code",
    "date",
    "temperature_avg",
    "temperature_max",
    "humidity_relative_avg",
    "precipitation_probability",
    "rain_probability"
)

# COMMAND ----------

df_clean = df_selected.fillna({
    "temperature_avg": 0,
    "humidity_relative_avg": 0,
    "precipitation_probability": 0
})

# COMMAND ----------

from pyspark.sql.functions import col

df_transformed = df_clean.withColumn(
    "is_hot_day", col("temperature_avg") > 85
).withColumn(
    "is_rain_expected", col("rain_probability") > 70
)

# COMMAND ----------

from pyspark.sql.functions import to_date

df_transformed = df_transformed.withColumn(
    "date", to_date("date")
)

# COMMAND ----------

df_transformed.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("weather_pipeline")

# COMMAND ----------

spark.sql("SELECT * FROM weather_pipeline").show()

# COMMAND ----------

spark.sql("""
SELECT city_name, AVG(temperature_avg) AS avg_temp
FROM weather_pipeline
GROUP BY city_name
""").show()

# COMMAND ----------

spark.sql("""
SELECT city_name, COUNT(*) AS hot_days
FROM weather_pipeline
WHERE is_hot_day = true
GROUP BY city_name
""").show()

# COMMAND ----------

# MAGIC %sql
# MAGIC describe formatted
# MAGIC samples.accuweather.forecast_daily_calendar_imperial