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
        import s3fs
        import pyarrow.dataset as ds
        import pyarrow.csv as pv
        import psycopg2
        import io

        # -------------------------
        # MinIO
        # -------------------------
        s3 = s3fs.S3FileSystem(
            key="minio_access_key",
            secret="minio_secret_key",
            client_kwargs={"endpoint_url": "http://minio:9000"},
        )

        dataset = ds.dataset(
            "taxi-data/taxi",
            filesystem=s3,
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

        # recreate table (optional)
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

            cur.copy_expert(
                """
                COPY taxi FROM STDIN WITH CSV HEADER
                """,
                buf,
            )

            conn.commit()

        cur.close()
        conn.close()

    transform_data()
