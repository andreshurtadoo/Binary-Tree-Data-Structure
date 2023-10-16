#Imports
from menu import menu
from controller import listarCatalogos
from controller import seleccionarProductos
from controller import hacerCompra
from controller import listarOrdenes
from controller import listarCarrito
#----------Arbol--------------------------------
from arbolDeCategoriaDeProductos import Arbol
from arbolDeCategoriaDeProductos import Categoria
from controllerArbol import cargarCategorias
from controllerArbol import mostrarCategorias
from controllerArbol import agregarCategoria
from controllerArbol import buscarCategoria
from controllerArbol import eliminarCategoria

#Intanciamos la clase Arbol
arbol = Arbol(Categoria('Root', 'Root', 1))

#----------Menu---------------------------------
opc = True
while(opc):
    try:
        opc = menu()
        #Conditional Estructure
        if opc == 1:
            listarCatalogos()

        elif opc == 2:
            seleccionarProductos()

        elif opc == 3:
            hacerCompra()

        elif opc == 4:
            listarOrdenes()

        elif opc == 5:
            listarCarrito()

        elif opc == 6:
            cargarCategorias(arbol)

        elif opc == 7:
            mostrarCategorias(arbol)

        elif opc == 8:
            agregarCategoria(arbol)

        elif opc == 9:
            buscarCategoria(arbol)

        elif opc == 10:
            eliminarCategoria(arbol)

        elif opc == 11:
            opc = False

    except ValueError:
        print('\nSolo datos numericos!')

#Fin del programa
print('\nPrograma Finalizado.')
