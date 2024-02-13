print("hello, world")
#practica de variables
nombre = "lohanys"
numero = 63748507
estatura = 1.68
print("holis " + nombre)

#en este caso para que no de error se convierte en numero en string con las siglas STR
print("Hola "+nombre +" su numero celular es " + str(numero))
"""
otra manera de escribir el print anterior mas rapido y corto es: 
esto se llama cadenas F
"""
print(f'hola {nombre} su numero celular es: {numero} esto es escrito con el print F')
print (f'hola {nombre}  con estatura {estatura} su numero es: {numero}')

print(type(nombre) )
print(type(estatura))
print(type(numero))
