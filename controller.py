#Modulo - Controllers
from product import catalogo
from car import carrito
from order import facturas

#Listar catalogos de productos cuyo status sea activo y stock sea mayor que cero
def listarCatalogos():
    print('\nCatalogo de productos disponibles:')
    for i in catalogo.list():
        #print('Producto: {0:10}  Opciones: {1}'.format(i.name, i.option))
        print('Producto: {0:10}  Categoria: {1}'.format(i.name, i.categoria))

#Seleccionar productos y añadirlo al carrito de compras.
def seleccionarProductos():
    band = True
    j = 1
    #Mostramos el catalogo de productos con su Id, nombre y precio
    print('\nSeleccione el producto que quiere añadir al carrito: ')
    for i in catalogo.list():
        print('{0}- {1:10} Precio: {2}'.format(j, i.name, i.price))
        j += 1

    #Agregar al carrito el producto indicado por el usuario
    while(band):
       try:
           opc = int(input('\nPulse 0 para terminar \nIndique el Id del producto que quiere agregar: '))
           if opc == 0: band = False
           else:
               #Con el metodo "obtener" sacamos el nodo en el idice indicado
               carrito.add(catalogo.obtener(opc - 1))
               print('Producto Añadido al carrito!!')

       except ValueError:
           print('Opcion Erronea!!')

#Hacer una compra con los productos agregados al carrito.
def hacerCompra():
    #Mostrar el total de la compra y los productos que hay en el carrito
    print('\nTotal de la compra: ', carrito.calculate())

    #Generar una factura
    facturas.agregar(carrito.list())

    #Al terminar la compra vaciar el carrito!!!!
    for i in carrito.list():
        carrito.delete(i.name)

#Listar ordenes creadas junto con respectivos datos y productos.
def listarOrdenes():
    #Mostrar las facturas creadas
    print('\nOrdenes creadas')
    facturas.recorrer()

#Listar productos del carrito actual
def listarCarrito():
    if(len(carrito.list()) == 0):
        return print('\nNo hay productos en el carrito!')

    print('\nProductos dentro del carrito:')
    for i in carrito.list():
        print('{0:10} Precio: {1}'.format(i.name, i.price))

    print('Total: ', carrito.calculate())
