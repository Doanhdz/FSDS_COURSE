import os
import random
from datetime import datetime
from time import sleep

from dotenv import load_dotenv
from postgresql_client import PostgresSQLClient

load_dotenv()

TABLE_NAME = "taxi"
NUM_ROWS = 100


def main():
    pc = PostgresSQLClient(
        database="k6",
        user="k6",
        password="k6",
    )

    # Get all columns from the diabetes table
    try:
        columns = pc.get_columns(table_name=TABLE_NAME)
        print(columns)
    except Exception as e:
        print(f"Failed to get schema for table with error: {e}")

    # Loop over all columns and create random values
    for _ in range(NUM_ROWS):
        vendorid = random.randint(0, 100)
        tpep_pickup_datetime = random.randint(0, 15)
        tpep_dropoff_datetime = random.randint(70, 200)
        passenger_count = random.randint(40, 120)
        trip_distance = random.randint(0, 60)
        ratecodeid = random.randint(0, 300)
        store_and_fwd_flag = round(random.uniform(18.0, 45.0), 1)
        pulocationid = round(random.uniform(0.05, 2.5), 3)
        dolocationid = random.randint(18, 80)
        payment_type = random.randint(18, 80)
        fare_amount  = random.randint(18, 80)
        extra = random.randint(18, 80)
        mta_tax  = random.randint(18, 80)
        tip_amount = random.randint(18, 80)
        tolls_amount = random.randint(18, 80)
        improvement_surcharge = random.randint(18, 80)
        total_amount = random.randint(18, 80)
        congestion_surcharge = random.randint(18, 80)
        airport_fee = random.randint(18, 80)
        query = f"""
            INSERT INTO {TABLE_NAME} (
                vendorid,
                tpep_pickup_datetime,
                tpep_dropoff_datetime,
                passenger_count,
                trip_distance,
                ratecodeid,
                store_and_fwd_flag,
                pulocationid,
                dolocationid,
                payment_type,
                fare_amount,
                extra,
                mta_tax,
                tip_amount,
                tolls_amount,
                improvement_surcharge,
                total_amount,
                congestion_surcharge,
                airport_fee
            )
            VALUES (
                {vendorid},
                {tpep_pickup_datetime},
                {tpep_dropoff_datetime},
                {passenger_count},
                {trip_distance},
                {ratecodeid},
                {store_and_fwd_flag},
                {pulocationid},
                {dolocationid},
                {payment_type},
                {fare_amount},
                {extra},
                {mta_tax},
                {tip_amount},
                {tolls_amount},
                {improvement_surcharge},
                {total_amount},
                {congestion_surcharge},
                {airport_fee}
            )
        """
        pc.execute_query(query)
        sleep(2)


if __name__ == "__main__":
    main()
