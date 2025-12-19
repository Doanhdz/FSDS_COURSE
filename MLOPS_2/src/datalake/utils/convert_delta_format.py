# import pandas as pd

# # Read Parquet file
# df = pd.read_parquet('/home/ndanh/Desktop/DuyAnh/MLOPs/FSDS/FSDS-Module-MLOPS-2/data/yellow_tripdata_2024-01.parquet')

# # Display the first few rows
# print(df.dtypes)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("ParquetToDelta") \
    .getOrCreate()
df = spark.read.parquet("/home/ndanh/Desktop/DuyAnh/MLOPs/FSDS/FSDS-Module-MLOPS-2/data/yellow_*.parquet")
df = df.withColumn("tpep_pickup_datetime", col("tpep_pickup_datetime").cast("timestamp"))
df = df.withColumn("tpep_dropoff_datetime", col("tpep_dropoff_datetime").cast("timestamp"))


df.write.format("delta") \
  .mode("overwrite") \
  .save("/home/ndanh/Desktop/DuyAnh/MLOPs/FSDS/FSDS-Module-MLOPS-2/data_delta")

