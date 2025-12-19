import os

from dotenv import load_dotenv
from postgresql_client import PostgresSQLClient

load_dotenv()


def main():
    pc = PostgresSQLClient(
        database="k6",
        user="k6",
        password="k6",
    )

    # Create devices table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS taxi (
        created TIMESTAMPTZ DEFAULT NOW(),
        vendorid VARCHAR(50),
        tpep_pickup_datetime VARCHAR(50),
        tpep_dropoff_datetime VARCHAR(50),
        passenger_count DECIMAL,
        trip_distance DECIMAL,
        ratecodeid DECIMAL,
        store_and_fwd_flag DECIMAL,
        pulocationid VARCHAR(50),
        dolocationid VARCHAR(50),
        payment_type VARCHAR(50),
        fare_amount DECIMAL,
        extra DECIMAL,
        mta_tax DECIMAL,
        tip_amount DECIMAL,
        tolls_amount DECIMAL,
        improvement_surcharge VARCHAR(50),
        total_amount DECIMAL,
        congestion_surcharge DECIMAL, 
        airport_fee DECIMAL
    );  
    """

    try:
        pc.execute_query(create_table_query)
    except Exception as e:
        print(f"Failed to create table with error: {e}")


if __name__ == "__main__":
    main()
