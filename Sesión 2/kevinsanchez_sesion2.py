#Ejercio 1
resultado = max(5,10,3,8)
print(resultado)

#Ejercicio 2
resul1 = round(3.14159, 2)
print(resul1)

#Ejercicio 3
resultado2 = min(5,10,3,8)
print(resultado2)

##########################################
name = "Kevin"
age = 27

print('Mi nombre es: ', name, 'y mi edad es:', age)
print(len(name))

##########################################

#funcion print()
print('Hola mundo')

##########################################

nombre = 'Carlos'
edad = 20
print('mi nombre es ', nombre, 'y mi edad es', edad)


mensaje = 'buenas tardes, este es un Hola mundo'
longitud = len(mensaje)
print('La longitud del mensaje es:', longitud)

##########################################

#type()
valor = 23
mensaje = 'Buenas tardes, este es hola mundo version2'
print('El tipo de dato de la variable es:', type(valor))

print('El tipo de dato de la variable es:', type(mensaje))

cadena = '123'
print('El tipo de dato es la variable cadena es: ', type(cadena))
cadena = int(cadena)
print('El tipo de dato es la variable cadena es: ', type(cadena))

cadena + cadena

valor = 14
print('El tipo de dato de la variable es: ', type(valor))

valor = float(valor)
print('El tipo de dato de la variable es: ', type(valor), valor)

if True:
    print('Es una prueba de identacion:', 3 + 4)

Valor = 6
if Valor > 19:
    print('El numero es mayor que 19')
    if valor % 2 == 0:
        print('El numero es par')
    else:
        print('El numero es impar')
else:
        print('El numero no es mayor que 19')

    #This is a comment

#Camel_case
#miVariableEjemplo
#nombreUsuario
#calcularImpuesto

#Pascal_case
#miVariableEjemplo
#nombreUsuario
#crearUsuario

#Snake_case
#numero_de_telefono
#cantidad_de_prodcutos
#mi_variable_ejemplo

#Lower_case
#mivariableejemplo
#cantidaddeproductos
#nombre

#Upper_case
#PI
#MAXIMO_VALOR
#MIVARIABLEEJEMPLO


def saludar(nombre):
    mensaje = 'Hola, ' + nombre + '!'
    print(mensaje)

saludar("Alice")

""" Este es un comentario de multilinea,
#aca escribo todo lo que quiera
"""
print('Hola Mundo')

x = 10
print(x)

y = 'Jhon'
print(y)

10*y

_print = 2
print(_print)

#Ejemplo
MyVar = 'Estilocamelcase'
MyVar

#Practica
m = 2
y = 'naranja'
z = 14.6

print(m)
print(y)
print(z)

x, y, z = 2, 'sandia', 23.3

print(x, y, z)
print(x,'\n\n', y,'\n',z,'\n\n\n')

x = 'Python is awesome'
y = 'incredible'
z = 'and is easy'

print(x,y,z)
print(x + y + z)

m, n, o = 1,2,3
print(m,n,o)

print(m + n + o)

print('La multiplicacion es', 2+3+5,'y la multiplicacion es', 10*2)

#Impresion de strings basicos
print('Hola Mundo')

#Imprimir varias variables en una linea

_nombre = 'kevin sanchez'
_edad = 26

print('Mi nombre es:', _nombre, 'y tengo', _edad, 'años')

valor_Hora = 17.5
total_horas = 8

sueldodiario = valor_Hora*total_horas

print('Nombre Empleado', _nombre,
'El precio por hora trabajada', valor_Hora,
'y el sueldo diario es:',sueldodiario)

nombre= 'Juan'
edad = 37
valorHora = 17.5
totalHoras = 8
sueldoDiario = valorHora*totalHoras

print(f'mi nombres es {nombre} y tengo {edad} años.')

print(f'Nombre empleado: {nombre}\n El precio por hora trabajada: {valorHora}\n y el sueldo es: {sueldoDiario}')

print('Mi nombre es %s y tengo %d años.\n\n'%(nombre, edad))

nombre = 'Alice'
edad = 30
peso = 120

print('Mi nombre es %s y tengo %d años %d.\n\n'%(nombre,peso,edad))

nombre = 'Alice'
preciohora = 17.5
horasTrabajadas = 44

print('Mi nombre es %s, cobro: %d por hora y trabajo %.2f\n\n'%(nombre,horasTrabajadas,preciohora))
print('Mi nombre es %s, cobro: %d por hora y trabajo %.3f\n\n'%(nombre,horasTrabajadas,preciohora))

#Tabulacion en la impresion y salto de lineas
print('Nombre: \t José \n Edad: \t 37')

#Tabulacion en la impresion y salto de lineas
print('Nombre: \n\t José \n Edad: \n\t 37')

print('Hola', end= '')
print('mundo')

colores = ['verde', 'amarillo', 'rojo']

print(colores[0])
print(colores[1])
print(colores[2])
print(colores[-2])

print(colores)
print('\n')
print(*colores)
print('\n')
print(colores, sep= ',')
print('\n')
print(*colores, sep= ',')

mensaje = "TeneMos que Hacer TaReaS"
mensajeMinuscula= mensaje.lower()
mensajeMayuscula=mensaje.upper()

print(mensajeMinuscula)
print(mensajeMayuscula)

nombreEmpleado1 = "Jose Antonio Fuentes"
nombreEmpleado2 = "jose antonio fuentes"

nombreEmpleado1 == nombreEmpleado2

nombreEmpleado1.lower == nombreEmpleado2.lower

print(nombreEmpleado1.lower())
print(nombreEmpleado2.lower())

x = str(3)
y = int(3)
z = float(3)

print(4*x)
print(x,y,z)

##########################################

nombre = "Kevin"
primerApellido = "Sanchez"
segundoApellido = "Crespin"
edad = 27
nacinalidad = "Salvadoreña"
sexo = "Masculino"

print(f'Mi nombre es {nombre} y mis apellidos son {primerApellido} {segundoApellido} \n, tengo {edad} y soy de nacionalidad {nacinalidad} y soy de sexo {sexo}')