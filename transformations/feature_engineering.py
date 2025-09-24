from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, countDistinct

spark = SparkSession.builder.appName("FeatureEngineering").getOrCreate()

df = spark.read.json("data/synthetic_events.json")

features = (
    df.groupBy("customer_id")
    .agg(
        max("timestamp").alias("last_activity"),
        avg("amount").alias("avg_spent"),
        countDistinct("event").alias("event_types")
    )
)

features.write.mode("overwrite").parquet("data/features/")
print("✅ Features saved to data/features/")
