# desarrolla un algoritmo que pregunte al usuario su nombre y sus apellidos
# que le pida un número flotante.
# que le pida un número entero.
# que muestre en una cadena su nombre y los números que escogio.
# que muestre en una cadena el tipo de datos de los numeros que escogio.
# que convierta el flotante en entero, devuelva su valor y su tipo de dato.

nombre=input('Ingrese su nombre.\n')
apellP=input('Ingrese su apellido paterno.\n')
apellM=input('Ingrese su apellido materno.\n')

num1=float(input('Ingrese un número decimal.\n'))
num2=int(input('Ingrese un número entero.\n'))

print('Nombre completo:',nombre,apellP,apellM+'.')
print(f'Números elegidos:\n.....Número decimal: {num1}\n.....Número entero: {num2}')

print('Tipo del número 1:',{type(num1)},'\nTipo del número 2:',{type(num2)})

num1=int(num1)

print(f'El decimal convertido a entero es: {num1}, y su tipo de dato es: {type(num1)}')
