'''
Prueba compresión de listas hgjhgfkajhnskjabnksfsfa
shgosijgoijsogihs
dogstring
'''
#variable = input('prueba:\n')
#lista = [letra.lower() for letra in variable if letra.lower() != ' ']
#print(lista)

#pares = [num for num in range(1, 101) if num % 2 == 0]
#impares = [num for num in range(1, 101) if num % 2 != 0]

#print('Pares: \n',pares)
#print('Impares: \n',impares)

fibo = []
num1 = 0
num2 = 1

for x in range(1,9):
    if num1 == 0:
        fibo.append(num1)
        fibo.append(num2)
    new_num = num1 + num2
    num1 = num2
    num2 = new_num
    fibo.append(num2)

print(fibo)
    
