import boto3
import logging
from botocore.exceptions import ClientError
import os

client = boto3.client(
    service_name='s3',
    aws_access_key_id='AKIAXT3LP36KMMHXOYAX',
    aws_secret_access_key='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',
    region_name='us-east-1' 
)

s3 = boto3.resource('s3')

def create_bucket(wesley, region= 'us-east-1'):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=wesley)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=wesley,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

client.create_bucket(
    ACL='private',
    Bucket='data-lake-de-wesley',    
)

s3 = boto3.resource('s3')
open('/Users/Luiz Fernandes\Desktop/aws/Sprint7/ETL/RAW/Local/CSV/Movies/2022/movies.csv', 'rb')
client.upload_file('/Users/Luiz Fernandes\Desktop/aws/Sprint7/ETL/RAW/Local/CSV/Movies/2022/movies.csv', 'data-lake-de-wesley', '/RAW/Local/CSV/Movies/2022/movies.csv')

open('/Users/Luiz Fernandes\Desktop/aws/Sprint7/ETL/RAW/Local/CSV/Series/2022/series.csv', 'rb')
client.upload_file('/Users/Luiz Fernandes\Desktop/aws/Sprint7/ETL/RAW/Local/CSV/Series/2022/series.csv', 'data-lake-de-wesley', '/RAW/Local/CSV/Series/2022/series.csv')


###caminho = "C:\Users\Luiz Fernandes\Desktop\aws\Sprint7\ETL\RAW\Local\CSV\Movies\2022\movies.csv"
###bucket = "data-lake-de-wesley"
###arquivo = "movies.csv"
###s3 = boto3.client('s3')
###s3.upload_file(caminho, bucket, arquivo)

