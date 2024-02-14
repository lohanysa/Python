from practica_uno import Producto
"""
2. Añadir una clase pedido que tiene como atributos:
    - lista de productos
    - lista de cantidades
   Añade las siguiente funcionalidad:
    - total_pedido: muestra el precio final del pedido
    - mostrar_productos: muestra los productos del pedido
"""
class Pedido:

    __productos = []
    __cantidades = []

    def __init__(self, producto, cantidad):
        self.__productos = producto
        self.__cantidades = cantidad
        self.__total =0

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

    productos = [p1, p2, p3]
    cantidades = [5, 10, 2]

    pedido = Pedido(productos, cantidades)

    print('Total pedido:', pedido.total_pedido())
    pedido.mostrar_productos()