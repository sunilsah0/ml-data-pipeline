from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {"owner": "airflow", "start_date": datetime(2023, 1, 1)}

with DAG("churn_pipeline", default_args=default_args, schedule_interval="@daily", catchup=False) as dag:

    ingest = BashOperator(
        task_id="batch_ingest",
        bash_command="python /usr/local/airflow/ingestion/batch_ingest.py"
    )

    transform = BashOperator(
        task_id="feature_engineering",
        bash_command="python /usr/local/airflow/transformations/feature_engineering.py"
    )

    quality = BashOperator(
        task_id="data_quality",
        bash_command="python /usr/local/airflow/quality_checks/validate.py"
    )

    ingest >> transform >> quality
