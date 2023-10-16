#Modulo - Arbol de categoria de productos

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato.name < nodo.dato.name:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            if nodo.dato.status == 1:
                print(nodo.dato.name, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            if nodo.dato.status == 1:
                print(nodo.dato.name, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            if nodo.dato.status == 1:
                print(nodo.dato.name, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato.name == busqueda:
            return nodo
        if busqueda < nodo.dato.name:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    def __eliminar(self, nodo, label):
        if nodo is None:
            return None
        else:
            pass


    #Funciones públicas
    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("______Imprimiendo árbol inorden: ______")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("______Imprimiendo árbol preorden: ______")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("______Imprimiendo árbol postorden: ______")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)

    def eliminar(self, label):
        return self.__eliminar(self.raiz, label)

class Categoria:
    #Constructor
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status
    #Methods
    #---Obtener nombre
    def getName(self):
        return self.nombre
    #---Obtener descripcion
    def getDescription(self):
        return self.description






