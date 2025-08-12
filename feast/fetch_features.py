from pprint import pprint
from feast import FeatureStore

# Connect to the Feast repo
store = FeatureStore(repo_path="used_cars/feature_repo")

# Fetch online features for the car price prediction example
feature_vector = store.get_online_features(
    features=[
        "car_features:car_model",
        "car_features:transmission_type",
        "car_features:engine_size",
        "car_features:fuel_type",
        "car_features:year",
        "car_features:brand",
    ],
    entity_rows=[
        {"car_id": 5},
    ],
).to_dict()

pprint(feature_vector)
