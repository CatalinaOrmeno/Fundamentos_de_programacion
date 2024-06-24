from modulos_app.construcción import enumerar_lista, solicitar_acción
from modulos_app.f_data import cabezera
from modulos_app.construcción import limpiar_pantalla as cls

menup = ['Ver Listado de Repuestos',
         'Buscar Repuestos',
         'Agregar Repuestos',
         'Eliminar Repuestos',
         'Exportar Repuestos']

while True:
    cabezera()
    enumerar_lista(menup)
    resp = solicitar_acción()
    if resp == '1':
        pass
    elif resp == '2':
        pass
    elif resp == '3':
        pass
    elif resp == '4':
        pass
    elif resp == '5':
        pass
    else:
        cls()
        print('Error: su respuesta no es valida')