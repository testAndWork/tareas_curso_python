NombreUsuario = 'Samuel Bonilla'
print(f'¡Hola, {NombreUsuario}! Bienvenido a nuestro programa.')
print('¡Hola, %s! Bienvenido a nuestro programa.'%NombreUsuario)

#Ejemplo
base = 5
altura = 7

areaTriangulo = base*altura/2

print('El area del triangulo es %.2f'%(areaTriangulo))

#Ejemplo

NombreUsuario = 'Samuel Bonilla'
edadUsuario = '19'
ciudadResidencia = 'Soyapango'

print(f'{NombreUsuario},{edadUsuario},{ciudadResidencia}')

#Ejemplo

x = 5
print(type(x))

x = 1 
y = 1.45654
z = 2j

print(type(x), type(y), type(z))

x = 1765343 
y = 145.654
z = 5+2j

print(type(x), type(y), type(z))

#Ejemploint
EjemploInt1 = 3234532
EjemploInt2 = -12323
EjemploInt3 = 2
EjemploInt4 = 0

print(type(EjemploInt1), type(EjemploInt2), type(EjemploInt4))

#EjemploFloat
EjemploFloat1 = 1.1
EjemploFloat2 = 234.584
EjemploFloat3 = 34.00000
EjemploFloat4 = 0

print(type(EjemploFloat1), type(EjemploFloat2), type(EjemploFloat4))

#Ejemplo de E

x = 35E3
y = 12e4
z = 1.2e4

print(type(x), type(y), type(z))

print(type(12*10*4))

#Numeros complejos

x = 3+5j
y = -5j
z = -3+0j

print(type(x), type(y), type(z))

#Practica

print(type(3))
print(type(3.14))
print(type(1+8j))
print(type("Hello World"))
print(type([1, 2, 3]))
print(type({1: 'one', 2: 'two', 3: 'three'}))
print(type({1, 2, 3}))
print(type((1, 2, 3)))

#Ejemplo 
dato = '1200'
hora = 34

Sueldo = dato*hora
print(Sueldo)

#int: para contador en bucle

totalContador = 0

for i in range(1,8):
    totalContador = totalContador + i
    print('valor de i:',i)
    print('valor de totalContador: ',totalContador)

    print('El tipo de la variable totalContador es:', type(totalContador),'y su valor final es',totalContador)

#float, list: calcular el promedio de notas de un alumno

notas = [7.0, 6.0, 9, 10.0, 8.4, 5.7, 9.4, 9.7]

promedio = sum(notas)/len(notas)

print('El promedio de notas es: ', promedio)

#bool: validar un campo

usuarioRegistrado = False

if usuarioRegistrado:
    print('Bienvenido al Curso')
else:
    print('El Usuario no esta en el Curso')

#List: tipo str

nombres = ['Cristian', 'Denis', 'Edwin', 'Henry', 'Roberto']
print(f'Lista de nombres: {nombres}')

#Tuple: Dias de la semana y otra con valores

diasSemana = ('L', 'M', 'W', 'J', 'V')

numeros = (1, 2, 3, 4, 5)

print(diasSemana)
print(type(diasSemana))

print(numeros)
print(type(numeros))

#Dict: Nombres y contactos

dictContactos = {

    'Cristian': 23245245, 
    'Denis': 23214456, 
    'Edwin': 79443198, 
    'Henry': 98846674, 
    'Roberto': 98332355   
}

print(type(dictContactos))

#Conversion de tipo

x = 1
y = 2.8
z = 3j

print(type(x), type(y), type(z))

convertX = float(x)
convertY = complex(y)
#convertZ = int(z) #Esta conversion no es posible

print(convertX,convertY)
print(type(convertX), type(convertY))

#Ejemplo

edadUsuario = input('Ingrese la edad del usuario')

edadUsuario = int(edadUsuario)

print(type(edadUsuario))

print('La edad es:', edadUsuario)

#Ejemplo 2

edadUsuario = int(input('Ingrese la edad del usuario:'))

print(type(edadUsuario))

print('La edad es:', edadUsuario)

#cadena de str -> int

cadena = '30'

strInt = int(cadena)

print(type(cadena), type(strInt))

print(cadena + cadena)

print(strInt + strInt)

#cadena de str -> float

cadena = '30'

strFloat = float(cadena)

print(type(cadena), type(strFloat))

print(cadena + cadena)

print(strFloat + strFloat)

#entero int -> cadena

entero = 45

print(type(entero))

cadenaInt = str(entero)

print(type(cadenaInt))

#entero float -> cadena

flotante = 4.59

cadenaFlotante = str(flotante)

print(type(cadenaFlotante))

#Lista a cadena

lista = [1, 2, 3, 4, 5]

cadenalst = str(lista)

print(type(cadena))
print(cadenalst)

#cadena a list

cadena = [1,2,3,4,5,6]

lista = eval(cadena)

print(type(lista))

print(lista)

#Ejemplo

print("Hola Mundo")
print('Hola Mundo')

a= "Hola mundo"
b= 'Hola mundo'

print(a,b)

#Ejemplo multiple
a = """ Este es una prueba de uso de comillas multiples """ 
print(a)

#Ejemplo cortar cadenas

a = "Hello, worldwide "
b = "No tuve opcion"

print(len(a),len(b))

print(a[2:16])
print(b[4:7])

print(a[0:10])
print(b[1:7])

print(a[:10])
print(b[:7])

print(a[2:])
print(b[5:])

print(a[-5:-2])
print(b[4:5])

#lista
lista = [1,2,3,4,5,6,7,8,9,10]

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-6])
print(lista[-8])

#Ejercicios

#Ejercicio 1
mensaje = "Bienvenido a Python"

print(mensaje)

#Ejercicio 2

poema = """ Por una mirada, un mundo,
por una sonrisa, un cielo,
por un beso… ¡yo no sé
qué te diera por un beso! """

print(poema)

#Ejercicio 3

cadena = "Programacion en Python"
subcadena = cadena[-6:]

print(subcadena)

subcadena2 = cadena[12:18]
print(subcadena2)

#Ejercicio 4

cadena = "abcdefghij"
print(cadena[2:6])

#Ejercicio 5

cadena = "python es genial"
print(len(cadena))
print(cadena[7:16])

parte = cadena[7:16]

#Ejemplo 

print(a.upper())

print(a.lower())

#Ejemplo de eliminar espacio

a = "     Hello world!"

print(a,a.strip())
print(a)
print(a.strip())

#Ejemplo

numStr = '  1234  '
print(numStr)

print(numStr.strip())

#Reemplazar cadena

a = "Hello World!"
print(a.replace ("H", "J"))
print(a.replace ("llo", "lou"))
print(a.replace ("World", "Gourld"))

#cadena dividida

a= "Hello World!"

print(a.split(","))
print(a.split("o"))

#Concantenacion de cadenas

a= 'Hello'
b= 'World'

print(a + b)
print(a +' '+ b)

#Formato de cadenas

edad = 34
cadena = "Mi nombre es Texto, y tengo {}"

print(cadena.format(edad))

#Ejemplo

superMercado   = 'La despensa de don Isaias'
cantidadGranos = 3
precioLibra    = 1.40
total = precioLibra*cantidadGranos

ordenSuper = 'Fui a {} y compre {} libras de frijoles a un precio de {} en un total de {} dolares'

print(ordenSuper.format(superMercado,cantidadGranos,precioLibra,total))

#Ejemplo

superMercado   = 'La despensa de don Isaias'
cantidadGranos = 3
precioLibra    = 1.40
total = precioLibra*cantidadGranos

ordenSuper = 'Fui a {0} y compre {1} libras de frijoles a un precio de {2} en un total de {3} dolares'

print(ordenSuper.format(superMercado,cantidadGranos,precioLibra,total))

#Ejemplo de /
superMercado = 'La Despensa de don \'Isaias\''
print(superMercado)


#Aplicando Conocimiento
#Ejercicio 1

mensajepython = "Programación es arte y ciencia, un lenguaje que crea la realidad, una forma de dar vida a la inteligencia, y al mundo digital una identidad"

print(mensajepython.split())

#Ejercicio 2
print('\t')
elAbecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(elAbecedario))
print(elAbecedario[:-16])
print(elAbecedario[-10:])
print(elAbecedario[::-1])