'''
Este algoritmo administra una base de datos de una tienda
---------------------------------------------------------
stock = {codigo: nombre, talla, precio}
'''
import os
def limpiar():
    os.system('cls')

def cabezera():
    print('='*50)
    print(' L A  R O P I T A '.center(50,'='))
    print('='*50)

stock = {111222333444: ['polera polo azul', 'S', 14990],
         111222333445: ['polera polo amarilla', 'L', 14990],
         111222333446: ['chaqueta azul', 'XS', 19990],
         111222333447: ['chaqueta roja', 'XL', 19990]}

menup = ['Agregar productos', 'Buscar prenda', 'Mostrar inventario',
        'Calcular total', 'Salir']

tallas = ['XS', 'S', 'M', 'L', 'XL']

while True:
    cabezera()
    for ind, opt in enumerate(menup):
        print(f'{ind + 1}. {opt}')
    resp = input('Elige una opción:\n').replace(' ','')
    if resp == '1':
        limpiar()
        ind = max(stock.keys())
        while True:
            nom = input('Ingresa el nombre de la prenda:\n')
            limpiar()
            resp = input(f'Nonbre: {nom}\n¿Es correcto? (s/n):\n')
            if resp.lower() in ['n', 'no']:
                limpiar()
                continue
            elif resp.lower() in ['s', 'si']:
                break
            else:
                limpiar()
                print('Error: respuesta no valida')
        limpiar()
        while True:
            size = input('Ingresa la talla de la prenda:\n')
            if not size.upper() in tallas:
                limpiar()
                print('Error: elige una talla valida')
                print('Las tallas validas son las siguientes:')
                for t in tallas:
                    print(t, end=' ')
                print()
                continue
            break
        limpiar()
        while True:
            try:
                price = int(input('Ingresa el precio de la prenda:\n'))
                limpiar()
                resp = input(f'Precio: ${price}\n¿Es correcto? (s/n):\n')
                if resp.lower() in ['n', 'no']:
                    limpiar()
                    continue
                elif resp.lower() in ['s', 'si']:
                    limpiar()
                    break
                else:
                    limpiar()
                    print('Error: respuesta no valida')
            except:
                limpiar()
                print('Error: precio no valido')
        stock[ind + 1] = [nom.lower(), size.upper(), price]
        limpiar()
        print('La prenda a sido agregada correctamente')
    elif resp == '2':
        limpiar()
        cont = 0
        resp = input('\nIngresa el código o nombre del producto:\n').lower()
        print()
        for prod in stock:
            if str(prod) == resp or resp in stock[prod][0]:
                print(f'Nombre: {stock[prod][0].upper()}')
                print(f'Codigo: {prod}')
                print(f'Talla: {stock[prod][1].upper()}')
                print(f'Precio: ${stock[prod][2]}\n')
                cont += 1
        if cont == 0:
            limpiar()
            print('Error: no existe ningun producto con ese nombre o código')
    elif resp == '3':
        limpiar()
        for prod in stock:
            print(f'Nombre: {stock[prod][0].upper()}')
            print(f'Codigo: {prod}')
            print(f'Talla: {stock[prod][1].upper()}')
            print(f'Precio: ${stock[prod][2]}\n')
    elif resp == '4':
        limpiar()
        val = 0
        for prod in stock:
            val += stock[prod][2]
        print(f'Total: ${val}')
    elif resp == '5':
        limpiar()
        print('Adios')
        break
    else:
        limpiar()
        print('Error: respuesta no valida')