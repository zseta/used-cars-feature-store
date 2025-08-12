# Feast + ScyllaDB setup guide

This guide walks you through setting up a Feast feature store with ScyllaDB.

Create a Python virtual environment
```
virtualenv env
source env/bin/activate
```


Install Python Dependencies
```
pip install -r requirements.txt
```


Run ScyllaDB in Docker
```
docker run --name node1 -d scylladb/scylla-enterprise:2024.2 \
  --overprovisioned 1 \
  --smp 1
```


Create keyspace
```
docker exec -it node1 cqlsh
```

```
CREATE KEYSPACE IF NOT EXISTS feast WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'replication_factor': 1
};
```

Edit Feast repository: `used_cars/feature_repo/example_repo.py`

Edit Feast configuration file: `used_cars/feature_repo/feature_store.yaml`

Apply Feast configuration
```
cd used_cars/feature_repo/
feast apply
```


Verify schema in ScyllaDB
```
docker exec -it node1 cqlsh
desc schema;
select * from feast.used_cars_car_features;
```

Exit cqlsh
```
exit
```

Insert online features
```
CURRENT_TIME=$(date -u +"%Y-%m-%dT%H:%M:%S")
feast materialize-incremental $CURRENT_TIME

See inserted rows:
```
docker exec -it node1 cqlsh
select * from feast.used_cars_car_features;
```

Fetch online features
```
cd ../../
python fetch_features.py
```
