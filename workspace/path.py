from pathlib import Path

home = Path(__file__).parent

#Path(ruta/'carpeta1').mkdir()
#Path(ruta/'carpeta1'/'carpeta_linda').mkdir()

#name = input('Ingresa el nombre del directorio:\n')
#home = Path(ruta/name)

#print(home.exists())
#print(home.is_dir())

#ruta = Path(home/'archivo.py')
#if ruta.exists():
#    print('El archivo ya existe, no puede ser creado')
#else:
#    Path(home/'nuevo.py').touch()

rutas = ['carpeta1/archivo.txt',
         'carpeta2/archivo.docx',
         'carpeta3/archivo.json',
         'carpeta1/carpeta_linda/archivo.py',
         'carpeta1/carpeta_fea/archivo.html']

carpetas = ['carpeta1', 'carpeta2','carpeta3',
            'carpeta1/carpeta_linda',
            'carpeta1/carpeta_fea']

for carpeta in carpetas:
    if Path(home/carpeta).exists():
        print('La carpeta ya existe\n')
    else:
        Path(home/carpeta).mkdir()
        print(f'{carpeta} creado exitosamente\n')

for ruta in rutas:
    if Path(home/ruta).exists():
        print('El archivo ya existe\n')
    else:
        Path(home/ruta).touch()
        print('Archivo creado exitosamente\n')

#for item in home.iterdir():
#    print(item.name)
#    if item.is_dir():
#        for item2 in Path(home/item).iterdir():
#            print(f'\t{item2.name}')
#            if item2.is_dir():
#                for item3 in Path(home/item2).iterdir():
#                    print(f'\t\t{item3.name}')

#for item in Path(home).glob('**/*.*'):
#    print(item)

#for item in Path(home).glob('**/*.json'):
#    print(item)

