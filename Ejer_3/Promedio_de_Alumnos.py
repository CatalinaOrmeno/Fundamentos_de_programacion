#Crea un diccionario que almacene las notas de un grupo de alumnos.
notasjuan = [4.0, 5.0, 7.0]
notasmario = [2.0, 7.0]
notasfelipe = [5.0, 6.0, 7.0]
dik = {'Juan': notasjuan, 'Mario': notasmario, 'Felipe': notasfelipe}
ind = 1
prom = 0

#Utiliza un bucle for para recorrer el diccionario y calcular el promedio de las notas.
for clave, notas in dik.items():
    print(f'{ind}.{clave}: {notas}')
    ind = ind + 1

while True:
    try:
        resp = int(input('¿Que estudiante quieres promediar?:\n'))
        break
    except:
        print('solo ingrese numeros')

while True:
    if resp == 1:
        pass
    elif resp == 2:
        pass
    elif resp == 3:
        pass
    else:
        print('Respuesta no valida')

#Muestra el promedio final.

