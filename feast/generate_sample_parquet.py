import pandas as pd
from datetime import datetime

# Create example data for Feast
data = {
    "car_id": [1, 2, 3, 4, 5],
    "car_model": ["Civic", "Corolla", "Model 3", "Mustang", "X5"],
    "transmission_type": ["Automatic", "Manual", "Automatic", "Manual", "Automatic"],
    "engine_size": [1.8, 1.6, 0.0, 5.0, 3.0],
    "fuel_type": ["Petrol", "Petrol", "Electric", "Petrol", "Diesel"],
    "year": [2018, 2017, 2021, 2015, 2019],
    "brand": ["Honda", "Toyota", "Tesla", "Ford", "BMW"],
    "event_timestamp": [
        datetime(2023, 5, 1, 12, 0),
        datetime(2023, 5, 2, 12, 0),
        datetime(2023, 5, 3, 12, 0),
        datetime(2023, 5, 4, 12, 0),
        datetime(2023, 5, 5, 12, 0),
    ],
    "created": [
        datetime(2023, 5, 1, 12, 5),
        datetime(2023, 5, 2, 12, 5),
        datetime(2023, 5, 3, 12, 5),
        datetime(2023, 5, 4, 12, 5),
        datetime(2023, 5, 5, 12, 5),
    ],
}

df = pd.DataFrame(data)

# Save to Parquet (requires pyarrow)
df.to_parquet("used_car_features.parquet", index=False)

print("Parquet file created: used_car_features.parquet")
