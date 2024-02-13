class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        return self.nombre, self.edad


class Ciudadano (Persona):
    def __init__(self, nombre, edad, deposito):
        super().__init__(nombre, edad)
        self.deposito = deposito

    def impuesto(self):
        if self.deposito > 4000:
            print("Si debe pagar")
        else:
            print("No, paga")

    def imprimir(self):
        return self.deposito


class Main:
    def __init__(self):
        print("Bienvenido al sistema de impuesto")
        nombre = input("ingrese su nombre: ")
        edad = int(input("ingrese su edad: "))
        deposito = int(input("ingrese el monto del deposito: "))
        Ciudadano1 = Ciudadano(nombre, edad, deposito)
        Ciudadano1.impuesto()

"""
Se agregó una comprobación if __name__ == "__main__": para garantizar que el código dentro de ese bloque solo se ejecute cuando el script se ejecute directamente,
 no cuando se importe desde otro script. Esto es una buena práctica en Python.
"""

if __name__ == "__main__":
    main_instance = Main()

