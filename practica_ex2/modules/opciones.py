from random import randint

def poblar(lista:list):
    if len(lista[1]) == 1:
        for producto in enumerate(lista[0]):
            lista[1].append(randint(1,100))
    else:
        print('Los datos ya han sido cargados!')