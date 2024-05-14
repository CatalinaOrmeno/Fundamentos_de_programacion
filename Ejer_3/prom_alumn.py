'''
Crear un diccionario con los nombres de los alumnos y sus notas, y promediarlos
-------------------------------------------------------------------------------
ind = indice
dik = diccionario
'''

dik = {'Juan': [4.0, 5.0, 7.0], 'Mario': [2.0, 7.0], 'Felipe': [5.0, 6.0, 7.0]}
promedios = []
prom = 0
num = 1
ind = 0
#Utiliza un bucle for para recorrer el diccionario y calcular el promedio de las notas.
notas = [nota for nota in dik.items()]

for clave, notas in dik.items():
    print(f'{num}.{clave}: {notas}')
    notas = [nota for nota in dik.items()]
    num += 1

while True:
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
        promedios.append(prom)
        print(promedios)
    elif resp == 2:
        prom = 0
        prom += notas[1][1][0]
        prom += notas[1][1][1]
        prom /= 2
        promedios.append(prom)
        print(promedios)
    elif resp == 3:
        prom = 0
        prom += notas[2][1][0]
        prom += notas[2][1][1]
        prom += notas[2][1][2]
        prom /= 3
        promedios.append(prom)
        print(promedios)
    else:
        print('Respuesta no valida')
        break

#Muestra el promedio final.

