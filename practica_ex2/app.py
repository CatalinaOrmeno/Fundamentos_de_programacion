'''
1. Modificar estructura de datos:
   - Cambia `data` para que tenga nombres de productos en lugar de años.
   - Añade una segunda lista para cantidades de inventario.

2. Actualizar funciones:
   - **`poblar`:** Llena la segunda lista con cantidades de productos aleatorias.
   - **`mostrar_clasificación`:** Imprime productos y sus cantidades.
   - **`clasificar`:** Ajusta los parámetros para clasificar productos por cantidad (baja, media, alta).
   - **`estadistica`:** Calcula y muestra estadísticas de las cantidades de productos.
   - **`exportar`:** Exporta inventario y estadísticas a un archivo.

3. Actualizar menú:
   - Asegúrate de que las opciones del menú reflejen las acciones relacionadas con el inventario de productos.

4. Pruebas:
   - Revisa y prueba el código para asegurar su correcto funcionamiento en el nuevo contexto.
'''
from modules.opciones import poblar
menup = ['Poblar Inventario',
         'Clasificar Inventario',
         'Mostrar Estadísticas',
         'Exportar Inventario',
         'Salir']

data = [['Leche',
         'Manzanas',
         'Naranjas',
         'Plátanos',
         'Uvas',
         'Peras',
         'Kiwis',
         'Fresas',
         'Mangos',
         'Piñas',
         'Sandías'],
         []]

while True:
    for ind, opc in enumerate(menup):
        print(f'{ind+1}. {opc}')
    resp = input('¿Que deseas hacer?: ')
    if resp == '1':
        poblar(data)
    elif resp == '2':
        pass
    elif resp == '3':
        pass
    elif resp == '4':
        pass
    elif resp == '5':
        exit('Gracias por ocupar el programa!')
    else:
        print('Error: respuesta no valida')