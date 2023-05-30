import requests
import pandas as pd
from IPython.display import display
import json

api_key = "838b6bf7ad091a6b1ea4100e79e1377a"

url = f"https://api.themoviedb.org/3/discover/movie?api_key={'838b6bf7ad091a6b1ea4100e79e1377a'}&include_adult=false&include_video=false&with_genres=16,35&language=en-US&release_date.gte=2013&release_date.lte=2023"

response = requests.get(url) 
data = response.json()
directors = []
numero_paginas = data['total_pages']


for pagina in range(1, numero_paginas+1):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={'838b6bf7ad091a6b1ea4100e79e1377a'}&include_adult=false&include_video=false&with_genres=16,35&language=en-US&release_date.gte=2013&release_date.lte=2023&page={pagina}"
    response = requests.get(url) 
    data = response.json()    

    for movie in data['results']:
                        
        url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?api_key={'838b6bf7ad091a6b1ea4100e79e1377a'}"
                
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
    print(f"Pagina: {pagina}")                     
print("Acabei!")
with open("Diretores.json", "a+") as arquivo:     
    json.dump(directors, arquivo, indent=4)                                                
