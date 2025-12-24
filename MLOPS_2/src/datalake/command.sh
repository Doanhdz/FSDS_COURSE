CREATE SCHEMA IF NOT EXISTS lakehouse.taxi
WITH (location = 's3://taxi-data/');

#Create a new table in the newly created schema
CREATE TABLE IF NOT EXISTS lakehouse.taxi.taxi (
    VendorID VARCHAR(50),
    tpep_pickup_datetime VARCHAR (50),
    tpep_dropoff_datetime VARCHAR (50),
    passenger_count DECIMAL,
    trip_distance DECIMAL,
    RatecodeID DECIMAL, 
    store_and_fwd_flag VARCHAR(50), 
    PULocationID VARCHAR(50),
    DOLocationID VARCHAR(50), 
    payment_type VARCHAR(50), 
    fare_amount DECIMAL, 
    extra DECIMAL, 
    mta_tax DECIMAL, 
    tip_amount DECIMAL, 
    tolls_amount DECIMAL, 
    improvement_surcharge VARCHAR(50),
    total_amount DECIMAL,
    congestion_surcharge DECIMAL, 
    Airport_fee DECIMAL
    ) WITH (
    location = 's3://taxi-data/taxi'
);