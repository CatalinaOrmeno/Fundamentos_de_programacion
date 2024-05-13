'''
Aqui guardamos clientes
---------parametros-------
nombre = nombre del cliente
apellido = apellido del cliente
fono = numero del cliente
direccion = direccion del cliente
'''

import os

nombre = ['Juanin']
apellido = ['Juan Harry']
fono = [912345678]
direccion = ['TVN 123']

menup = ['Ver Clientes', 'Añadir Cliente', 'Eliminar Cliente', 'Salir']

while True:
    for ind, elem in enumerate(menup):
        print(f'{ind + 1}. {elem}')
    resp = input('¿Que quieres hacer?:\n')
    if resp == '1':
        os.system('cls')
        for ind in range(len(nombre)):
            print(f'Nombre: {nombre[ind]}')
            print(f'Apellido: {apellido[ind]}')
            print(f'Fono: {fono[ind]}')
            print(f'Dirección: {direccion[ind]}\n')

    elif resp == '2':
        os.system('cls')
        while True:
            new_nombre = input('Ingresa el nombre del cliente:\n')
            new_apellido = input('Ingrese el apellido del cliente:\n')
            if not new_nombre.replace(' ', '').isalpha() or not new_apellido.replace(' ', '').isalpha():
                os.system('cls')
                print('Error: el nombre o el apellido tiene que estar solo en texto')
                continue
            new_fono = input('Ingrese el numero del cliente:\n')
            if not new_fono.isnumeric() or len(new_fono) != 9:
                os.system('cls')
                print('Error: el telefono debe tener solo 9 numeros\n')
            new_direccion = input('Ingrese la dirección del cliente:\n')
            while True:
                os.system('cls')
                print(f'Nombre: {new_nombre}')
                print(f'Apellido: {new_apellido}')
                print(f'Fono: {new_fono}')
                print(f'Dirección: {new_direccion}')
                resp = input('\n¿Son los datos correctos? (s/n):\n')
                if resp.lower() in ['s', 'si', 'n', 'no']:
                    if resp.lower() == 's' or resp.lower() == 'si':
                        nombre.append(new_nombre)
                        apellido.append(new_apellido)
                        fono.append(new_fono)
                        direccion.append(new_direccion)
                        break
                    elif resp.lower() == 'n' or resp.lower() == 'no':
                        os.system('cls')
                        continue
                else:
                    os.system('cls')
                    print('Error: la respuesta no es valida')
                    continue
            break

    elif resp == '3':
        os.system('cls')
        for ind in range(len(nombre)):
            print(f'{ind + 1}. {nombre[ind]}\t{apellido[ind]}')
        while True:
            try:
                resp = int(input('¿Cual cliente le gustaria eliminar?:\n'))
                break
            except:
                os.system('cls')
                print('Error: solo se puede ingresar numeros')
                continue
        if resp - 1 <= len(nombre):
            del nombre[resp - 1]
            del apellido[resp - 1]
            del fono[resp - 1]
            del direccion[resp - 1]
        else:
            os.system('cls')
            print('Error: el cliente que pidio no existe')
        os.system('cls')
        print('Cliente eliminado exitosamente')
        
    elif resp == '4':
        os.system('cls')
        exit('Gracias por usar el programa')
    else:
        os.system('cls')
        print('Ingrese una respuesta valida')