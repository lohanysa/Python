"""
crear una tupla y pedir que ingresen un numero por teclado
e indicar en que posicion esta
"""

numeros = (5,6,7,8,6,5,5,6,90,12,14,12)
numero= int(input("dame un numero: "))

#print("el numero " + str(numero) + "se repite " + str(numeros.count(numero)))

print ("el numero: " + str(numero) + "se encuentra en el indice " + str(numeros.index(numero)))
