from airflow import DAG
from airflow.operators.python import PythonOperator
from weather_api_extract_to_s3 import weather_api_extract
from datetime import datetime

default_args = {
    'owner': 'Botafli',
    'retries': 2
}

dag = DAG(
    dag_id = "ibadan_weather_to_s3",
    description = "This is the dag for ibadan daily weather extraction to s3",
    start_date = datetime(2025,6,11),
    schedule_interval = "@daily", # runs daily at 8am 
    catchup= False,
    default_args = default_args
    )

weather_api_dump_to_s3 = PythonOperator(
    task_id = "weather_api_dump_to_s3",
    dag = dag,
    python_callable = weather_api_extract
    )

weather_api_dump_to_s3