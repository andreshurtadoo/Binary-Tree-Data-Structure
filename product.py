#Imports

#Controllers
class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

#Clase productos
class Product:
    #Constructor
    def __init__(self, name,desc,price,status,stock,create,update,categoria):
        self.name = name
        self.description = desc
        self.price = price
        self.status = status
        self.stock = stock
        self.data_create = create
        self.data_update = update
        self.categoria = categoria

    #Update stock => OJO dismiss stock when do a purchase
    def update(self, new_stock):
        self.stock = new_stock

    #Show details
    def details(self):
        #print(self.name , self.price, self.stock)
        return self.name

#Clase productos con option
class PruductWithOptions(Product):
    #Attributes
    option = dict

    #Constructor
    def __init__(self, name,desc,price,status,stock,create,update,categoria,option):
        super().__init__(name,desc,price,status,stock,create,update,categoria)
        self.option = option

    #Methods
    #Show Available Options
    def availableOptions(self):
        print(self.option)

#Lista enlazada donde se almacenan los productos (Pila)
class ListaEnlazada:
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

    #Add node to the list
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1

    #Delete node to the list
    def eliminar(self, valor):
        if self.cabeza is None:
            return False

        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return True
        actual = self.cabeza

        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                self.longitud -= 1
                return True
            actual = actual.siguiente
        return False

    #Insert node to an expecifict position to the list
    def insertar(self, indice, valor):
        if indice < 0 or indice > self.longitud:
            raise IndexError("Índice fuera de rango")
        nuevo_nodo = Nodo(valor)

        if indice == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for i in range(indice - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1

    #Get node to the list
    def obtener(self, indice):
        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for i in range(indice):
            actual = actual.siguiente
        return actual.valor

    #Get the index of the any node
    def index(self, valor):
        actual = self.cabeza
        indice = 0
        while actual:
            if actual.valor == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        raise ValueError("{} no está en la lista".format(valor))

    #Delete any node to the list
    def pop(self, indice=None):
        if indice is None:
            indice = self.longitud - 1

        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")

        if indice == 0:
            valor = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return valor
        actual = self.cabeza

        for i in range(indice - 1):
            actual = actual.siguiente

        valor = actual.siguiente.valor
        actual.siguiente = actual.siguiente.siguiente
        self.longitud -= 1
        return valor

    #Liting all the product with status is active and stock > 0
    def list(self):
        actual = self.cabeza
        list = []
        listOption = []
        for i in range(0, self.longitud):
            if (actual.valor.status == "activo" and actual.valor.stock > 0):
                list.append(actual.valor)
                listOption.append(actual.valor.option)
            actual = actual.siguiente
        return list

#Ejemplo de uso:
#Creamos algunos objetos de la clase Product
product1 = PruductWithOptions("Harina", "Pan", 10, "activo", 20, "4/14/23", "5/14/23","Alimentos", {'color':'rojo'})
product2 = PruductWithOptions("Arroz", "Mary", 20, "activo", 30, "4/14/23", "5/14/23","Alimentos", {'color':'azul'})
product3 = PruductWithOptions("Pasta", "Larga", 30, "activo", 40, "4/14/23", "5/14/23","Alimentos", {'color':'morado'})
product4 = PruductWithOptions("Leche", "Liquida", 40, "activo", 50, "4/14/23", "5/14/23","Alimentos", {'color':'blanco'})

#Creamos la lista enlazada y agregamos algunos productos
catalogo = ListaEnlazada()
catalogo.agregar(product1)
catalogo.agregar(product2)
catalogo.agregar(product3)
catalogo.agregar(product4)







