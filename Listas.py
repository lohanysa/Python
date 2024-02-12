"""
Escribir un programa que almacene las asignaturas de un curso

asignaturas = ["matemática", "fisica", "inglés", "español"]
print(asignaturas[0])
print(type(asignaturas))

#loteria ordenada
numeros =[]
for i in range(6):
    numeros.append(int(input("ingrese un numero: ")))
numeros.sort()

print(f'los numeros ganadores son: {numeros}')
"""
#como recorrer la lista
lista=[1, 2, 3,4 ,5 ,6,7,8, "Hola mundo :)"]
for i in lista:
    print(i)
"""
#metodo para eliminar un elemento,se debe escribir el elemento que se quiere eliminar
#en caso de que hubera dos 6 solo elimina el primero
lista.remove(6)
print(f'lista despues de eliminar el 6 con remove: {lista}')
#aqui ae debe pasar una posicion es decir el indice, tambien es un metodo que elimina elementos
#para eliminar el hola mundo, coloco la posicion ocho por que anterios mente se elimino un elemento
#el tamaño de la lista se redujo
lista.pop(7)
print(f'lista despues de eliminar el Hola mundo: {lista}')
#otro metodo para eliminar es del, es exactamente igual a el metodo pop
del lista[6]
print(f'lista despues de eliminar el 8 con del: {lista}')
#otro metodo para eliminar es lista.clear
#dlimina todoslos elementos de la lista
lista.clear()
print(f'lista despues de utilizar clear: {lista}')

"""

#metodo para contar las veces que se repite un elemento
print(f'cuantas veces esta el hola mundo en la lista :{lista.count("Hola mundo :)")}')

#este metodo muestra el indice en el que se encuentra un elemento
print(f' pocision del numero 4: {lista.index(4)}')

#metodod para mostrar la lista arreves
lista.reverse()
print("lista reversa")
print(lista)