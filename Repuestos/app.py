from modulos_app.construcción import enumerar_lista, solicitar_acción, verificar_ingreso, verificar_tipo, verificar_num
from modulos_app.f_data import cabezera, crear_ruta_home, verificar_existencia_archivo_j, verificar_archivo_j_vacio, read_j, dump_j, actualizar_codigo, verificar_existencia_archivo_csv, exportar
from modulos_app.construcción import limpiar_pantalla as cls
from pathlib import Path
import json

home = crear_ruta_home()

ruta_j = verificar_existencia_archivo_j(home)

verificar_archivo_j_vacio(ruta_j)

menup = ['Ver Listado de Repuestos',
         'Buscar Repuestos',
         'Agregar Repuestos',
         'Eliminar Repuestos',
         'Exportar Repuestos']

data = {'código':'',
        'nombre':'',
        'marca':'',
        'modelo':'',
        'tipo':'',
        'valor':'',
        'stock':''}

while True:
    cabezera()
    enumerar_lista(menup)
    resp = solicitar_acción()
    if resp == '1':
        cls()
        base_de_datos = read_j(ruta_j)
        if len(base_de_datos) == 0:
            cls()
            print('Error: la base de datos no tiene contenido todavia\n')
        else:
            for repuesto in base_de_datos:
                print(f'\nCÓDIGO: {repuesto["código"]}')
                print(f'NOMBRE: {repuesto["nombre"]}\n')
    elif resp == '2':
        cls()
        base_de_datos = read_j(ruta_j)
        if len(base_de_datos) == 0:
            print('Error: la base de datos no tiene contenido todavia\n')
        else:
            resp = input('¿Que repuesto desea buscar?:\n(Puede buscar por código, nombre, marca, modelo o por tipo.)\n').lower()
            for repuesto in base_de_datos:
                if resp == str(repuesto['código']) or \
                resp == repuesto['nombre'].lower() or \
                resp == repuesto['marca'].lower() or \
                resp == repuesto['modelo'].lower() or \
                resp == repuesto['tipo'].lower():
                    print(f'CÓDIGO: {repuesto["código"]}')
                    print(f'NOMBRE: {repuesto["nombre"]}')
                    print(f'MARCA: {repuesto["marca"]}')
                    print(f'MODELO: {repuesto["modelo"]}')
                    print(f'TIPO: {repuesto["tipo"]}')
                    print(f'VALOR: {repuesto["valor"]}')
                    print(f'STOCK: {repuesto["stock"]}\n')
    elif resp == '3':
        cls()
        base_de_datos = read_j(ruta_j)
        while True:
            found = 0
            nombre = verificar_ingreso('el','nombre')
            for repuesto in base_de_datos:
                if repuesto["nombre"] == nombre:
                    cls()
                    print('Error: el nombre ingresado ya esta en la base de datos, intente de nuevo.\n')
                    found = 1
            if found == 0:
                break
        marca = verificar_ingreso('la', 'marca')
        modelo = verificar_ingreso('el','modelo')
        tipo = verificar_tipo()
        valor = verificar_num('valor')
        stock = verificar_num('stock')

        data.update({"nombre":nombre})
        data.update({"marca":marca})
        data.update({"modelo":modelo})
        data.update({"tipo":tipo})
        data.update({"valor":valor})
        data.update({"stock":stock})

        base_de_datos.append(data)

        actualizar_codigo(base_de_datos)
        dump_j(base_de_datos, ruta_j)
    elif resp == '4':
        cls()
        base_de_datos = read_j(ruta_j)
        if len(base_de_datos) == 0:
            print('Error: la base de datos no tiene contenido todavia\n')
        else:
            try:
                resp = int(input('Ingrese el código del producto que desea eliminar:\n'))
            except:
                print('Error: entrada invalida.\nSolo números.\n')
            eliminado = False
            for repuesto in base_de_datos[:]:
                if 'código' in repuesto and repuesto['código'] == resp:
                    base_de_datos.remove(repuesto)
                    eliminado = True
            
            if eliminado:
                actualizar_codigo(base_de_datos)
                dump_j(base_de_datos, ruta_j)
                print(f"Producto con código '{resp}' eliminado correctamente.\n")
            else:
                print(f"No se encontró ningún producto con código '{resp}'.\n")
    elif resp == '5':
        cls()
        ruta_c = verificar_existencia_archivo_csv(home)
        exportar(ruta_j, ruta_c)
    else:
        cls()
        print('Error: su respuesta no es valida\n')