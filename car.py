#Modula carrito

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

#Clase carrito
class Car:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def __len__(self):
        return self.longitud

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.valor
            actual = actual.siguiente

    #Añadir productos a la lista enlazada (Pila)
    def add(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1

    #Eliminar producto de la lista por su nombre
    def delete(self, valor):
        if self.cabeza is None:
            return False

        if self.cabeza.valor.name == valor:
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return True
        actual = self.cabeza

        while actual.siguiente:
            if actual.siguiente.valor.name == valor:
                actual.siguiente = actual.siguiente.siguiente
                self.longitud -= 1
                return True
            actual = actual.siguiente
        return False

    #Calcular el total de la compra
    def calculate(self):
        actual = self.cabeza
        sum = 0
        for i in range(0, self.longitud):
            sum += actual.valor.price
            actual = actual.siguiente
        return sum

    #Listar los productos del carrito
    def list(self):
        actual = self.cabeza
        list = []
        for i in range(0, self.longitud):
            list.append(actual.valor)
            actual = actual.siguiente
        return list

#Instaciamos la clase Car
carrito = Car()




