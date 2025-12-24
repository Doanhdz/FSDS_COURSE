from datetime import datetime

import constants
import pandas as pd
import pytz
from feast import FeatureStore

# Note: see https://docs.feast.dev/getting-started/concepts/feature-retrieval for
# more details on how to retrieve for all entities in the offline store instead
entity_df = pd.DataFrame.from_dict(
    {
        # entity's join key -> entity values
        "vendorid": [0, 1, 2],
    }
)
entity_df["event_timestamp"] = datetime.now(pytz.utc)
entity_df["vendorid"] = entity_df["vendorid"].astype(str)

# Initialize the feature store
store = FeatureStore(repo_path=constants.REPO_PATH)

# Get training data from feature store
# we only want to get feature_6 for all device_ids
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "taxi:tpep_pickup_datetime",
        "taxi:tpep_dropoff_datetime",
        "taxi:passenger_count",  
        "taxi:trip_distance",
        "taxi:ratecodeid",
        "taxi:store_and_fwd_flag",
        "taxi:pulocationid",
        "taxi:dolocationid",
        "taxi:payment_type",
        "taxi:fare_amount",
        "taxi:extra",
        "taxi:mta_tax",
        "taxi:tip_amount",
        "taxi:tolls_amount",
        "taxi:improvement_surcharge",
        "taxi:total_amount",
        "taxi:congestion_surcharge",
        "taxi:airport_fee"
    ],
).to_df()

print("----- Feature schema -----\n")
print(training_df.info())

print()
print("----- Example features -----\n")
print(training_df.head())
