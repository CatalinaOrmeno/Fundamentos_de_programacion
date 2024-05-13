'''Ingreso de autos 
para el taller
en diccionario'''
import os
ind = 1
ingreso = {}

menup = ['Ver Autos', 'Añadir autos', 'Eliminar auto', 'Salir']

while True:
    print('¿Que desea hacer?')
    for inde, elem in enumerate(menup):
        print(f'{inde + 1}. {elem}')

    while True:
        try:
            resp = int(input('Elija el numero de la opcion correspondiente:\n'))
            break
        except:
            print('Solo ingrese números')

    if resp == 1:
        os.system('cls')
        for llave, valor in ingreso.items():
            print(f'{llave}:\n Dueño: {valor[0]}\t Marca-modelo: {valor[1]}\n')
    elif resp == 2:
        os.system('cls')
        nom = input('Ingrese el nombre del cliente:\n').capitalize()
        marca = input('Ingrese la marca del modelo:\n')
        ingreso.update({('000' + str(ind)): [nom, marca]})
        ind = ind + 1
        os.system('cls')
    elif resp == 3:
        os.system('cls')
        while True:
            try:
                resp = int(input('Ingresa el registro que quieres eliminar:\n'))
                break
            except:
                os.system('cls')
                print('Error: el registro debe ser numerico')
        if str(resp) in ingreso:
            del ingreso[resp]
            os.system('cls')
            print('Registro borrado exitosamente')
        else:
            os.system('cls')
            print('Error: el registro indicado no existe')
    elif resp == 4:
        os.system('cls')
        print('Gracias por utilizar el programa\n¡Adios!')
        break
    else:
        os.system('cls')
        print('Por favor, elija una opción establecida:')

