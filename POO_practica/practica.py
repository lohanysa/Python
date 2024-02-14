"""
7. Mostrar con un while los números del 1 al 100

8. Mostrar con un for los números del 1 al 100

9. Mostrar los caracteres de la cadena "Hola mundo"

10. Mostrar los números pares entre 1 al 100
"""
class mientras:
    def funcion1(self):
        num=0
        while num < 100:
            num += 1
            print(num)

class para:
    def funcion2(self):
        print ("este es el ciclo for")
        for i in range(100):
            print(i+1)

class mostrar:
    def imprimir(self):
        for i in "Hola Mundo":
            print(i)

class pares:
    def par(self):
        """
La línea de código que proporcionaste es una lista de comprensión de Python. La lista de comprensión se ejecuta de la siguiente manera:
Se crea una lista vacía llamada lista_pares.
Se itera sobre el rango de números entre 1 y 100 (range(1,101)).
Para cada número en el rango, se verifica si es par o no. Esto se hace usando la expresión booleana (x % 2 == 0).
Si el número es par (es decir, la expresión booleana es True), se agrega a la lista lista_pares.
Después de iterar sobre todos los números en el rango, la lista lista_pares contiene todos los números pares entre 1 y 100, inclusive.
        """
        #la primera x es el resultado de la iteracion
        #luego se escribe el ciclo for normal y puedo agregarle un condicional
        #en este caso verificar que el numero sea par
        lista_pares = [ x for x in range(1,101) if x % 2 ==0]
        print(lista_pares)
if __name__ == "__main__":
    #ciclo_mientras = mientras()
    #ciclo_para = para()
    #ciclo_mostar = mostrar()
    #ciclo_mostar.imprimir()
    par_impar = pares().par()
