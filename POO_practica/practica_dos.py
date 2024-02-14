from practica_uno import Producto
"""
2. Añadir una clase pedido que tiene como atributos:
    - lista de productos
    - lista de cantidades
   Añade las siguiente funcionalidad:
    - total_pedido: muestra el precio final del pedido
    - mostrar_productos: muestra los productos del pedido
"""

"""
3. Siguiendo con la clase pedido, añade la siguiente funcionalidad:
    - aniadir_producto: le pasamos un producto y una cantidad,
    añadira ese producto y esa cantidad a su respectiva lista.
    Debemos validar que el dato que nos pasen es correcto, es decir,
    que sea un producto y que la cantidad sea valida. En caso de que no,
    devolver una excepción.
    - eliminar_producto: le pasamos el producto a borrar, si existe, lo eliminamos.
    Sino existe devolver una excepcion, indicandolo.
    Comprobar tambien que es un producto lo que nos pasan.
"""
class Pedido:

    def __init__(self):
        #aqui se va inicializar las variables y listas
        self.__productos = []
        self.__cantidades = []
        self.__total =0

    def anadir_producto(self, productos, cantidad):
        #aca se comprueba que el producto sea una instancia de la clase producto para añadirlo a la lista
        #se pregunta si no es una instancia, entonces se va al raise y muestar el error
        if not isinstance(productos, Producto) or not isinstance(cantidad,int) or cantidad <=0:
            raise TypeError ("porfavor verifique la informacion ingresada" + str(TypeError()))
        if productos in self.__productos:
            #como el producto ya existe, busco el indice y lo utilizo para actualizar la cantidad o el precio.
            indexx = self.__productos.index(productos)
            #no entiendo por que se suma
            self.__cantidades.index[indexx] =  self.__cantidades.index(indexx) + cantidad
            print("se actualizo el precio del producto")
        else:
            self.__productos.append(productos)
            self.__cantidades.append(cantidad)

    def eliminar_producto(self, producto):
        #esta condicion es para verificar si el producto existe
        if not isinstance(producto, Producto):
            raise TypeError ("este producto no es una instancia de producto " + str(TypeError))
        else:
            # obtengo el indice del producto
            indexx = self.__productos.index(producto)
            self.__productos.pop(indexx)
            self.__cantidades.pop(indexx)

    def total_pedido(self, ):
        total = 0
        #for para recorrer dos listas juntas con el metodo zip()
        for (p,c) in zip(self.__productos,self.__cantidades):
         total += Producto.calcular(p, c)
        return total
    def mostrar_productos(self):
        for (p,c) in zip(self.__productos,self.__cantidades):
            print(f'producto: {p} , cantidad {c}')


if __name__ == "__main__":
    p1 = Producto(1, "producto 1", 5)
    p2 = Producto(2, "producto 2", 15)
    p3 = Producto(3, "producto 3", 25)
    p4 = Producto(8, "carro", 6700)


    pedido = Pedido()
    """
    print('Total pedido:', pedido.total_pedido())
        pedido.mostrar_productos()
    """
    try:
        #print("se agrega un nuevo producto que desate el error")
        #pedido.anadir_producto("escoba", 3.99)
        print("se agrega un producto correcamente ")
        pedido.anadir_producto(p4, 1)
        pedido.anadir_producto(p1, 1)
        pedido.anadir_producto(p2, 1)
        print("mostrar producto añadido ")
        pedido.mostrar_productos()
        #print("eliminar producto añadido ")
        #pedido.eliminar_producto(p4)
        print("mostrar total de pedidos", str(pedido.total_pedido()))

    except Exception as e:
        print(e)
