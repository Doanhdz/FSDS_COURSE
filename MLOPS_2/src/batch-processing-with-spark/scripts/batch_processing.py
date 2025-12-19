from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
import argparse


def main(args):
    # The entrypoint to access all functions of Spark
    spark = (
        SparkSession.builder.master("local[*]")
        .appName("Python Spark read parquet example")
        .getOrCreate()
    )

    # Read from a parquet file (transformation)
    # https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html
    df = spark.read.parquet(args.input)
    print(df.head())
    
    # Set the number of partitions with repartitions
    num_partitions = 4  # Replace with the desired number of partitions
    df = df.repartition(
        num_partitions
    )  # Default using hash-based partition, which can potentially be lead to skew problem!
  # Write to a single file result.parquet
    df.coalesce(1).write.mode("overwrite").parquet("datawarehouse/data/taxi")

    # Show data (action)
    df.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        default="datalake/data/yellow_tripdata_2024-01.parquet",
        help="Data file in parquet format.",
    )
    args = parser.parse_args()
    main(args)
