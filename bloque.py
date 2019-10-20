import os
import time
import hashlib

class nodoB:
    def __init__(self, index, timet, clase, data, datos, phash, mhash):
        self.index = index
        self.timet = timet
        self.clase = clase
        self.data = data
        self.datos = datos
        self.phash = phash
        self.mhash = mhash
        self.sig = None
        self.ant = None

class bloque:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamayo = 0

    def agregarFinal(self, node):
        self.tamayo = self.tamayo + 1
        if self.fin is None:
            #node.phash = "0000"
            #m = hashlib.sha256()
            #m.update((str(node.index)+node.timet+node.clase+node.datos+node.phash).encode('utf-8'))
            #node.mhash = m.hexdigest()
            self.fin = node
            self.inicio = node
        else:
            #m = hashlib.sha256()
            #node.phash = node.ant.mhash
            #m.update((str(node.index) + node.timet + node.clase + node.datos + node.phash).encode('utf-8'))
            #node.mhash = m.hexdigest()
            self.fin.sig = node
            node.ant = self.fin
            self.fin = node

    def graficar(self):
        pun1=0
        pun2=1
        actual = self.inicio
        datos = "digraph G {\n"
        datos = datos + "node[shape = record, width = 2.3, height = 0.6];\n"
        datos = datos + "rankdir = LR;\n"
        while actual is not None:
            datos = datos + "nodo" +str(pun1) + "[label=\" Class=" +actual.clase + "\n TimeStamp="+actual.timet + "\n PreviousHash=" + actual.phash + "Hash=" +actual.mhash+"\"];\n"
            if actual is self.fin:
                break
            if actual.sig is not None:
                datos = datos + "nodo" +str(pun1) + "->nodo"+str(pun2) + "\n"
                datos = datos + "nodo" + str(pun2) + "->nodo" + str(pun1) + "\n"
                pun1 = pun1 + 1
                pun2 = pun2 + 1
            actual = actual.sig
        #datos = datos + "nodof [label=\" null  \"];\n"
        #datos = datos + "nodo" + str(pun1) + "->nodof \n"
        #datos = datos + "nodoi [label=\" null  \"];\n"
        #datos = datos + "nodoi ->nodo0 \n"
        datos = datos + "}"
        f = open("otro.dot", "w")
        f.write(datos)
        f.close()
        os.system("dot -Tjpg otro.dot -o block.jpg")
        os.system("block.jpg")