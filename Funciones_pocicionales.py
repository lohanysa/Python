#se puede decir que el args es una lista
""""
def suma (*args):
    s=0
    for i in args:
        s+=i
    return s

resultado= suma(3,4,5,4)
print(resultado)
"""
"""
def lenguajes (nombre, *lenguaje):
    print(f"hola, {nombre} tus lenguajes favoritos son:{lenguaje}")

lenguajes("lohanys", "java", "javaScript", "python", "SQL")
"""
#recordar que los Kwargs esta asociados a una clave volor tiene un conportamiento como de listas
#los contadores son necesarios en el kwargs
#los kwargs trabajan en forma de diccionario
def lenguajes (nombre, **Kwargs):
    print(type(Kwargs))
    print(f"hola, {nombre} los lenguajes que conoses son: ")
    contador = 0
    for i in Kwargs:
        contador += 1
        print(f"{contador}: {Kwargs[i]}")

#aqui si es necesario ponerle nombres cuando pasas los valores por la relacion clave valor

lenguajes("lohanys", idioma1 ="java", idioma2 ="SQL", idioma3="HTML", idioma4 ="javaScript", idioma5 = "python")
