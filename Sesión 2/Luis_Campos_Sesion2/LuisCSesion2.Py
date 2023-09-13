resultado = max(5,10,3,8)
print(resultado)

resultado = round(3.14159,2)
print(resultado)

resultado = min(5,10,3,8)
print(resultado)


valor =23
mensaje = 'buenas tardes, este es un Hola Mundo'
print('El tipo de dato de la variable valor es:', type(valor))
print('El tipo de dato de la variable mensaje es:', type(mensaje))

cadena = '123'
print('El tipo de dato de la variable cadena es:', type(cadena))
cadena = int(cadena)
print('El tipo de dato de la variable cadena es:', type(cadena))

cadena + cadena


nombre = ('Jose Luis Campos')
Edad = ('22')
print('mi nombre es',nombre,'mi edad es:', Edad, )
longitud = len(nombre)
print('la longitud',longitud,)

valor = 30 
if valor > 22:
    print ('el numero es mayor que 22')
    if valor % 2 == 0:
        print('el numero es par')
    else:
        print('el numero es impar')
else:
    print('el numero no es mayor que 5')

x = 5
print(x)

y = 'jhon'
print (y)

print_ = 2
print (print_)

x = 2 
y = 'Naranja'
z = 14.2

print(x)
print(y)
print(z)

print ('hola mundo')
#imprimir varias variables
nombre = 'Luis Campos'
edad = 22
print ('Mi nombre es:',nombre,"y tengo",edad,"años.")

valorHora = 17.5 
totalHoras = 8
sueldoDiario = valorHora*totalHoras
print ('Nombre Empleado:',nombre,'El precio por hora trabajada:',valorHora,'y el sueldo diarios es:',sueldoDiario,)

#formato de cadena 

print (f'Mi nombre es ´{nombre} y tengo {edad} años')

#imprimir por tipo de variable %
print (f'Mi nombre es {nombre} y tengo {edad} años.\n\n ')

peso = 120

print('Nombre:\n\t Luis \n Edad: \n\t 37')
print ('Mi nombre es %s y tengo %d años y peso %d \n\n' %(nombre,edad,peso))

print('hola', end = '')
print('Mundo')

colores = ['verde','amarillo','rojo']
print(colores[0])
print('\n')
print(colores[1])
print('\n')
print(colores[2])
print('\n')
print(colores[-2])
print('\n')
print('\n')
print('\n')
print(*colores, sep= ',')

mensaje ='tenemos que hacer tarea'
mensajeMinuscula = mensaje.lower()

mensajeMayuscula = mensaje.upper()

print(mensajeMinuscula)
print(mensajeMayuscula)

nombreEmpleado1 = 'Jose antonio fuentes velasquez'
nombreEmpleados2 = 'jose antonio fuentes velasquez'
nombreEmpleado1 == nombreEmpleados2
print(nombreEmpleado1.lower())
print(nombreEmpleados2.lower())

x = str(3)
y = int (3)
z = float(3)
print(4*x)
print (x,y,z)

#Tarea 
nombres = input('Jose Luis')
primerApellido = 'Campos'
segundoApellido = 'Giron'
edad = 22
nacionalidad = 'Salvadoreño'
sexo = 'Masculino'

print (f'Mi nombre es {nombres} {primerApellido} {segundoApellido}\n y tengo {edad} años, soy de nacionalidad {nacionalidad} y mi sexo es {sexo}.\n\n ')



