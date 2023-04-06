import hashlib


while True:
    texto = input("Digite algo:")
    lista = hashlib.sha1()
    lista.update(texto.encode('utf-8'))

    print(lista.hexdigest())


