import requests
import pandas as pd
from IPython.display import display
from botocore.exceptions import ClientError
import json


api_key = "8643b12cf0604bc870166748e54b534e"

url = f"https://api.themoviedb.org/3/discover/movie?api_key={'8643b12cf0604bc870166748e54b534e'}&include_adult=false&include_video=false&with_genres=16,35&language=en-US&release_date.gte=2013&release_date.lte=2023"

response = requests.get(url) 
data = response.json()
custos= []
numero_paginas = data['total_pages']
c=0
g=0

for pagina in range(1, numero_paginas+1):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={'8643b12cf0604bc870166748e54b534e'}&include_adult=false&include_video=false&with_genres=16,35&language=en-US&release_date.gte=2013&release_date.lte=2023&page={pagina}"
    response = requests.get(url) 
    data = response.json()    

    for movie in data['results']:
                        
        url = f"https://api.themoviedb.org/3/movie/{movie['id']}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NjQzYjEyY2YwNjA0YmM4NzAxNjY3NDhlNTRiNTM0ZSIsInN1YiI6IjY0NmQ1N2U3MzNhMzc2MDExZWM1YjA1MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lXkBkv2RQ-AKSnbthDpUlnkVMjAu5bXmA8iwh0lbH8Y"
        }
                
        response2 = requests.get(url, headers=headers)
        
        data2 = response2.json()                  

        df = {
            'imdb_id': data2['imdb_id'],
            'orcamento': data2['budget'],
            'receita': data2['revenue']
        }
        custos.append(df)
        c=c+1
        print(c)
        if c > 99:
            with open(f'custo{g}.json', 'w') as json_file:
                json.dump(custos, json_file)
                g=g+1
                c=0
                custos.clear()
        else:
            with open(f'custo{g}.json', 'w') as json_file:
                json.dump(custos, json_file)
                
                         
