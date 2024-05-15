'''
Crear un diccionario con los nombres de los alumnos y sus notas, y promediarlos
-------------------------------------------------------------------------------
ind = indice
dik = diccionario
'''
import os
dik = {'Juan': [4.0, 5.0, 7.0], 'Mario': [2.0, 7.0], 'Felipe': [5.0, 6.0, 7.0]}
promedios = ['Juan', 'Mario', 'Felipe']
prom = 0
num = 1
ind = 0
#Utiliza un bucle for para recorrer el diccionario y calcular el promedio de las notas.
notas = [nota for nota in dik.items()]

while True:
    num = 1
    if not 'Juan' in promedios and not 'Mario' in promedios and not 'Felipe' in promedios:
        os.system('cls')
        print(f'Los promedios finales fueron:\nJuan: {promedios[0]}\nMario: {promedios[1]}\nFelipe: {promedios[2]}')
        exit('Ya promediaste todo, adios!')
    for clave, notas in dik.items():
        print(f'{num}.{clave}: {notas}')
        notas = [nota for nota in dik.items()]
        num += 1
    while True:
        try:
            resp = int(input('¿Que estudiante quieres promediar?:\n'))
            break
        except:
            print('Error: Solo ingrese numeros')
    if resp == 1:
        prom = 0
        prom += notas[0][1][0]
        prom += notas[0][1][1]
        prom += notas[0][1][2]
        prom /= 3
        promedios[0] = prom
        print(f'Juan: {prom}')
    elif resp == 2:
        prom = 0
        prom += notas[1][1][0]
        prom += notas[1][1][1]
        prom /= 2
        promedios[1] = prom
        print(f'Mario: {prom}')
    elif resp == 3:
        prom = 0
        prom += notas[2][1][0]
        prom += notas[2][1][1]
        prom += notas[2][1][2]
        prom /= 3
        promedios[2] = prom
        print(f'Felipe: {prom}')
    else:
        print('Respuesta no valida')
        break

#Muestra el promedio final.

