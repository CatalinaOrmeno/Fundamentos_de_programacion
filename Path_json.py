from pathlib import Path
import json
import os
home = Path(__file__).parent

#Archivo.txt

#ruta_text = Path(home/'nuevo.txt')
#stream = Path(ruta_text).read_text()
#Path(ruta_text).write_text(stream + '\nHola de nuevo.')
#print(stream)

#Archivo.json

if not Path(home/'nuevo.json').exists():
    Path(home/'nuevo.json').touch()
else:
    print('El archivo ya existe.')

menup = ['Leer archivo', 'Escribir archivo']
data = {'NOMBRE':'Marco','APELLIDO':'Lechuga'}
ruta_j = Path(home/'nuevo.json')
while True:
    for i, opc in enumerate(menup):
        print(f'{i + 1}. {opc}')
    resp = input('Que quieres hacer?:\n')
    os.system('cls')
    if resp == '1':
        if Path(ruta_j).stat().st_size == 0:
            print('Error: el archivo esta vacio')
        else:
            with open(ruta_j, mode='r') as archivo_abierto:
                archivo_json = json.load(archivo_abierto)
                print(archivo_json)
    elif resp == '2':
        if Path(ruta_j).stat().st_size == 0:
            archivo_json = []
        else:
            with open(ruta_j, mode='r') as archivo_abierto:
                archivo_json = json.load(archivo_abierto)
            
        archivo_json.append(data)

        with open(ruta_j, mode='w') as archivo_abierto:
            wjson = json.dump(archivo_json, archivo_abierto)
    else:
        print('Error: respuesta invalida')