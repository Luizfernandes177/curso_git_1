import requests
import pandas as pd
from IPython.display import display
import json
import boto3
import logging
from botocore.exceptions import ClientError


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

                         
