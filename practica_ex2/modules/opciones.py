from random import randint
from os import system
from pathlib import Path

def cls():
    system('cls')

def poblar(lista:list):
    if len(lista[1]) == 0:
        for producto in enumerate(lista[0]):
            lista[1].append(randint(1,120))
    else:
        print('Los datos ya han sido cargados!')

def clasificar(data:list):
    if len(data[1]) != 0:
        menor_a_50 = []
        de_50_a_100 = []
        mayor_a_100 = []
        for ind,stock in enumerate(data[1]):
            if stock < 50:
                menor_a_50.append(ind)
            elif stock >= 50 and stock <= 100:
                de_50_a_100.append(ind)
            else:
                mayor_a_100.append(ind)
        print(f'STOCK MENOR A 50:\n')
        mostrar_calificación(data, menor_a_50)
        print(f'STOCK ENTRE 50 A 100:\n')
        mostrar_calificación(data, de_50_a_100)
        print(f'STOCK MAYOR A 100:\n')
        mostrar_calificación(data, mayor_a_100)
    else: print('Error: no hay datos ingresados')

def mostrar_calificación(data:list,lista:list):
    for indice in lista:
        print(f'\tPRODUCTO: {data[0][indice]}    STOCK: {data[1][indice]}')
    print()

def exportar(data:list):
    tabla = ''
    tabla += 'PRODUCTOS'.ljust(12,' ') + 'STOCK'.ljust(12,' ') + '\n'
    for ind,opc in enumerate(data[0]):
        tabla += str(data[0][ind]).ljust(12,' ') + str(data[1][ind]).ljust(12,' ') + '\n'
    home = Path(__file__).parent.parent
    ruta_txt = Path(home/'export.txt')
    if ruta_txt.exists():
        ruta_txt.unlink()
        ruta_txt.touch()
    else: ruta_txt.touch()
    with open(ruta_txt,mode='w',encoding='UTF-8') as open_file:
        open_file.write(tabla)