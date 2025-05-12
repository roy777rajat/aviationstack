
import boto3
import json
from botocore.exceptions import ClientError
import os
from datetime import datetime
import webbrowser
import tempfile
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY_AVIATION")
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

def get_secret():

    secret_name = "dev/python/api"
    region_name = "eu-west-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        print("Fetching secret...")
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

    except Exception as e:
        print(f"Error fetching secret: {e}")
        raise e
    except ClientError as e:
       
        print(f"Error fetching secret: {e}")
        raise e

    secret = get_secret_value_response['SecretString']
    #secret to dict preetify
    secret = json.loads(secret)
   
    print(secret)
    

if __name__ == "__main__":
    get_secret()
   