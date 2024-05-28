import numpy as np
import os

#Generar los números y letras
lista = [str(x) for x in range(1, 11)]
letras = ['A', 'B', 'C', 'D', 'E',
          'F', 'G', 'H', 'I', 'J']

array = np.array(lista * 10).reshape(10, 10)
letras = np.array(letras)
letras = letras[:, np.newaxis]
cine = np.hstack((letras, array))

def imprimir_cine():
    for linea in cine:
        for num in linea:
            print(num, end='  ')
        print()

while True:
    imprimir_cine()
    resp = input('¿En que fila desea reservar?:\n').capitalize().replace(' ','')
    if resp.isalpha() == False:
        os.system('cls')
        print('Error: la respuesta no es valida\n')
    elif not resp in cine:
        os.system('cls')
        print('Error: la fila no existe\n')
    else:
        break

ind = np.where(cine == resp)
ind = ind[0][0]

while True:
    try:
        num = int(input('¿Que asiento desea reservar?:\n'))
    except:
        os.system('cls')
        print('Error: ingreso no valido(Ingrese solo números)\n')
        continue
    if num in range(1, 11):
        break
    else:
        os.system('cls')
        print('Error: número de entrada no valido')
        imprimir_cine()
        continue

cine[ind, num] = 'X'
os.system('cls')
print('Entrada reservada exitosamente!')

imprimir_cine()
print(f'Entrada:\nFila {resp}   Número {num}')