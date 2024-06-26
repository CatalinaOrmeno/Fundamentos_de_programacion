def enumerar_lista(lista: list):
    for ind, opc in enumerate(lista):
        print(f'{ind+1}. {opc}')

def solicitar_acc():
    resp = input('¿Que deseas hacer?:\n')
    return resp

