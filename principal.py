import csv
import hashlib
import json
import os
import socket
import select
import sys
import threading
import time
from bloque import bloque
from bloque import nodoB
from arbol import arbol
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
arbolT = arbol()
nodoTem = None
nodoReporte = None
def ser():
    while True:

        # maintains a list of possible input streams
        read_sockets = select.select([server], [], [], 1)[0]
        import msvcrt
        if msvcrt.kbhit(): read_sockets.append(sys.stdin)
        try:
            message = socks.recv(2048)
            print(message.decode('utf-8'))
        except:
            continue
        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
                print(message.decode('utf-8'))
                if message.decode('utf-8') != "true" and message.decode('utf-8') != "false":
                    if message.decode('utf-8') != "Welcome to [EDD]Blockchain Project":
                        jason = open("verj.json", "w")
                        jason.write(message.decode('utf-8'))
                        jason.close()
                        with open("verj.json") as enviado:
                            datosE = json.load(enviado)
                            # print(datosE['index'])
                            print(datosE)
                            h = hashlib.sha256()
                            cadenahash = json.dumps(datosE['data']).replace(" ", "")
                            cadenahash = cadenahash.replace("\n", "")
                            h.update((json.dumps(datosE['index']).replace("\"", "") + json.dumps(datosE['timestamp']).replace("\"", "") + json.dumps(datosE['class']).replace("\"", "") + cadenahash + json.dumps(datosE['previoushash']).replace("\"", "")).encode('utf-8'))
                            if h.hexdigest() == json.dumps(datosE['hash']).replace("\"", ""):
                                server.sendall(("true").encode('utf-8'))
                            else:
                                server.sendall(("false").encode('utf-8'))
                            au = aux(arbolT)
                            au.recorrer(datosE)
                            nodoTem = nodoB(datosE['index'], json.dumps(datosE['timestamp']).replace("\"", ""),
                                  json.dumps(datosE['class']).replace("\"", ""), arbolT, cadenahash,
                                  json.dumps(datosE['previoushash']).replace("\"", ""),
                                  json.dumps(datosE['hash']).replace("\"", ""))
                elif message.decode('utf-8') == "true":
                    lista.agregarFinal(nodoTem)

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
#start_new_thread(ser(), )
hilo = threading.Thread(target = ser)
hilo.setDaemon(True)
hilo.start()
#hilo.join()
while menu < 4:
    #print(hilo.isAlive())
    print("1. INSERTAR BLOQUE")
    print("2. SELECCIONAR BLOQUE")
    print("3. REPORTES")

    #try:
    if True:
        menu = int(input())
        if menu == 1:
            nombre = ""
            data = ""
            auxT = ""
            print("Ingrese nombre archivo")
            archivo = input()
            archivo = "bloques/" + archivo
            with open(archivo + '.csv') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == "class":
                        nombre = row[1]
                    if row[0] == "data":
                        auxT = row[1]
                j = open(nombre + ".json", "w")
                j.write(auxT)
                j.close()
                ar = arbol()
                datosj = ""
                auxT = auxT.replace(" ", "")
                auxT = auxT.replace("\n", "")
                with open(nombre + ".json") as contenido:
                    datos = json.load(contenido)
                    cadena = json.dumps(datos).replace(" ", "")
                    cadena = cadena.replace('\n', "")
                    fincadena = cadena
                    # m = hashlib.sha256()
                    # m.update(cadena.encode('utf-8'))
                    # p = open("prueba.txt", "w")
                    # p.write(cadena)
                    # p.close()
                    datosj = datos
                    # au = aux(ar)
                    # au.recorrer(datos)

                    data = data + "{"
                    data = data + "\"index\":" + str(lista.tamayo) + ","
                    data = data + "\"timestamp\":" + "\"" + time.strftime("%d") + "-" + time.strftime(
                        "%m") + "-" + time.strftime("%y") + "-::" + time.strftime("%X") + "\","
                    data = data + "\"class\":" + "\"" + nombre + "\","
                    data = data + "\"data\":" + auxT + ","
                    hashanterior = ""
                    if lista.fin is not None:
                        data = data + "\"previoushash\":" + "\"" + lista.fin.mhash + "\","
                        hashanterior = lista.fin.mhash
                    else:
                        data = data + "\"previoushash\":" + "\"" + "0000" + "\","
                        hashanterior = "0000"
                    m = hashlib.sha256()
                    m.update((str(index) + time.strftime("%d") + "-" + time.strftime("%m") + "-" + time.strftime(
                        "%y") + "-::" + time.strftime("%X") + nombre + auxT + hashanterior).encode('utf-8'))
                    data = data + "\"hash\":" + "\"" + m.hexdigest() + "\"}"
                    server.sendall(data.encode('utf-8'))
                    # prueba
                    jason = open("verj.json", "w")
                    jason.write(data)
                    jason.close()
                    with open("verj.json") as enviado:
                        datosE = json.load(enviado)
                        # print(datosE['index'])
                        #print(datosE)
                        h = hashlib.sha256()
                        cadenahash = json.dumps(datosE['data']).replace(" ", "")
                        cadenahash = cadenahash.replace("\n", "")
                        h.update((json.dumps(datosE['index']).replace("\"", "") + json.dumps(datosE['timestamp']).replace("\"", "") + json.dumps(datosE['class']).replace("\"","") + cadenahash + json.dumps(datosE['previoushash']).replace("\"", "")).encode('utf-8'))
                        # print(json.dumps(datosE['index']).replace("\"","")+json.dumps(datosE['timestamp']).replace("\"","")+json.dumps(datosE['class']).replace("\"","")+cadenahash+json.dumps(datosE['previoushash']).replace("\"",""))
                        # print(h.hexdigest())
                        index = index + 1
                        au = aux(ar)
                        au.recorrer(datos)
                        lista.agregarFinal(nodoB(datosE['index'], json.dumps(datosE['timestamp']).replace("\"", ""),
                                                 json.dumps(datosE['class']).replace("\"", ""), ar, cadenahash,
                                                 json.dumps(datosE['previoushash']).replace("\"", ""),
                                                 json.dumps(datosE['hash']).replace("\"", "")))
                        """lista.agregarFinal(nodoB(1, json.dumps(datosE['timestamp']).replace("\"", ""),
                                                 json.dumps(datosE['class']).replace("\"", ""), ar, cadenahash,
                                                 json.dumps(datosE['previoushash']).replace("\"", ""),
                                                 json.dumps(datosE['hash']).replace("\"", "")))"""
                        #print(h.hexdigest())
                        #print(json.dumps(datosE['hash']).replace("\"", ""))
                        if h.hexdigest() == json.dumps(datosE['hash']).replace("\"", ""):
                            #print("si entra")
                            server.sendall("true".encode('utf-8'))
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

                    # lista.agregarFinal(nodoB(index, nombre, ar, data))
        if menu == 2:
            if lista.inicio is not None:
                os.system("cls")
                nodoCambiante = lista.inicio
                letra = "f"
                while letra is not "s":
                    print(nodoCambiante.index)
                    print(nodoCambiante.timet)
                    print(nodoCambiante.clase)
                    print(nodoCambiante.datos[0:50])
                    print(nodoCambiante.phash)
                    print(nodoCambiante.mhash)
                    letra = input()
                    if letra is "a":
                        if nodoCambiante.ant is not None:
                            nodoCambiante = nodoCambiante.ant
                    if letra is "d":
                        if nodoCambiante.sig is not None:
                            nodoCambiante = nodoCambiante.sig
                    if letra is "w":
                        nodoReporte = nodoCambiante.data
                    os.system("cls")
        if menu == 3:
            submenu = 1
            while submenu < 6:
                print("1. BLOCKCHAIN REPORT")
                print("2. ARBOL")
                print("3. Preorden")
                print("4. Posorden")
                print("5. Inorden")
                submenu = int(input())
                if submenu == 1:
                    lista.graficar()
                if submenu == 2:
                    nodoReporte.grafo()
                if submenu == 3:
                    nodoReporte.grafoPre()
    #except:
        #continue
