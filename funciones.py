#menup = ['Letras', 'Números', 'Salir']
#num = [num for num in range(10)]
#Letras = ['A', 'B', 'C', 'D', 'E']

#def listar(lista):
#    '''Esta funcion lista cosas'''
#    for ind, opt in enumerate(lista):
#        print(f'{ind + 1}. {opt}')

#def responder():
#    '''Esta funcion recoge una respuesta y la guarda en una variable'''
#    resp = input('¿Que quieres hacer?\n')
#    return resp

#while True:
#    listar(menup)
#    resp = responder()
#    if resp == '1':
#        listar(Letras)
#    elif resp == '2':
#        listar(num)
#    elif resp == '3':
#        exit('Adios')
#    else:
#        print('Error: respuesta no valida')



#cadena = '12.345.678-9'

#def reemplazador(ingreso, *args):
#    resultado = ingreso
#    for arg in args:
#        resultado = resultado.replace(arg,'')
#    return resultado

#cadena = reemplazador(cadena, '.')
#print(cadena)



#from pathlib import Path
#home = Path(__file__).parent
#def construir(*argumentos):
#    ruta = home
#    for arg in argumentos:
#        ruta = Path(f'{ruta}/{arg}')
#    return ruta

#def verificar(ruta_av):
#    if ruta_av.exists():
#        print('La ruta existe')
#    else:
#        print('La ruta no existe')
#        ruta_av.mkdir()

#verificar(construir('Carpeta1'))
