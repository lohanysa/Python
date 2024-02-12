#formas de crear un diccionario
"""
#primera forma
diccionario ={
    "documento": 456234,
    "nombre": "sara",
    "edad":28

}
print(diccionario)
#segunda forma
diccionario_segundo = dict(nombre='paola', edad=34, documento=336677)
print(diccionario_segundo)
#tercera forma
diccionario_tercera = dict([
    ("nombre","pablo"),
    ("edad", "29"),
    ("documento", 345780)
])
print(diccionario_tercera)


"""
inventario = {"manzana":230,"pera": 120, "melocoton": 37, "mango":33}

print(inventario.items())