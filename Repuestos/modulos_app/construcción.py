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

def verificar_ingreso(pronombre,dato):
    while True:
        valor = input(f'Ingrese {pronombre} {dato} del repuesto:\n')
        resp = input(f'{dato.upper()}: {valor}\n¿Es correcto?(s/n):\n').lower().replace(' ', '')
        if resp in ['s','si']:
            limpiar_pantalla()
            return valor
        elif resp in ['n','no']:
            limpiar_pantalla()
            print('Okey, intente de nuevo')
        else:
            limpiar_pantalla()
            print('Error: respuesta invalida\nIntente con (s, si , n, no)\n')

def verificar_tipo():
    while True:
        tipo = input(f'Ingrese el tipo de repuesto (AUTOMOTRIZ / MOTOCICLETA):\n').upper().replace(' ', '')
        if tipo == 'AUTOMOTRIZ' or tipo == 'MOTOCICLETA':
            limpiar_pantalla()
            resp = input(f'TIPO: {tipo}\n¿Es correcto?(s/n):\n').lower().replace(' ', '')
            if resp in ['s','si']:
                limpiar_pantalla()
                return tipo
            elif resp in ['n','no']:
                limpiar_pantalla()
                print('Okey, intente de nuevo')
            else:
                limpiar_pantalla()
                print('Error: respuesta invalida\nIntente con (s, si , n, no)\n')
        else:
            limpiar_pantalla()
            print('Error: respuesta invalida.\nIntente de nuevo.\n')

def verificar_num(dato):
    while True:
        try:
            valor = int(input(f'Ingrese el {dato} del repuesto:\n'))
        except:
            limpiar_pantalla()
            print('Error: ingreso invalido.\nSolo ingrese números.\n')
            continue
        resp = input(f'{dato.upper()}: {valor}\n¿Es correcto?(s/n):\n').lower().replace(' ', '')
        if resp in ['s','si']:
            limpiar_pantalla()
            return valor
        elif resp in ['n','no']:
            limpiar_pantalla()
            print('Okey, intente de nuevo')
        else:
            limpiar_pantalla()
            print('Error: respuesta invalida\nIntente con (s, si , n, no)\n')