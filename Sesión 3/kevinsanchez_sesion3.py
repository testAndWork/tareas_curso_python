#Tipos de datos
"""
str -> String
numericos -> int,float, complex
secuencia -> list,tuple,range
mapeo -> dict
establecer tipos -> set, fronzenset
booleano -> bool
binarios -> bytes,bytearray,memoryview
none -> nonetype
"""
##################################################

user = "Steren"

print(f'!Hola {user} Bienvenido a nuestro programa')
print("!Hola %s Bienvenido a nuestro programa." %(user))

##################################################
a = bxh/2
b = 2.8
h = 7.4

a = (b*h / 2)

print(f'El area del triangulo es: {a}')

##################################################

nombre = str(input("Ingrese su nombre:"))
edad = int(input("Ingrese su edad: "))
ciudad = str(input("Ingrese su residencia:"))

print(f"El nombre del usuario es: {nombre}, y su edad es de {edad}, su resicencia es {ciudad}")


##################################################

#Tipo de datos
x = 1           #int
y = 1.45654     #float
z = 2j          #complex

print(type(x), type(y), type(z))

ejemploInt1 = 3234532
ejemploInt2 = -12323
ejemploInt3 = 2
ejemploInt4 = 0

type(ejemploInt1), type(ejemploInt2), type(ejemploInt3), type(ejemploInt4)

ejemploFloat1 = 1.1
ejemploFloat2 = 234.5683
ejemploFloat3 = 34.0000
ejemploFloat4 = 0

print(type(ejemploFloat1), type(ejemploFloat2), type(ejemploFloat3), type(ejemploFloat4))

x = 35E3
y = 12e4
z = 1.2e4
print(type(x), type(y), type(z))
print(type(12*10**4))

x = 3+5j
y = -5j
z = -3+0j

print(type(x), type(y), type(z))

##################################################
# Test para saber los tipos de datos

print(type(3))
print(type(3.14))
print(type(1 + 8j))
print(type("Hello Wordl"))
print(type([1,2,3]))
print(type({'one': 1, 'two': 2, 'three': 3}))
print(type({1,2,3}))
print(type((1,2,3)))

dato = '1200'
hora = 34

sueldo = dato * hora

print(sueldo)
##################################################

#contador
totalContador = 0

for i in range(1,5):
    totalContador = totalContador + i
    print('El valor de i es: ', i)
    print('El valor contador es: ', totalContador)

print('El tipo de la variable contador es:,', type(totalContador),'y su valo final es:', totalContador)

##################################################

notas = [7.0,6.0,9,10.0,8.4,5.7,9.4,9.7]

promedio = sum(notas)/len(notas)

print('El promedio de notas es: ', promedio)

##################################################

userRegister = True

if userRegister:
    print('Bienvenido al curso')
else:
    print('El ususario no esta en curso')

##################################################

nombres = ['Cristian', 'Deniss', 'Edwin', 'Henry', 'Roberto']

print(f'Lista de nombre: {nombres}')

##################################################

diasSemana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')
numeros = (1,2,3,4,5,6,7)

print(diasSemana)
print(type(diasSemana))

print(numeros)
print(type(numeros))

##################################################

diccionarioContactos = {
    'Cristian' : 12345678,
    'Edwin' : 12345678,
    'Dennis' : 12345678,
    'Henry' : 12345678,
    'Roberto' : 12345678,
}

print(diccionarioContactos)
print(type(diccionarioContactos))

##################################################

#Conversion de dato
x = 1
y = 2.8
z = 3j

print(type(x), type(y), type(z))

convertx = float(x)
converty = complex(x)
convertz = int(x)

print(convertx,converty)
print(type(convertx), type(converty))

##################################################

# Forma 1
edadUser = input('Ingrese la edad: ')

print(type(edadUser))

edadUser = int(edadUser)

print(type(edadUser))

print('La edad es: ', edadUser)


# Forma 2
edadUser = int(input('Ingrese la edad: '))

print(type(edadUser))

print('La edad es: ', edadUser)
##################################################

cadena = '30'

strInt = int(cadena)

print(type(cadena), type(strInt))

print(cadena + cadena)

print(strInt + strInt)

cadena = '3.75'

strFloat = float(cadena)

print(type(cadena), type(strFloat))

print(cadena + cadena)

print(strFloat + strFloat)

##################################################

entero = 45
type(entero)

cadenaInt = str(entero)
print(type(cadenaInt))

flotante = 4.59
type(entero)

cadenaFloat = str(flotante)
print(type(cadenaFloat))

##################################################

lista1 = [1,2,3,4,5]

cadenalst = str(lista1)

type(cadenalst)
cadenalst

#cadena a lista
cadena = '[1,2,3,4,5]'

lista2 = eval(cadena) #funcion para hacer la conversion

print(type(lista2))

print(lista2)

##################################################

#Cortar cadenas
a = 'Hello, World:Hola Mundo'
b = 'No se me courre nada'

print(len(a), len(b))

print(a[2:21])
print(b[4:5])

print(a[0:10])
print(b[17:20])

#Corte del principio
print(a[:14])
print(b[:9])

#Cortar hasta el final
print(a[2:])
print(b[5:])

#Indices negativos
print(a[-5:-2])
print(b[-14:-1])

lista = [1,3,4,5,6,7,8,9,10]

print(lista[-1])
print(lista[-2])
print(lista[-4])
print(lista[-6])
print(lista[-8])

a = 'Hello, World:Hola Mundo'
b = 'No se me courre nada'

print(b)
print(b[-3:-1])
print(b[-4:-1])
print(b[-6:-1])
print(b[-7:-1])

print(a)
subCadena = a[0:12]

##################################################

#---1
welcome = 'Bienvenido a Python'

print(f'Hola usuario {welcome}')

#---2
poema = """Recuerde el alma dormida
Avive el seso y despierte
Contemplando
Cómo se pasa la vida,
Cómo se viene la muerte,
Tan callando,
Cuán presto se va el placer,
Cómo, después de acordado
Da dolor,
Cómo, a nuestro parecer,
Cualquier tiempo pasado
Fue mejor."""

print(poema)

#---3
cadena1 = "Programacion en Python"

print(len(cadena1))

print(cadena1[16:22])

subcadena = cadena1[16:22]

print(subcadena)

#---4
cadena2 = 'abcdefghij'
print(len(cadena2))

print(cadena2[2:6])

subcadena = cadena2[2:6]

print(subcadena)

#---5
cadena3 = 'Pyhton es genial'
print(len(cadena3))
print(cadena3[7:16])

subcadena = cadena3[7:16]

print(subcadena)

##################################################
a = 'Hello, World:Hola Mundo'
print(a.upper())

print(a.lower())

##################################################

#Metodo Strip
a = '   Hello World'
b = 'No se me courre nada'

print(b,a,b)
print(b,a.strip(),b)
print(a)
print(a.strip())

numStr = '  1234'

print(numStr)

print(numStr.strip())

##################################################

#Reemplazar cadena
a = 'Hello World'

print(a.replace("H", "j"))
print(a.replace("llo", "lou"))
print(a.replace("Wordl", "Guord"))

#################################################
#Cadena dividida

print(a.split(","))
print(a.split("o"))

#################################################
#Concatenacion
a = "Hello"
b = "Wordl"
print(a + b)
print(a +' '+ b)

#################################################
#Formato de Cadena

edad = 34
cadena = 'Mi nombre es texto y tengo' + edad

print(cadena)

edad = 34
cadena = 'Mi nombre es texto y tengo {}'

print(cadena.format(edad))
#################################################

superMercado = 'La despensa de Don Isaias'
cantidadGranos = 3
precioLibra = 1.40
total = precioLibra * cantidadGranos

ordenSuper = 'Fui a {} y compre {} libras de frijoles a un precio de {} dolares cada libra y gaste un total de {}'

print(ordenSuper.format(superMercado, cantidadGranos, precioLibra, total))

ordenSuper = 'Fui a {2} y compre {0} libras de frijoles a un precio de {1} dolares cada libra y gaste un total de {3}'

print(ordenSuper.format(superMercado, cantidadGranos, precioLibra, total))

#################################################

superMercado = 'La despensa de Don \'Isaias\''
print(superMercado)

#################################################

#Ejercicio 1
mensaje = 'Programacion es arte y ciencia, un lenguaje que crea la realidad una forma de dar vida a la inteligencia, y al mundo digital una identidad.'

print(mensaje.split())

#Ejercicio 2
alphabet = "abcdefghijklmnopqrstuvwxyz"

print('Primeras 10 letras del abecedario: ', alphabet[0:10])

print('Ultimas 10 letras del abecedario: ', alphabet[-10:])

print('Abecedario alreves: ', alphabet[::-1])








