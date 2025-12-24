from airflow.decorators import task
from airflow import DAG
from datetime import datetime


with DAG(
    dag_id="transform_data",
    start_date=datetime(2025, 12, 16),
    schedule=None,
    catchup=False,
) as dag:

    @task(task_id="minio_to_postgresql")
    def transform_data():
        import pyarrow.dataset as ds
        import pyarrow.fs as pafs
        import pyarrow.csv as pv
        import psycopg2
        import io

        # -------------------------
        # MinIO via pyarrow.fs (NO s3fs)
        # -------------------------
        fs = pafs.S3FileSystem(
            access_key="minio_access_key",
            secret_key="minio_secret_key",
            endpoint_override="http://minio:9000",
            scheme="http",
        )

        dataset = ds.dataset(
            "taxi-data/taxi",
            filesystem=fs,
            format="parquet",
        )

        # -------------------------
        # PostgreSQL
        # -------------------------
        conn = psycopg2.connect(
            host="offline-fs",
            port=5432,
            dbname="k6",
            user="k6",
            password="k6",
        )
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS taxi (
            created TIMESTAMPTZ DEFAULT NOW(),
            vendorid VARCHAR(50),
            tpep_pickup_datetime VARCHAR(50),
            tpep_dropoff_datetime VARCHAR(50),
            passenger_count DECIMAL,
            trip_distance DECIMAL,
            ratecodeid DECIMAL,
            store_and_fwd_flag VARCHAR(50),
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
        """)

        cur.execute("TRUNCATE TABLE taxi;")
        conn.commit()

        # -------------------------
        # Stream Parquet → COPY
        # -------------------------
        for fragment in dataset.get_fragments():
            table = fragment.to_table()
            buf = io.BytesIO()

            pv.write_csv(table, buf)
            buf.seek(0)

            columns = [field.name for field in table.schema]
        cols_sql = ", ".join(f'"{c.lower()}"' for c in columns)

        cur.copy_expert(
            f"""
            COPY taxi ({cols_sql})
            FROM STDIN
            WITH CSV HEADER
            """,
            buf,
        )

        conn.commit()

        cur.close()
        conn.close()

    transform_data()
