from pathlib import Path
import json
import csv
import os

def ruta_home():
    home = Path(__file__).parent.parent
    return home

def ruta_json(home: Path):
    while True:
        if not Path(home/'data.json').exists():
            Path(home/'data.json').touch()
        else:
            ruta_j = Path(home/'data.json')
            return ruta_j

def ruta_csv(home: Path):
    while True:
        if not Path(home/'export.csv').exists():
            Path(home/'export.csv').touch()
        else:
            Path(home/'export.csv').unlink()
            Path(home/'export.csv').touch()
            ruta_csv = Path(home/'export.csv')
            return ruta_csv

def empty_json(ruta_j: Path):
    while True:
        if Path(ruta_j).stat().st_size == 0:
            with open(ruta_j,mode='w') as open_file:
                file_j = []
                save = json.dump(file_j, open_file)
        else: return True

def read_json(ruta_j: Path):
    with open(ruta_j,mode='r') as open_file:
        file_j = json.load(open_file)
        return file_j

def dump_json(base_de_datos: list, ruta_j: Path):
    with open(ruta_j,mode='w') as open_file:
        save = json.dump(base_de_datos,open_file)

def cls():
    os.system('cls')

def exportar(ruta_j:Path):
    json_file = read_json(ruta_j)
    for pintura in json_file:
        line = [pintura["código"],
                pintura["nombre"],
                pintura["tipo"],
                pintura["valor"],
                pintura["stock"]]
        with open(ruta_csv(ruta_home),mode='a',newline='') as open_file:
            whiter = csv.writer(open_file)
            whiter.writerow(line)