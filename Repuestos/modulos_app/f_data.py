from pathlib import Path
import json
import csv

def cabezera():
    '''
    Esta función imprime la cabezera del negocio
    '''
    print('='*50)
    print(' El Repuestito '.upper().center(50,'='))
    print('='*50)

def crear_ruta_home():
    '''
    Esta función crea una ruta home para el archivo json.\n
    Apartir de la ruta del archivo del programa.\n
    ----RETURN----\n
    La funcion devuelve la ruta home y se guarda de la siguiente forma:\n
    home = crear_ruta_home()
    '''
    home = Path(__file__).parent.parent
    return home

def verificar_existencia_archivo_j(home: Path):
    '''
    Esta función sirve para verificar la existencia de la base de datos del negocio.\n
    Y si ya existia previamente, devuelve la ruta del archivo.\n
    ----PARAMS----\n
    home = ruta donde esta el archivo del programa\n
    ----RETURN----\n
    En caso que ya existiera la ruta, devolvera su ruta para poder ser almacenada en una variable.\n
    La cual se guardaria asi:\n
    ruta_j = verificar_existencia_archivo_j()
    '''
    while True:
        if not Path(home/'data.json').exists():
            Path(home/'data.json').touch()
        else:
            ruta_j = Path(home/'data.json')
            return ruta_j

def verificar_archivo_j_vacio(ruta_j: Path):
    '''
    Esta función sirve para verificar si un archivo.json ya existente tiene contenido o no.\n
    Si este no tiene contenido, va a poner una lista en el archivo.json.\n
    Y si este no esta vacio, devolvera un pase que se pueda usar en controles de flujo siguientes.\n
    ----PARAMS----\n
    ruta_j = la ruta del archivo.json\n
    ----RETURN----\n
    En caso de que ya se a comprovado el contenido del archivo.json, esta misma se puede usar como
    un pase para controles de flujo.
    '''
    while True:
        if Path(ruta_j).stat().st_size == 0:
            with open(ruta_j, mode='w') as stream:
                archivo_j = []
                new_json = json.dump(archivo_j, stream)
        else:
            return True
        

def actualizar_codigo(base_de_datos: list):
    codigo_inicial = 950256000
    for repuesto in base_de_datos:
        repuesto.update({"código":codigo_inicial})
        codigo_inicial += 1

def read_j(ruta_j: Path):
    with open(ruta_j,mode='r') as open_archive:
        archivo_j = json.load(open_archive)
    return archivo_j

def dump_j(base_de_datos: list, ruta_j: Path):
    with open(ruta_j,mode='w') as open_archive:
        new_base = json.dump(base_de_datos,open_archive)

def verificar_existencia_archivo_csv(home: Path):
    while True:
        if not Path(home/'repuestito.csv').exists():
            Path(home/'repuestito.csv').touch()
        else:
            Path(home/'repuestito.csv').unlink()
            Path(home/'repuestito.csv').touch()
            ruta_c = Path(home/'repuestito.csv')
            return ruta_c
        
def exportar(ruta_j, ruta_c):
    with open(ruta_j,mode='r') as open_archive:
        archivo_j = json.load(open_archive)
        for repuesto in archivo_j:
            line = [repuesto['código'],
                    repuesto['nombre'],
                    repuesto['marca'],
                    repuesto['modelo'],
                    repuesto['tipo'],
                    repuesto['valor'],
                    repuesto['stock']]
            with open(ruta_c, mode='a',newline='') as open_csv:
                whiter = csv.writer(open_csv, delimiter=',')
                whiter.writerow(line)
