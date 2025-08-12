from datetime import timedelta
from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
    Project,
)
from feast.types import String, Float32, Int64

# Define a project for the feature repo
project = Project(name="used_cars", description="Features for used car price prediction model")

# Define the entity for cars
car = Entity(name="car", join_keys=["car_id"], description="Unique identifier for a car")

# Define the source of features (replace with your actual data path)
car_features_source = FileSource(
    name="car_features_source",
    path="data/used_car_features.parquet",  # Change to your actual dataset location
    timestamp_field="event_timestamp",     # Ensure your dataset has this column
    created_timestamp_column="created",    # Optional: can remove if not present
)

# Define the FeatureView
car_features_fv = FeatureView(
    name="car_features",
    entities=[car],
    ttl=timedelta(days=365*5),
    schema=[
        Field(name="car_model", dtype=String),
        Field(name="transmission_type", dtype=String),
        Field(name="engine_size", dtype=Float32),
        Field(name="fuel_type", dtype=String),
        Field(name="year", dtype=Int64),
        Field(name="brand", dtype=String),
    ],
    online=True,
    source=car_features_source,
    tags={"project": "used_cars"},
)

# Define a FeatureService to group features for model consumption
car_price_prediction_fs = FeatureService(
    name="car_price_prediction_service",
    features=[car_features_fv],
)
