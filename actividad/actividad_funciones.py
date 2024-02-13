def convertir(seleccion, tipo, valor):
    resultado= 0

    match seleccion:
        case 1:
            match tipo:
                case "a": resultado = valor * 3750
                case "b": resultado = valor * 6.37
                case "c": resultado = valor * 0.76
        case 2:
            match tipo:
                case "a": resultado = valor * 4000
                case "b": resultado = valor * 6.93
                case "c": resultado = valor * 0.83
    return round(resultado)

def menu():
    print("bienvenido al sistema de convertidor de monedas")
    print("tipo de moneda que posee: ")
    print("1: dolares")
    print("2: euros ")
    seleccion = int(input(" ingrese respuesta: "))
    repetir = 0
    while(repetir != 2):
        print("\n")
        print("convertir a : ")
        print("a- pesos colombianos")
        print("b- yuanes")
        print("c- libras esternilas")
        tipo=(input("seleccion: "))

        if (tipo != 0):
            valor = float(input("\n valor de la moneda actual: "))
            total = convertir(seleccion, tipo, valor)
            print(f"\n el total convertido es: {total}")
        else:
            print("valor invalidos \n")

        print("desea convertir nueva mente \n")
        repetir = int(input("1-si    2-no:  "))
        if repetir==2:
            print("hasta pronto :)")
menu()