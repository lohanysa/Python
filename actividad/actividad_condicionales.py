nombre = (input("ingrese su nombre: "))
monto = int(input("cantidad total de la compra: "))

if(monto>= 80 and monto < 150):
    descuento = (int(monto) * 0.1)
    print(f'hola, {nombre}')
    print(f' valor de la compra sin descuento {monto}')
    print(f'su descuento es de: {descuento} su compra final es de: {monto-descuento}')
elif(monto >=150 and monto <= 300):
    descuento = (monto * 0.15)
    print(f'hola, {nombre}')
    print(f' valor de la compra sin descuento {monto}')
    print(f'su descuento es de: {descuento} su compra final es de: {monto-descuento}')
elif(monto >300 and monto < 500):
    descuento = (monto * 0.20)
    print(f'hola, {nombre}')
    print(f' El valor de la compra sin descuento es : {monto}')
    print(f'Su descuento es de: {descuento} su compra final es de: {monto - descuento}')
else:
    print(f'hola, {nombre}')
    print("los descuentos solo aplican para compras mayores o iguales al monto de $ 80")
    print(f' su monto final es de  : {monto}')

"""
1. Angel Mario Villa Lopez el valor de su compra con descuento es de: 364
2. Rosa Diaz el valor de: 94.5
3. Dilan Gonzales el valor de su compra de: 212.5
4. Kelly Daza el valor de su compra es de: 344.0
"""