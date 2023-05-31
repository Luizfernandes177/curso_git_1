import requests
import pandas as pd
import json
import boto3
import logging
from botocore.exceptions import ClientError
from io import BytesIO

def lambda_handler(event, context):
    
    api_key = "8643b12cf0604bc870166748e54b534e"

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={'8643b12cf0604bc870166748e54b534e'}&include_adult=false&include_video=false&with_genres=16,35&language=en-US&release_date.gte=2013&release_date.lte=2023"
    
    response = requests.get(url) 
    data = response.json()
    directors = []
    numero_paginas = data['total_pages']
    
    
    for pagina in range(1, numero_paginas+1):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={'8643b12cf0604bc870166748e54b534e'}&include_adult=false&include_video=false&with_genres=16,35&language=en-US&release_date.gte=2013&release_date.lte=2023&page={pagina}"
        response = requests.get(url) 
        data = response.json()    
    
        for movie in data['results']:
                            
            url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?api_key={'8643b12cf0604bc870166748e54b534e'}"
                    
            response2 = requests.get(url)
            data2 = response2.json()                
                        
            for credit in data2['crew']:        
                if credit['job'] == 'Director':            
                    for job, value_of_dict in credit.items():
                        if job == 'name':
                            df = {'Diretor': value_of_dict,
                            'ID filme': movie['id']
                            }
                            directors.append(df)
    
                             
    
    
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
    
    bloco = 0
    contador = 0
    grupo = []                            
    tam_dir = len(directors)                            
    for n in range(tam_dir):    
        if contador < 100:
            grupo.append(directors[n])
            contador = contador+1
            novo_dataframe = pd.DataFrame(grupo)
            json_data = novo_dataframe.to_json(orient='records')
            objeto_final = BytesIO(json_data.encode())
            client.put_object(Bucket='data-lake-de-wesley', Key=f'/RAW/TMDB/JSON/2023/05/30/{bloco}.json', Body=objeto_final)
        else:
            grupo.clear()
            grupo.append(directors[n])
            bloco = bloco+1
            novo_dataframe = pd.DataFrame(grupo)
            json_data = novo_dataframe.to_json(orient='records')
            objeto_final = BytesIO(json_data.encode())
            client.put_object(Bucket='data-lake-de-wesley', Key=f'/RAW/TMDB/JSON/2023/05/30/{bloco}.json', Body=objeto_final)             
            contador = 1        
                             
    
    return {
        'statusCode': 200,
        'body': json.dumps('Finish')
    }
