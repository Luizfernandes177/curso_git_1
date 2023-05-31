#exercicio 2


animais = ['galo', 'raposa', 'urubu', 'coelho', 'vaca', 'gato', 'cachorro', 
           'tubarão', 'baleia', 'aguia','urso', 'elefante', 'girafa', 'morcego',
           'golfinho', 'camaleão', 'pombo', 'cavalo', 'porco', 'tatu']
animais.sort()
list(map(print, animais))

arquivo = open("lista_animais.csv", "a")
for n in animais:
    arquivo.write(f'{n}\n')
