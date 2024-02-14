"""
1. Crear una Clase Producto con los siguientes atributos:
 - codigo
 - nombre
 - precio
Creale, su constructor, getter y setter y una funcion llamada calcular_total, donde le pasaremos unas unidades
y nos debe calcular el precio final.
"""
class Producto:

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

#este es el get
    @property
    def codigo(self):
        return self.__codigo

#este es el set
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def calcular (self, cantidad):
        return self.precio * cantidad


    #aqui sobre escribo el metodo to string

    def __str__(self):
        return 'codigo: ' + str(self.__codigo) + ', nombre: ' + str(self.__nombre) +', precio: ' + str(self.__precio)


if __name__ == "__main__":
    p1 = Producto(1, "Producto 1", 25.6)
    p2 = Producto(2, "Producto 2", 11.5)
    p3 = Producto(3, "Producto 3", 46)

    #p1.nombre = "que pez"
    print(p1.calcular(22))
