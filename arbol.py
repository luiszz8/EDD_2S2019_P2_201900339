import os


class nodoA:
    def __init__(self,carnet,nombre):
        self.carnet = carnet
        self.nombre = nombre
        self.izq = None
        self.der = None
        self.fe = 0

    #@property
    #def padre(self):
    #    return self._padre

    #@padre.setter
    #def padre(self, node):
    #    if node is not None:
    #        self._padre = node
    #        self.altura = self.padre.altura + 1
    #    else:
    #        self.altura = 0

class arbol:
    def __init__(self):
        self.raiz = None
        self.size = 0

    def obtenerFE(self,node):
        if(node is None):
            return -1
        else:
            return node.fe

    def insertarAVL(self, nuevo, sub):
        padre = sub
        if nuevo.carnet < sub.carnet:
            if sub.izq is None:
                sub.izq = nuevo
            else:
                sub.izq = self.insertarAVL(nuevo, sub.izq)
                if self.obtenerFE(sub.izq) - self.obtenerFE(sub.der) == 2:
                    if nuevo.carnet < sub.izq.carnet:
                        padre = self.rotate_left(sub)
                    else:
                        padre = self.double_rotate_left(sub)
        elif nuevo.carnet > sub.carnet:
            if sub.der is None:
                sub.der = nuevo
            else:
                sub.der = self.insertarAVL(nuevo, sub.der)
                if self.obtenerFE(sub.der) - self.obtenerFE(sub.izq) == 2:
                    if nuevo.carnet > sub.der.carnet:
                        padre = self.rotate_right(sub)
                    else:
                        padre = self.double_rotate_right(sub)
        if sub.izq is None and sub.der is not None:
            sub.fe = sub.der.fe + 1
        elif sub.izq is not None and sub.der is None:
            sub.fe = sub.izq.fe + 1
        else:
            if self.obtenerFE(sub.izq) > self.obtenerFE(sub.der):
                sub.fe = self.obtenerFE(sub.izq) + 1
            else:
                sub.fe = self.obtenerFE(sub.der) + 1
        return padre

    def insertar(self, carnet, nombre):
        nuevo = nodoA(carnet,nombre)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self.raiz = self.insertarAVL(nuevo, self.raiz)

    def rotate_left(self, node):
        aux = node.izq
        node.izq = aux.der
        aux.der = node
        if self.obtenerFE(node.izq) >= self.obtenerFE(node.der):
            node.fe = self.obtenerFE(node.izq) + 1
        else:
            node.fe = self.obtenerFE(node.der) + 1
        if self.obtenerFE(aux.izq) >= self.obtenerFE(aux.der):
            aux.fe = self.obtenerFE(aux.izq) + 1
        else:
            aux.fe = self.obtenerFE(aux.der) + 1
        return aux

    def rotate_right(self, node):
        aux = node.der
        node.der = aux.izq
        aux.izq = node
        if self.obtenerFE(node.izq) >= self.obtenerFE(node.der):
            node.fe = self.obtenerFE(node.izq) + 1
        else:
            node.fe = self.obtenerFE(node.der) + 1
        if self.obtenerFE(aux.izq) >= self.obtenerFE(aux.der):
            aux.fe = self.obtenerFE(aux.izq) + 1
        else:
            aux.fe = self.obtenerFE(aux.der) + 1
        return aux

    def double_rotate_left(self, node):
        node.izq = self.rotate_right(node.izq)
        temporal = self.rotate_left(node)
        return temporal

    def double_rotate_right(self, node):
        node.der = self.rotate_left(node.der)
        temporal = self.rotate_right(node)
        return temporal

    def empty(self):
        if self.raiz is None:
            return True
        return False

    def preShow(self, curr_node):
        if curr_node is not None:
            self.preShow(curr_node.izq)
            print(curr_node.carnet, end=" ")
            self.preShow(curr_node.der)

    def preorder(self, curr_node):
        if curr_node is not None:
            print(curr_node.carnet, end=" ")
            self.preorder(curr_node.izq)
            self.preorder(curr_node.der)

    def alturas(self, curr_node):
        while(curr_node.padre is not None):
            curr_node = curr_node.padre
            curr_node.altura = curr_node.altura + 1

    def graficar(self, curr_node):
        datos = ""
        if curr_node is not None:
            if curr_node.izq is not None:
                datos = datos + "\"" +str(curr_node.carnet) + curr_node.nombre + str(curr_node.fe) + "\""
                datos = datos + "->" + "\"" + str(curr_node.izq.carnet) + curr_node.izq.nombre + str(curr_node.izq.fe) + "\"" + ";"
            if curr_node.der is not None:
                datos = datos + "\"" + str(curr_node.carnet) + curr_node.nombre + str(curr_node.fe) + "\""
                datos = datos + "->" + "\"" + str(curr_node.der.carnet) + curr_node.der.nombre + str(curr_node.der.fe) + "\"" + ";"
            datos = datos + self.graficar(curr_node.izq)
            datos = datos + self.graficar(curr_node.der)
        return datos

    def grafo(self):
        datos = "digraph BST {"
        datos = datos + self.graficar(self.raiz)
        datos = datos +"}"
        f = open("otro.dot", "w")
        f.write(datos)
        f.close()
        os.system("dot -Tjpg otro.dot -o arbol.jpg")
        os.system("arbol.jpg")
