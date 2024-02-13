agenda = {"jose": 302944, "Mario": 829455, "Angel": 829405, "Luis": 930594}

def consultar ( ):
    nombre = input("ingrese nombre: ")
    #otra manera de escribir esta condicional es agenda.get(nombre,"no existe")
    respuesta = agenda[nombre] if nombre in agenda else "no existe"
    return respuesta

def anadir():
    nombre = input("ingrese nombre: ")
    if nombre not in agenda:
        numero=int(input("ingrese numero: "))
        agenda[nombre] = numero
    else:
        print("ya existe")

def modificar ():
    nombre = input("ingrese nombre para modificar el numero")
    if nombre in agenda:
        numero=int(input("ingrese nuevo numero: "))
        agenda[nombre] = numero
    else:
        print(f" {nombre} no existe ")
def borrar():
    nombre=input("ingrese un nombre")
    if nombre in agenda:
       resultado = agenda.pop(nombre), 'se elimino ', nombre, 'con exito '
    else:
        resultado = "no existe, fracaso en la eliminacion"
    return resultado
menu = 0


while menu != 5:
    print("\n")
    print("1. Consultar")
    print("2. Añadir")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Salir")
    menu = int(input("digite su opcion(ingrese el numero): "))
    match menu:
        case 1: print(consultar())
        case 2: anadir()
        case 3: modificar()
        case 4: print(borrar())
        case 5: print("hasta pronto ;)")
