#admnistrar stock
import os

print('=' * 50)
print(' STOCK '.center(50, '='))
print('=' * 50)

productos = {'Harina': 10, 'Huevos': 50, 'Escoba': 5, 'Jugo de naranja': 3}
menu = ['Ver productos', 'Agregar Producto', 'Eliminar Producto', 'Salir']

while True:
    while True:
        for indice in range(len(menu)):
                print(f'{indice+1}. {menu[indice]}')
        try:
            resp = int(input('Elige una opción:\n'))
            break
        except:
            os.system('cls')
            print('Por favor, ingrese un numero\n')
    if resp == 1:
        os.system('cls')
        for x in productos:
            print(f'{x.center(20, " ")}: {productos[x]}')
        print()
    elif resp == 2:
        while True:
            new_item = input('Ingrese el nombre del producto:\n')
            if new_item.replace(' ', '').isalpha():
                new_item = new_item.capitalize()
                break
            else:
                print('Solo ingrese letras')
        if new_item in productos:
            os.system('cls')
            print('Error: El producto ya existe\n')
        else:
            os.system('cls')
            while True:
                try:
                   productos[new_item] = int(input('Ingrese cuanto inventario hay:\n'))
                   break
                except:
                    os.system('cls')
                    print('Por favor, ingrese un numero\n')
            os.system('cls')
            print('Producto agregado exitosamente.')
    elif resp == 3:
        while True:
            edit_item = input('Ingrese el nombre del producto que desea eliminar:\n')
            if edit_item.replace(' ', '').isalpha():
                edit_item = edit_item.capitalize()
                break
            else:
                print('Solo ingrese letras')
        if not edit_item in productos:
            print('Error: El producto no existe')
        else:
            os.system('cls')
            del productos[edit_item]
            print('Producto eliminado exitosamente.')
    elif resp == 4:
        os.system('cls')
        exit('Adios!')
    else:
        os.system('cls')
        print('Error: respuesta no valida.\n')