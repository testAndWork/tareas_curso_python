alumnos = []

while True:
    nombre = input("Ingrese el nombre del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    alumnos.append((nombre, edad))
    
    continuar = input("¿Desea ingresar otro alumno? (s/n): ")
    if continuar.lower() != "s":
        break

print("Alumnos mayores de 18 años:")
for alumno, edad in alumnos:
    if edad > 18:
        print(alumno)