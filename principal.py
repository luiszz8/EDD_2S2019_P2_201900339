import csv
import hashlib
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
#hilo.join()
while menu < 4:
    print("1. INSERTAR BLOQUE")
    print("2. SELECCIONAR BLOQUE")
    print("3. REPORTES")
    menu = int(input())
    if menu == 1:
        nombre = ""
        data = ""
        auxT = ""
        with open('datos.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "class":
                    nombre = row[1]
                if row[0] == "data":
                   auxT = row[1]
            j = open(nombre + ".json", "w")
            j.write(auxT)
            j.close()
            # ar = arbol()
            datosj = ""
            auxT = auxT.replace(" ","")
            auxT = auxT.replace("\n", "")
            with open(nombre + ".json") as contenido:
                datos = json.load(contenido)
                cadena = json.dumps(datos).replace(" ", "")
                cadena = cadena.replace('\n', "")
                fincadena = cadena
                #m = hashlib.sha256()
                #m.update(cadena.encode('utf-8'))
                #p = open("prueba.txt", "w")
                #p.write(cadena)
                #p.close()
                datosj = datos
                #au = aux(ar)
                #au.recorrer(datos)


                data = data + "{"
                data = data + "\"\"index\"\":" + str(index) + ","
                data = data + "\"\"timestamp\"\":" + "\"\"" + time.strftime("%d") + "-" + time.strftime("%m") + "-" +time.strftime("%y") + "-::" + time.strftime("%X") + "\"\","
                data = data + "\"\"class\"\":" + "\"\"" + nombre + "\"\","
                data = data + "\"\"data\"\":" + auxT + ","
                hashanterior = ""
                if lista.fin is not None:
                    data = data + "\"\"previoushash\"\":" + "\"\"" + lista.fin.mhash + "\"\","
                    hashanterior = lista.fin.mhash
                else:
                    data = data + "\"\"previoushash\"\":" + "\"\"" + "0000" + "\"\","
                    hashanterior = "0000"
                m = hashlib.sha256()
                m.update((str(index) + time.strftime("%d") + "-" + time.strftime("%m") + "-" +time.strftime("%y") + "-::" + time.strftime("%X") + nombre + auxT + hashanterior).encode('utf-8'))
                data = data + "\"\"hash\"\":" + "\"\"" + m.hexdigest() + "\"\"}"
                server.sendall(data.encode('utf-8'))
                """j = open(nombre+".json", "w")
                j.write(data)
                j.close()
                #ar = arbol()
                datosj = ""
                with open(nombre+".json") as contenido:
                    datos = json.load(contenido)
                    cadena = json.dumps(datos).replace(" ", "")
                    cadena = cadena.replace('\n', "")
                    m = hashlib.sha256()
                    m.update(cadena.encode('utf-8'))
                    print(m.hexdigest())
                    p = open("prueba.txt", "w")
                    p.write(cadena)
                    p.close()
                    datosj = datos
                    au = aux(ar)
                    au.recorrer(datos)"""

                #lista.agregarFinal(nodoB(index, nombre, ar, data))
