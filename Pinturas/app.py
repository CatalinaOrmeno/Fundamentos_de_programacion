from modules.construcción import enumerar_lista, solicitar_acc
from modules.data import ruta_home, ruta_json, ruta_csv, empty_json, read_json, dump_json, cls, exportar

ruta_j = ruta_json(ruta_home())
empty_json(ruta_j)

menup = ['Ver listado',
         'Buscar',
         'Agregar',
         'Eliminar',
         'Exportar',
         'Salir']

data = {'código':'123',
        'nombre':'',
        'tipo':'',
        'valor':'',
        'stock':''}

while True:
    print('='*50)
    print(' PINTURAS '.center(50,'='))
    print('='*50)
    enumerar_lista(menup)
    resp = solicitar_acc()
    if resp == '1':
        cls()
        json_file = read_json(ruta_j)
        if len(json_file) == 0:
            print('Error: no hay registros')
        else:
            for pintura in json_file:
                print(f'\nCÓDIGO: {pintura["código"]}')
                print(f'NOMBRE: {pintura["nombre"]}\n')
    elif resp == '2':
        cls()
        json_file = read_json(ruta_j)
        if len(json_file) == 0:
            print('Error: no hay registros')
        else:
            resp = input('Ingrese el código, el nombre o el tipo de la pintura a buscar:\n').lower()
            for pintura in json_file:
                for valor in pintura.values():
                    if valor == resp:
                        print(f'CÓDIGO: {pintura["código"]}')
                        print(f'NOMBRE: {pintura["nombre"]}')
                        print(f'TIPO: {pintura["tipo"]}')
                        print(f'VALOR: {pintura["valor"]}')
                        print(f'STOCK: {pintura["stock"]}')
    elif resp == '3':
        cls()
        json_file = read_json(ruta_j)
        while True:
            pass
    elif resp == '4':
        cls()
        json_file = read_json(ruta_j)
        if len(json_file) == 0:
            print('Error: no hay registros')
        else:
            resp = input('Ingrese el código de la pintura a eliminar:\n').lower()
            for pintura in json_file:
                if str(pintura["código"]) == resp:
                    json_file.remove(pintura)
                    dump_json(json_file,ruta_j)
    elif resp == '5':
        cls()
        json_file = read_json(ruta_j)
        if len(json_file) == 0:
            print('Error: no hay registros')
        else:
            exportar(ruta_j)
    elif resp == '6':
        cls()
        exit('Gracias por usar el programa!')
    else:
        cls()
        print('Error: Respuesta invalida')