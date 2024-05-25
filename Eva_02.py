'''Aqui vendemos
Este algoritmo tiene la funcion de mostrar y modificar 
el stock de una tienda llamada "Aqui vendemos"
-------------------------------------------------------

'''
import os
menup = []
menup.append('Ver stock de productos')
menup.append('Añadir nuevo producto')
menup.append('Ajustar stock')
menup.append('Eliminar producto')
menup.append('Salir')

productos = {'Escoba': 5, 'Huevos': 25, 'Leche': 9}
print('*' * 30)
print('Administración de stock')
print('*' * 30)
while True:
    contador = 0
    index_ = [index_ for index_ in range(len(productos))]
    for ind in range(len(menup)):
        print(f'{ind + 1}. {menup[ind]}')    
    try:
        resp = int(input('¿Que quieres hacer?\n'))
    except:
        os.system('cls')
        print('Solo puedes ingresar números')
        continue
    if resp == 1:
        os.system('cls')
        for clave, produc in productos.items():
            print(f'{index_[contador] + 1}. {clave}: {produc}')
            contador += 1
        print()
    elif resp == 2:
        os.system('cls')
        while True:
            nombre = input('Ingrese el nombre del nuevo producto:\n').replace(' ', '').capitalize()
            if nombre.isalpha():
                break
            else:
                os.system('cls')
                print('Error: solo ingrese letras')
        while True:
            try:
                stock = int(input('Ingrese el stock del nuevo producto:\n').replace(' ', ''))
                break
            except:
                os.system('cls')
                print('Error: Solo ingrese números')
        if nombre in productos.keys():
            os.system('cls')
            print('Error: este producto ya existe')
        else:
            productos[nombre] = stock
            os.system('cls')
            print('El producto se añadio exitosamente')
    elif resp == 3:
        while True:
            nombre = str(input('Ingrese el nombre del producto que desea actualizar:\n').replace(' ', '').capitalize())
            if nombre.isalpha():
                break
            else:
                os.system('cls')
                print('Error: Solo ingrese letras')
        if not nombre in productos.keys():
            os.system('cls')
            print('Error: este producto no existe')
        else:
            while True:
                try:
                    stock = int(input('Ingrese el stock del producto:\n').replace(' ', ''))
                    break
                except:
                    os.system('cls')
                    print('Error: Solo ingrese números')
            productos[nombre] = stock
            os.system('cls')
            print('El stock se ha actualizado exitosamente')
    elif resp == 4:
        os.system('cls')
        while True:
            nombre = str(input('Ingrese el nombre del producto que quiere eliminar:\n').replace(' ', '').capitalize())
            if nombre.isalpha():
                break
            else:
                os.system('cls')
                print('Error: Solo ingrese letras')
        if not nombre in productos.keys():
            os.system('cls')
            print('Error: este producto no existe')
        else:
            productos.pop(nombre)
            os.system('cls')
            print('El producto se elimino exitosamente')
    elif resp == 5:
        exit('Adios!')
    else:
        os.system('cls')
        print('Error: respuesta invalida')
