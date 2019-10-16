import csv
import json

from bloque import bloque
from bloque import nodoB
from arbol import arbol


class aux:
    def __init__(self, arbol):
        self.arbol = arbol

    def recorrer(self, datos):
        if datos is not None:
            self.recorrer(datos['left'])
            self.arbol.insertar(datos['value'].split("-")[0], datos['value'].split("-")[1])
            self.recorrer(datos['right'])

menu = 0
index = 0
lista = bloque()
while menu < 4:
    print("1. INSERTAR BLOQUE")
    print("2. SELECCIONAR BLOQUE")
    print("3. REPORTES")
    menu = int(input())
    if menu == 1:
        nombre = ""
        data = ""
        with open('datos.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "class":
                    nombre = row[1]
                if row[0] == "data":
                   data = row[1]
            j = open(nombre+".json", "w")
            j.write(data)
            j.close()
            ar = arbol()
            datosj = ""
            with open(nombre+".json") as contenido:
                datos = json.load(contenido)
                datosj = datos
                au = aux(ar)
                au.recorrer(datos)

            lista.agregarFinal(nodoB(index, nombre, ar, data))

