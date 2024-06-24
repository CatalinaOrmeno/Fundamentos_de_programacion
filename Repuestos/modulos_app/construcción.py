def enumerar_lista(lista):
    '''
    Esta función sirve para enumerar una lista.\n
    ----PARAMS----\n
    lista = Una lista valida
    '''
    for ind, opc in enumerate(lista):
        print(f'{ind+1}. {opc}')

def solicitar_acción():
    '''
    Esta función solicita un tipo de respuesta en el contexto de acciones en un menú.\n
    ----RETURN----\n
    Devuelve la respuesta al ambiente global y hay que guardarla de la siguiente forma:\n
    [variable_x] = solicitar_acción()\n
    Se devuelve como string de forma determinada.
    '''
    respuesta = input('¿Que desea hacer?:\n')
    return respuesta

def limpiar_pantalla():
    '''
    Esta función sirve para limpiar la pantalla de la consola.
    '''
    import os
    os.system('cls')
