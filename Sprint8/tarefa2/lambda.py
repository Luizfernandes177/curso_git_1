import boto3
import logging
from botocore.exceptions import ClientError


client = boto3.client(
    service_name='s3',
    aws_access_key_id='AKIAXT3LP36KEUTFDOFO',
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

for n in range(32):
    open(f'/Users/Luiz Fernandes/Documents/github/Compass-Uol-Udemy/Sprint8/tarefa2/{n}.json', 'rb')
    client.upload_file(f'/Users/Luiz Fernandes/Documents/github/Compass-Uol-Udemy/Sprint8/tarefa2/{n}.json', 'data-lake-de-wesley', f'/RAW/TMDB/JSON/2023/05/30/{n}.json')


