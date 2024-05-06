#El propocito de este algoritmo es calificador de estado, que sirve para comprovar si un cliente es apto para pedir un prestamo bancario o no.

print('Bienvenido al clasificador de estados de cliente')

nombre=input('Ingrese el nombre del cliente:\n')
edad=int(input('Ingrese la edad del cliente:\n'))
est_civil=input('Ingrese estado civil del cliente:\n')
saldo=input('Ingrese el saldo del cliente:\n')

nombre=nombre.replace(' ','')

if nombre.isalpha()==False:
    exit('Error: Nombre inválido')

elif edad < 18 or edad > 60:
    exit('Error: Edad inválida')


print('berificando')




    

