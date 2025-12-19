from datetime import timedelta

from data_sources import taxi_batch_source
from entities import taxi
from feast import FeatureView, Field
from feast.types import Float32, Int32, String
# from feast.stream_feature_view import stream_feature_view
# from pyspark.sql import DataFrame

taxi_view = FeatureView(
    name="taxi",
    description="taxi features",
    entities=[taxi],
    ttl=timedelta(days=36500),
    schema=[
        Field(name="vendorid", dtype=String),
        # Field(name="tpep_pickup_datetime", dtype=Int32),
        Field(name="tpep_dropoff_datetime", dtype=Int32),
        Field(name="passenger_count", dtype=Int32),
        Field(name="trip_distance", dtype=Int32),
        Field(name="ratecodeid", dtype=Float32),
        Field(name="store_and_fwd_flag", dtype=Float32),
        Field(name="pulocationid", dtype=Int32),
        Field(name="dolocationid", dtype=Int32),
        Field(name="payment_type", dtype=Int32),
        Field(name="fare_amount", dtype=Int32),
        Field(name="extra", dtype=Int32),
        Field(name="mta_tax", dtype=Int32),
        Field(name="tip_amount", dtype=Int32),
        Field(name="tolls_amount", dtype=Int32),
        Field(name="improvement_surcharge", dtype=Int32),
        Field(name="total_amount", dtype=Int32),
        Field(name="congestion_surcharge", dtype=Int32),
        Field(name="airport_fee", dtype=Int32),
    ],
    online=True,
    source=taxi_batch_source,
)


# @stream_feature_view(
#     entities=[device],
#     ttl=timedelta(days=36500),
#     mode="spark",
#     schema=[
#         Field(name="feature_5", dtype=Float32),
#         Field(name="feature_3", dtype=Float32),
#         Field(name="feature_1", dtype=Float32),
#         Field(name="feature_8", dtype=Float32),
#         Field(name="feature_6", dtype=Float32),
#         Field(name="feature_0", dtype=Float32),
#         Field(name="feature_4", dtype=Float32),
#     ],
#     timestamp_field="created",
#     online=True,
#     source=device_stats_stream_source,
# )
# def device_stats_stream(df: DataFrame):
#     from pyspark.sql.functions import col

#     return (
#         df.withColumn("new_feature_5", col("feature_5") + 1.0)
#         .withColumn("new_feature_3", col("feature_3") + 1.0)
#         .withColumn("new_feature_1", col("feature_1") + 1.0)
#         .withColumn("new_feature_8", col("feature_8") + 1.0)
#         .withColumn("new_feature_6", col("feature_6") + 1.0)
#         .withColumn("new_feature_0", col("feature_0") + 1.0)
#         .withColumn("new_feature_4", col("feature_4") + 1.0)
#         .drop(
#             "feature_5",
#             "feature_3",
#             "feature_1",
#             "feature_8",
#             "feature_6",
#             "feature_0",
#             "feature_4",
#         )
#         .withColumnRenamed("new_feature_5", "feature_5")
#         .withColumnRenamed("new_feature_3", "feature_3")
#         .withColumnRenamed("new_feature_1", "feature_1")
#         .withColumnRenamed("new_feature_8", "feature_8")
#         .withColumnRenamed("new_feature_6", "feature_6")
#         .withColumnRenamed("new_feature_0", "feature_0")
#         .withColumnRenamed("new_feature_4", "feature_4")
#     )
