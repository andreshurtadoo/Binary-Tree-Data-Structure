#Modulo - Ordenes

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

#Clase Orden con lista enlazada (Cola)
class Order:
    def __init__(self):
        self.frente = None
        self.fin = None

    #Verificar si la lista esta vacia
    def esta_vacia(self):
        return self.frente is None

    #Agragar a la lista
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nodo_nuevo
        else:
            self.fin.siguiente = nodo_nuevo
        self.fin = nodo_nuevo

    #Recorrer la lista
    def recorrer(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            self._recorrer_aux(self.frente)

    #Imprime el resultado de Recorrer
    def _recorrer_aux(self, nodo):
        if nodo is not None:
            #print(nodo.valor)
            for i in nodo.valor:
                print(i.name, i.price)
            print(' ')
            self._recorrer_aux(nodo.siguiente)

#Instanciamos la clase Order
facturas = Order()
