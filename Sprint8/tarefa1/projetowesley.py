import requests
import pandas as pd
from IPython.display import display
import json

api_key = "838b6bf7ad091a6b1ea4100e79e1377a"

#url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={'838b6bf7ad091a6b1ea4100e79e1377a'}&language=pt-BR"

url = f"https://api.themoviedb.org/3/discover/movie?api_key={'838b6bf7ad091a6b1ea4100e79e1377a'}&include_adult=false&include_video=false&with_genres=16"

response = requests.get(url)
data = response.json()
filmes = []

for movie in data['results']:
    df = {'Id':movie['id'],
    'Titulo': movie['title'],
    'Média de votos:': movie['vote_average']
    }
    filmes.append(df)
df = pd.DataFrame(filmes)
#display(df)

qtd = len(filmes)

for z in range(qtd):
    identifica = filmes[z]["Id"]  # valor id de cada filme na pagina
    url = f"https://api.themoviedb.org/3/movie/{identifica}/credits?api_key={'838b6bf7ad091a6b1ea4100e79e1377a'}"
   
    response = requests.get(url)
    dados2 = response.json()    
    directors = []  
    
    for credit in dados2['crew']:        
        if credit['job'] == 'Director':            
            for job, value_of_dict in credit.items():
                if job == 'name':
                    df = {'Diretor': value_of_dict,
                    'ID filme': filmes[z]["Id"]
                    }                                   
                    with open("df.json", "a+") as arquivo:     
                        json.dump(df, arquivo, indent=4)