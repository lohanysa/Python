print("PROMEDIO DE NOTAS ")
nombre = input("ingrese su nombre completo: ")
materias = int(input("cantidad de materias que cursa: "))
i =0
prom = 0
while i < materias:
    print("***---***")
    curso= input(f'nombre del curso{i+1}: ')
    nota = float(input("ingrese caloficacion del curso: "))
    prom += nota
    i += 1

print("***RESULTADO***")
print(f'{nombre} su promedio final es: {prom/materias}')
if(prom/materias <3.0):
    print("lo siento has fracasado :(")
elif(3.0< prom/materias<4.0 ):
    print("aprobado, puede mejorar >w<")
else:
    print("aprobado, tiene execelentes calificaciones :)")

#mi nombre es lohanys y mi promedio seria de 4.26