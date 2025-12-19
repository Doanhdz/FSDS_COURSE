from pprint import pprint
import constants
from feast import FeatureStore

# Initialize the feature store
store = FeatureStore(repo_path=constants.REPO_PATH)
# Get serving data from feature store, we retrieve
# all features


feature_vector = store.get_online_features(
    features=[
        # "taxi:tpep_pickup_datetime",
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
    entity_rows=[
        {"vendorid": 3},
    ],
).to_dict()

pprint(feature_vector)
