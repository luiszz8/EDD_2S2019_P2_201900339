import csv
import json
import socket
import select
import sys
import threading
import time
from bloque import bloque
from bloque import nodoB
from arbol import arbol

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

def ser():
    while True:

        # maintains a list of possible input streams
        read_sockets = select.select([server], [], [], 1)[0]
        import msvcrt
        if msvcrt.kbhit(): read_sockets.append(sys.stdin)

        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
                print (message.decode('utf-8'))
            else:
                message = sys.stdin.readline()
                server.sendall(message.encode('utf-8'))
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()

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
hilo = threading.Thread(target = ser)
hilo.setDaemon(False)
hilo.start()
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

            lista.agrega4rFinal(nodoB(index, nombre, ar, data))
