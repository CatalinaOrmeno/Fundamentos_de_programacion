from random import randint
from statistics import geometric_mean
from pathlib import Path
import os

data = [[x for x in range(2000,2011)]]
menup = ['Poblar',
         'Clasificar',
         'Estadisticas',
         'Exportar',
         'Salir']

def verificar_lista(lista:list):
    if len(lista) > 1:
        print('Los datos ya han sido generados')
        print('No hay nada que se pueda hacer\n')
        return True
    else: return True

def verificar_lista2(lista):
    if len(lista) < 2:
        print('La data aun no ha sido generada')
        print('No hay nada que se pueda hacer\n')
        return False
    else: return True

def poblar(lista:list):
    lista.append([])
    for anio in lista[0]:
        lista[1].append(randint(100,201))

def listar(lista:list):
    for ind, opc in enumerate(lista):
        print(f'{ind+1}. {opc}')

def mostrar_clasificación(lista:list):
    for i in lista:
        print(f'\tAÑO: {data[0][i]} - ML: {data[1][i]}')
    print()

def clasificar(piso,techo):
    cont1 = 0
    cont2 = 0
    cont3 = 0
    ran1 = []
    ran2 = []
    ran3 = []
    for ind,ml in enumerate(data[1]):
        if ml < piso:
            cont1 += 1
            ran1.append(ind)
        elif ml in range(piso,techo+1):
            cont2 += 1
            ran2.append(ind)
        elif ml > techo:
            cont3 += 1
            ran3.append(ind)
    print(f'MENORES QUE {piso} ML: {cont1}')
    mostrar_clasificación(ran1)
    print(f'ENTRE {piso} ML Y {techo} ML: {cont2}')
    mostrar_clasificación(ran2)
    print(f'MAYORES QUE {techo} ML: {cont3}')
    mostrar_clasificación(ran3)

def estadistica(lista:list):
    print()
    ind = lista[1].index(min(lista[1]))
    print('El año con menos lluvia fue:')
    print(f'\tAÑO: {lista[0][ind]} - ML: {lista[1][ind]}\n')
    ind = lista[1].index(max(lista[1]))
    print('El año con más lluvia fue:')
    print(f'\tAÑO: {lista[0][ind]} - ML: {lista[1][ind]}\n')
    mean = round(sum(lista[1])/len(lista[1]), 2)
    print(f'El promedio de lluvia entre los años 2000 y 2010 es: {mean} ML\n')
    geo = round(geometric_mean(lista[1]), 2)
    print(f'La media geometrica es de: {geo} ML\n')

def exportar(lista:list):
    mean = round(sum(lista[1])/len(lista[1]), 2)
    geo = round(geometric_mean(lista[1]), 2)
    tabla = ''
    tabla += '|'
    tabla += 'AÑO'.center(6, ' ') + '|'
    tabla += 'ML'.center(6, ' ') + '|'
    tabla += 'PROM'.center(10, ' ')+'|'
    tabla += 'GEO'.center(10, ' ')+ '|\n'
    tabla += '─'*37 + '\n'
    for ind, opc in enumerate(lista[1]):
        tabla += '|'
        tabla += str(data[0][ind]).center(6, ' ')+'|'
        tabla += str(opc).center(6, ' ')+'|'
        tabla += str(mean).center(10, ' ')+'|'
        tabla += str(geo).center(10, ' ')+'|\n'
    print(tabla)
    home = Path(__file__).parent
    if not Path(home/'export.txt').exists():
        Path(home/'export.txt').touch()
        ruta_txt = Path(home/'export.txt')
    else:
        Path(home/'export.txt').unlink()
        Path(home/'export.txt').touch()
        ruta_txt = Path(home/'export.txt')
    
    with open(ruta_txt,mode='w',encoding='UTF-8') as open_file:
        open_file.write(tabla)
    


while True:
    listar(menup)
    resp = input('¿Que desea hacer?: ')
    if resp == '1':
        os.system('cls')
        if verificar_lista(data):
            poblar(data)
    elif resp == '2':
        os.system('cls')
        if verificar_lista2(data):
            clasificar(130,160)
    elif resp == '3':
        os.system('cls')
        if verificar_lista2(data):
            estadistica(data)
    elif resp == '4':
        os.system('cls')
        if verificar_lista2(data):
            exportar(data)
    elif resp == '5':
        os.system('cls')
        exit('Versión 1.0\nCreado por Catalina Ormeño\nGracias por usar!')
    else:
        os.system('cls')
        print('Opción invalida!')