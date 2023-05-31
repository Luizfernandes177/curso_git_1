#exercicio 1

import random

numeros=[]
tam= len(numeros)

while tam < 250:    
    numero = random.randint(1,250)       
    if numero not in numeros: 
        numeros.append(numero)
        tam= len(numeros)     

numeros.reverse()
print(numeros)







