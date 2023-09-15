import librarys.my_modulo2 as rg

names = []
ages = []

op = 'si'
while op == 'si':
    nombre = input('Digite el nombre: ')
    edad = int(input('Digite la edad: '))
    rg.nombre_edad(nombre,edad)
    
    op = input('Quieres seguir ingresando?  ')


#rg.nombre_edad(nombre,edad)





