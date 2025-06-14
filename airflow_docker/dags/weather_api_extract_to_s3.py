import pandas as pd
import requests
from airflow.models import Variable
from dotenv import load_dotenv
import awswrangler as wr
from datetime import datetime
import boto3

load_dotenv()

Api_key = Variable.get('API_KEY')

latitude = 7.422313446017177
longtitude = 3.9573960812542888


def weather_api_extract():
    """
    Extracts current Ibadan weather data from the Weatherbit API and saves
    it to an S3 bucket in Parquet format.
    """
    lat_lon_apikey = f"lat={latitude}&lon={longtitude}&key={Api_key}"
    Base_url = f"https://api.weatherbit.io/v2.0/current?{lat_lon_apikey}"
    response = requests.get(Base_url)
    if response.status_code == 200:
        data = response.json()['data']
        df = pd.json_normalize(data)

        session = boto3.Session(
            aws_access_key_id=Variable.get('access_key'),
            aws_secret_access_key=Variable.get('secret_key'),
            region_name=Variable.get('region'))
        date_value = datetime.today().strftime('%Y-%m-%d')
        bucket_name = "botafli-weather-api"
        parquet_file = f"weather-api-{date_value}.parquet"
        path_s3 = f's3://{bucket_name}/{parquet_file}'
        wr.s3.to_parquet(
            df=df,
            path=path_s3,
            dataset=False,
            boto3_session=session)
        return data
    else:
        raise ValueError(f'this error code is :{response.status_code}')
