#Controlador de arbol
from arbolDeCategoriaDeProductos import Categoria
from product import catalogo

def cargarCategorias(arbol):
    #Creamos n categorias del tipo de la clase Categoria
    electronica = Categoria('Electronica', 'Televisores', 1)
    hogar = Categoria('Hogar', 'Baño y Cocina', 1)
    papeleria = Categoria('Papeleria', 'Cuadernos', 1)
    textil = Categoria('Textil', 'Damas', 1)
    jardineria = Categoria('Jardineria', 'Podadoras', 1)
    construccion = Categoria('Construccion', 'Materiales', 1)
    pintura = Categoria('Pintura', 'Brillo de seda', 1)
    coche = Categoria('Coche', 'Repuestos y Cauchos', 0)

    #Las agregamos al arbol como nodos
    arbol.agregar(electronica)
    arbol.agregar(hogar)
    arbol.agregar(papeleria)
    arbol.agregar(textil)
    arbol.agregar(jardineria)
    arbol.agregar(construccion)
    arbol.agregar(pintura)
    arbol.agregar(coche)

    print('\nCategorias Cargadas Exitosamente!')

def mostrarCategorias(arbol):
    #Mostramos todas las categorias por su nombre
    #Recorremos los nodos de las 3 maneras
    print('\nMostrando Categorias')
    arbol.inorden()
    arbol.preorden()
    arbol.postorden()
    return

def agregarCategoria(arbol):
    #Creamos una categoria de la clase Categoria
    #Agreamos el nodo al arbol
    band = True
    name = input('\nIngrese el nombre de la categoria: ')
    desc = input('Ingrese la descripcion de la categoria: ')
    while(band):
        try:
            status = int(input('Ingrese el status de la categoria 0-1: '))
            if status == 0 or status == 1:
                band = False
            else:print('Solo puede ser 0 o 1')
        except ValueError:
            print('Solo numeros!')
    arbol.agregar(Categoria(name, desc, status))
    print('Categoria Creada Exitosamente!')
    return

def buscarCategoria(arbol):
    #Indicamos el nombre de la categoria
    busqueda = input("\nIndique el nombre de la categoria: ")
    #Hacemos la busqueda
    nodo = arbol.buscar(busqueda)
    #En caso de que no halla nodo..
    if nodo is None:
        return print(busqueda, "no existe")
    #En caso de que si exista y su status sea 1
    if nodo.dato.status == 1:
        print(busqueda, "sí existe")
        print('Esta es su subCategoria:', nodo.dato.description)

        #BUSCADO TODOS LOS PRUDUCTOS CON ESTA CATEGORIA
        print('Estos son sus productos: ')
        buscarProductosConCategoria(busqueda)

        #ASIGNAMOS ESTA CATEGORIA A LOS PRODUCTOS QUE QUERAMOS
        cambio = input('Quieres asignarle esta categoria algun producto - si o no: ')
        if(cambio == 'si' or cambio == 'SI'):
            asignarCategoria(busqueda)
        else: return
    #En caso de que exista y su estatus sea 0
    else:
        return print(busqueda, "no existe")

def eliminarCategoria(arbol):
    #Queremos saber si exite el producto que se va a eliminar
    busqueda = input('\nIndique el nombre de la categoria que desea eliminar: ')
    nodo = arbol.buscar(busqueda)
    if nodo is None:
        return print(busqueda, "no existe")
    else:
        nodo.dato.status = 0
        return print('Categoria eliminada exitosamente!')

def asignarCategoria(busqueda):
    band = True
    j = 1
    print('\n-------------ASIGNANDO CATEGORIAS---------------------')
    print('Seleccione un producto para asignarle una categoria: ')
    for i in catalogo.list():
        print('{0}- {1:10} Categoria: {2}'.format(j, i.name, i.categoria))
        j += 1

    #Asignar
    while (band):
        try:
            #OJO solo numero que pertenezcan a la lista
            opc = int(input('\nPulse 0 para terminar \nIndique el Id del producto asignar: '))
            if opc == 0:
                band = False
            else:
                catalogo.obtener(opc - 1).categoria = busqueda

        except ValueError:
            print('Opcion Erronea!!')

def buscarProductosConCategoria(busqueda):
    j = 1
    for i in catalogo.list():
        if i.categoria == busqueda:
            print('{0}- {1:10} Categoria: {2}'.format(j, i.name, i.categoria))
        j += 1
