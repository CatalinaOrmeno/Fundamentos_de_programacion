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
    resp = input('Que en que fila desea reservar?:\n').capitalize().replace(' ','')
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
num = 10
cine[ind, num] = 'X'

imprimir_cine()