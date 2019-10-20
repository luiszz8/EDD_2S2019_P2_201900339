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

    def agregarFinal(self, node):
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
