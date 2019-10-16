class nodoAN:
    def __init__(self,carnet,nombre,padre):
        self.carnet = carnet
        self.nombre = nombre
        self.izq = None
        self.der = None
        self.padre = padre

class arbolNormal:
    def __init__(self):
        self.raiz = None
        self.size = 0

    def empty(self):
        if self.raiz is None:
            return True
        return False

    def insert(self, carnet, nombre):
        # Creamos un nuevo nodo
        new_node = nodoAN(carnet,nombre, None)
        # Si el árbol esta vacio
        if self.empty():
            self.raiz = new_node
        else:
            # Si el árbol no esta vacio
            curr_node = self.raiz
            while curr_node is not None:
                parent_node = curr_node
                if new_node.carnet < curr_node.carnet:
                    curr_node = curr_node.izq
                else:
                    curr_node = curr_node.der
            if new_node.carnet < parent_node.carnet:
                parent_node.izq = new_node
            else:
                parent_node.der = new_node
            new_node.padre = parent_node


    def insertarP(self,carnet,nombre):
        if self.raiz is None:
            self.raiz = nodoAN(carnet,nombre)
        else:
            self.insertar(self.raiz,carnet,nombre)

    def insertar(self,nodoR,carnet,nombre):
        if nodoR is None:
            nodoR = nodoAN(carnet,nombre)
        else:
            if carnet < nodoR.carnet:
                self.insertar(nodoR.izq, carnet, nombre)
            else:
                self.insertar(nodoR.der, carnet, nombre)

    def preorder(self, curr_node):
        if curr_node is not None:
            print(curr_node.carnet, end=" ")
            self.preorder(curr_node.izq)
            self.preorder(curr_node.der)

t = arbolNormal()
t.insert(5, "luis")
t.insert(3, "luis")
t.insert(2, "luis")
t.insert(4, "luis")
t.insert(10, "luis")
t.preorder(t.raiz)