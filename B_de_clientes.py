import numpy as np
import os

ver = [str(x) for x in range(10)] + ['K']

print('='*50)
print(' CLIENTES '.center(50, '='))
print('='*50)

base = np.array([['12345678', 'K', 'María', 'Gómez', 'calle456', '678987678'],
                 ['16254865', '1', 'Pedro', 'Fernández', 'av789', '345678345'],
                 ['19851543', '7', 'Laura', 'Ramírez', 'plaza012', '789012789'],
                 ['20587656', '0', 'Juan', 'Sánchez', 'parque345', '234567234'],
                 ['15864548', '3', 'Sofía', 'Martínez', 'calle678', '567890567']])
menup = ['Buscar cliente', 'Agregar cliente', 'Eliminar cliente', 'Salir']

while True:
    for ind, opt in enumerate(menup):
        print(f'{ind + 1}. {opt}')
    ans = input('Elige una opción:\n')
    if ans == '1':
        while True:
            rut = input('Ingrese el rut del cliente a buscar (sin dijito verificador):\n')
            if len(rut) not in range(7, 9) or not rut.isnumeric():
                os.system('cls')
                print('Error: formato de rut no valido\n')
                continue
            break
        if rut in base:
            ind = np.where(base == rut)[0][0]
            os.system('cls')
            print(f'Rut: {base[ind][0]}-{base[ind][1]}')
            print(f'Nombre: {base[ind][2]}')
            print(f'Apellido: {base[ind][3]}')
            print(f'Dirección: {base[ind][4]}')
            print(f'Teléfono: {base[ind][5]}\n')
        elif not rut in base:
            os.system('cls')
            print('Error: el cliente no existe\n')
    elif ans == '2':
        os.system('cls')
        while True:
            try:
                rut = input('Ingrese el rut del cliente(12345678-9):\n')
                new_rut = rut.split('-')[0]
                dv = rut.split('-')[1]
                if new_rut in base:
                    os.system('cls')
                    print('Error: cliente ya exite\n')
                    continue
                elif len(new_rut) not in range(7, 9) or not new_rut.isnumeric():
                    os.system('cls')
                    print('Error: rut invalido\n')
                    continue
                if not dv.upper() in ver:
                    os.system('cls')
                    print('Error: dijito verificador invalido\n')
                    continue
            except:
                os.system('cls')
                print('Error: rut no valido')
                continue
            
            nombre = input('Ingresa el nombre del cliente:\n').capitalize().replace(' ','')
            if not nombre.isalpha():
                os.system('cls')
                print('Error: nombre no valido\n')
                continue

            apellido = input('Ingresa el apellido del cliente:\n').capitalize().replace(' ','')
            if not apellido.isalpha():
                os.system('cls')
                print('Error: apellido no valido\n')
                continue

            fono = input('Ingrese el teléfono del cliente(123456789):\n')
            if len(fono) != 9 or not fono.isnumeric():
                os.system('cls')
                print('Error: teléfono no valido\n')
                continue
            dire = input('Ingrese la dirección del cliente:\n')
            new = np.array([new_rut, dv, nombre, apellido, dire, fono])
            base = np.vstack((base, new))
            os.system('cls')
            print('Cliente agregado exitosamente!\n')
            break
    elif ans == '3':
        while True:
            rut = input('Ingrese el rut del cliente a buscar (sin dijito verificador):\n')
            if len(rut) not in range(7, 9) or not rut.isnumeric():
                os.system('cls')
                print('Error: formato de rut no valido\n')
                continue
            break
        if rut in base:
            ind = np.where(base == rut)[0][0]
            os.system('cls')
            base = np.delete(base, ind)
            print('Cliente eliminado exitosamente!\n')
        elif not rut in base:
            os.system('cls')
            print('Error: el cliente no existe\n')
    elif ans == '4':
        exit('Adiós!')
    else:
        print('Error: opción no válida\n')


