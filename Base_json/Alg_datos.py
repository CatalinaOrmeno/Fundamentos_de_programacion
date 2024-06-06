'''
Este algoritmo hace la funcion de ingresar datos de clientes y guardarlos en un archivo .json
---------------------------------------------------------------------------------------------
home = Ruta relativa del algoritmo
data = Datos a ingresar en el json
ruta_j = ruta del archivo json
archivo_abierto = variable determinada para ejercer la apertura del archivo json
archivo_json = contiene los contenidos del archivo json y la junta con el nuevo dato a ingresar
'''
from pathlib import Path
import json
import os
home = Path(__file__).parent

if not Path(home/'base_d.json').exists():
    Path(home/'base_d.json').touch()

menup = ['Agregar nuevo cliente', 'Buscar cliente', 
         'Eliminar cliente', 'Salir']
data = {'rut':'','dv':'','nombre':'','apellido':''}
ruta_j = Path(home/'base_d.json')

while True:
    for i, opc in enumerate(menup):
        print(f'{i + 1}. {opc}')
    resp = input('¿Que deseas hacer?:\n')
    os.system('cls')
    if resp == '1':
        os.system('cls')
        if Path(ruta_j).stat().st_size == 0:
            archivo_json = []
        else:
            while True:
                rut = str(input('Ingrese el rut de cliente de la siguiente forma: (12345678-9)\n')).lower()
                try:
                    new_rut = rut.split('-')[0]
                    dv = rut.split('-')[1]
                except:
                    os.system('cls')
                    print('Error: el ingreso no fue valido, intente de nuevo.\n')
                    continue
                found = 0
                with open(ruta_j, mode='r') as archivo_abierto:
                    archivo_json = json.load(archivo_abierto)
                for dicc in archivo_json:
                    if dicc['rut'] == new_rut:
                        found += 1
                if found != 0:
                    os.system('cls')
                    print('Error: el rut ingresado ya existe\n')
                    continue
                    
                if not new_rut.isnumeric():
                    os.system('cls')
                    print('Error: El rut (sin el dijito verificador) es invalido\n')
                    continue
                elif len(new_rut) != 8:
                    os.system('cls')
                    print('Error: la cantidad de números en el rut es incorrecta\n')
                    continue

                if dv.isnumeric() or dv == 'k':
                    if len(dv) == 1:
                        os.system('cls')
                        print('El rut fue ingresado correctamente\n')
                        break
                    else:
                        os.system('cls')
                        print('Error: El dijito verificador tiene más de un dijito\n')
                        continue
                else:
                    os.system('cls')
                    print('Error: El dijito verificador no es valido\n')
                    continue

            si = False
            while si == False:
                nom = str(input('Ingrese el nombre del cliente:\n')).replace(' ','')
                if not nom.isalpha():
                    os.system('cls')
                    print('Error: ingrese solo letras\n')
                    continue
                os.system('cls')
                apell = str(input('Ingrese el apellido del cliente:\n')).replace(' ','')
                if not apell.isalpha():
                    os.system('cls')
                    print('Error: ingrese solo letras\n')
                    continue
                os.system('cls')
                while True:
                    resp = input(f'Nombre: {nom}\tApellido: {apell}\n¿Es correcto? (s/n):\n').lower()
                    if resp in ['si', 's']:
                        os.system('cls')
                        print('Nombre y Apellido confirmados.\n')
                        si = True
                        break
                    elif resp in ['no', 'n']:
                        os.system('cls')
                        print('Entendido, ingreselo nuevamente.\n')
                        break
                    else:
                        os.system('cls')
                        print('Error: la respuesta no es valida.\nintente con (si o s / no o n)\n')
            
            data.update({'rut':new_rut})
            data.update({'dv':dv})
            data.update({'nombre':nom})
            data.update({'apellido':apell})

            with open(ruta_j, mode='r') as archivo_abierto:
                archivo_json = json.load(archivo_abierto)
        
        archivo_json.append(data)
        if len(archivo_json) >= 2:
            for diccionario in archivo_json:
                if diccionario['rut'] == '':
                    archivo_json.remove(diccionario)
        archivo_json = sorted(archivo_json, key=lambda x: x['rut'])
        with open(ruta_j, mode='w') as archivo_abierto:
            wjson = json.dump(archivo_json, archivo_abierto)
    elif resp == '2':
        os.system('cls')
        if Path(ruta_j).stat().st_size == 0:
            os.system('cls')
            print('Error: no se ha ingresado ningun cliente todavia.\n')
        else:
            while True:
                resp = str(input('Ingrese el rut del cliente que desea buscar:(sin dijito verificador)\n')).replace(' ','')
                if not resp.isnumeric():
                    os.system('cls')
                    print('Error: El rut (sin el dijito verificador) es invalido\n')
                    continue
                elif len(resp) != 8:
                    os.system('cls')
                    print('Error: la cantidad de números en el rut es incorrecta\n')
                    continue
                else: break

            not_found = 0
            with open(ruta_j, mode='r') as archivo_abierto:
                archivo_json = json.load(archivo_abierto)
            for diccionario in archivo_json:
                if diccionario['rut'] == resp:
                    os.system('cls')
                    print(f'RUT: {diccionario['rut']}-{diccionario['dv']}\nNombre: {diccionario['nombre']}\nApellido: {diccionario['apellido']}\n')
                else:
                    not_found += 1
                    if not_found == len(archivo_json):
                        os.system('cls')
                        print('Error: no se encontro ninguna coincidencia\n')
    elif resp == '3':
        os.system('cls')
        if Path(ruta_j).stat().st_size == 0:
            os.system('cls')
            print('Error: no se ha ingresado ningun cliente todavia.\n')
        else:
            while True:
                resp = str(input('Ingrese el rut del cliente que desea eliminar:(sin dijito verificador)\n')).replace(' ','')
                if not resp.isnumeric():
                    os.system('cls')
                    print('Error: El rut (sin el dijito verificador) es invalido\n')
                    continue
                elif len(resp) != 8:
                    os.system('cls')
                    print('Error: la cantidad de números en el rut es incorrecta\n')
                    continue
                else: break

            not_found = 0
            with open(ruta_j, mode='r') as archivo_abierto:
                archivo_json = json.load(archivo_abierto)
            for diccionario in archivo_json:
                if diccionario['rut'] == resp:
                    archivo_json.remove(diccionario)
                else:
                    not_found += 1
                    if not_found == len(archivo_json):
                        os.system('cls')
                        print('Error: no se encontro ninguna coincidencia\n')
                    else:
                        os.system('cls')
                        print('El cliente se a eliminado exitosamente.')
            with open(ruta_j, mode='w') as archivo_abierto:
                wjson = json.dump(archivo_json, archivo_abierto)
    elif resp == '4':
        os.system('cls')
        exit('Gracias por haber utilizado el algoritmo.\nAdios.')
    else:
        os.system('cls')
        print('Error: respuesta invalida')
        