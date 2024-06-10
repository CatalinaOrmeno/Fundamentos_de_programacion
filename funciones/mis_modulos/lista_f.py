def iterar(lista):
    '''
    Muestra por pantalla un iterable ordenado por su indice + 1
    ---Params---
    lista = debe ser un objeto iterable, sino fallara por completo.
    '''
    for ind, opt in enumerate(lista):
        print(f'{ind+1}. {opt}')