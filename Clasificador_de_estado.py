#El propocito de este algoritmo es calificador de estado, que sirve para comprovar si un cliente es apto para pedir un prestamo bancario o no.

print('Bienvenido al clasificador de estados de cliente')

nombre=input('Ingrese el nombre del cliente:\n')
edad=int(input('Ingrese la edad del cliente:\n'))
est_civil=input('Ingrese estado civil del cliente:\n')
saldo=int(input('Ingrese el saldo del cliente:\n'))

nombre=nombre.replace(' ','')
nombre=nombre.capitalize()
est_civil=est_civil.capitalize()

#Verificación del nombre
if nombre.isalpha()==False:
    exit('Error: Nombre inválido')

#Verificación de la edad
if edad < 18 or edad > 60:
    exit('Error: Edad inválida')

#Verificación del estado civil
if est_civil.isalpha()==False:
    exit('Error: Estado civil inválido')

if 'Soltero' in est_civil==False and 'Casado' in est_civil==False:
    exit('Error: Estado civil inválido')

#Verificación del saldo
if saldo < 0 or saldo > 9999999:
    exit('Error: Saldo inválido')

#Clasificando edad
if edad >= 18 and edad <= 29:
    cate_edad='Joven'
elif edad >= 30 and edad <= 49:
    cate_edad='Adulto'
else:
    cate_edad='Adulto Mayor'

#Clasificando saldo
if saldo >= 0 and saldo <= 2500000:
    cate_saldo='Bajo'
elif saldo >= 2500001 and saldo <= 5000000:
    cate_saldo='Medio'
else:
    cate_saldo='Alto'

#Clasificando riesgo
if 'Soltero' in est_civil:
    if 'Adulto Mayor' in cate_edad:
        cate_riesgo='Riesgo Alto'
    else:
        cate_riesgo='Riesgo Medio'
else:
    if 'Joven' in cate_edad:
        cate_riesgo='Riesgo Alto'
    else:
        cate_riesgo='Riesgo Medio'

#Apto o no apto
if 'Joven' in cate_edad:
    if 'Bajo' in cate_saldo:
        aptidad='no apto'
    else:
        aptidad='apto'
elif 'Mayor' in cate_edad:
    if 'Alto' in cate_saldo:
        aptidad='apto'
    else:
        aptidad='no apto'
else:
    if 'Bajo' in cate_saldo or 'Medio' in cate_saldo:
        if 'Medio' in cate_riesgo:
            aptidad='apto'
        else:
            aptidad='no apto'
    else:
        aptidad='apto'

print(f'El cliente {nombre} es {aptidad} para solicitar el crédito.')