#El siguiente código sirve para identificar los códigos ASCII de los caracteres y el inverso.

print('Bienvenido al programa para analizar caracteres en la tabla ASCII')

carac=input('Por favor, ingrese un carácter cualquier utilizando el teclado: ')
ord_carac=ord(carac)

print(f'El carácter ingresado es {carac} y su número correspondiente en la tabla ASCII es {ord_carac}')

suma=input('Ingrese un número entero para verificar el siguiente carácter: ')

new_ord=int(ord_carac)+int(suma)

new_carac=chr(new_ord)

print(f'El resultado de {ord_carac} + {suma} es {new_ord}. El carácter que corresponde a ese número en la tabla es {new_carac}')
