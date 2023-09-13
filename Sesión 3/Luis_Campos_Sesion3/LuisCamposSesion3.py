#Ejercicio1
nombreUsuario = 'Jose Luis Campos'
print (f"hola {nombreUsuario} Bienvenido a nuestro programa")
print ("hola",nombreUsuario, "Bienvenido a nuestro programa")
print ("hola %s Bienvenido a nuestro programa" %(nombreUsuario))
#Ejercicio 2
base = 5
altura = 7
areaTriangulo = base*altura/2
print("El Area de tu triangulo es:", (base*altura) / 2)
print ('el area del triangulo es: %.2f'%(areaTriangulo))

nombreUsuario = 'Jose luis campos'
edadUsurio ='22'
ciudadResidencia= 'san martin'

print (f'{nombreUsuario},{edadUsurio},{ciudadResidencia}')

x = 5
print(type(x))

x = 1
y = 1.45654
z = 2j
type (x)
type(y)
type(z)
ejemploInt1 = (32424)
ejemploInt2 = (-1312342)
ejemploInt3 = 2
ejemploInt4 = 0

print (type (ejemploInt1),type(ejemploInt2),type(ejemploInt3),type(ejemploInt4))

x = 35E3
y = 12E4
z =1.2e4
print(x,y,z)
print(type(x),type(y),type(z))
print(type(12*10**4))


x = 3+5j
y = -3j
z = -3+0j
print(type(x),type(y),type(z))

#practica
print(type(3))
print(type(3.14))
print(type(1+8j))
print(type("hello word"))
print(type([1,2,3]))
print(type({1:"one",2:"two",3:"three"}))
print(type({1,2,3}))
print(type((1,2,3)))

dato = '1200'
hora = 34
sueldo = dato*hora

print (sueldo)

#int: para un contador de bucle
totalContador = 0 
for i in range(1,5):
    totalContador = totalContador + i
print('el tipo de la variable totalcontador es ',type(totalContador), 'y su valor final es ',totalContador)

#Calcular notas
notas = [7.0,6.0,9,10.0]
promedio = sum(notas)/len(notas)
print('el promedio de notas es',promedio)

#bool validar campos
usarioRegistrado = False

if usarioRegistrado:
    print('bienvenido al curso')
else:
    print('el usuario no esta en el curso')

#list: tipo str
nombre = ['cristian','dennis', 'henry','roberto']
print (F'LISTA DE NOMBRES:{nombre}')

#tuple dias de la semana 
diasSemanas = ('l','m','m','j','v','s','d')
numeros = (1,2,3,4,5)
print(numeros)
print(type(numeros))

print(diasSemanas)
print(type(diasSemanas))

#dic nombres y contactos 
dictContactos ={
    'cristian': 752342,
    'dennis':145544, 
    'henry':142578,
    'roberto':144114
    }
print(type(dictContactos))

#convertir tipo de datos numericos
x = 1
y = 2.8
z = 3j
print (type(x),type(y),type(z))

convertX = float(x)
convertY = complex(y)
#convetZ = int(z) no es posible
print(convertY,convertX)
print (type(convertX),type(convertY))


#forma 1
edadUsuarios = input('ingrese la edad del usuario:')
edadUsuarios = int(edadUsuarios)
print(type(edadUsuarios))
print('la edad de usuarios :', edadUsuarios)

cadena = '3.75'
strFloat = float(cadena)
print(type(cadena),type(strFloat))
print(cadena+cadena)
print(strFloat+strFloat)


#int cadena 
entero = 45 
print(type(entero))
cadenaInt = str(entero)
print(type(cadenaInt))

#float cadena 
flotante = 4.5 
print(type(flotante))
cadenafloat = str(flotante)
print(type(cadenafloat))


lista = [1,2,3,4,5] 
print(type(lista))
cadenaList = str(lista)
print(type(cadenaList))

cadena = '[1,2,3,4,5] '
listas = eval(cadena)
print(type(lista))
print(lista)

a = "hello"
b = 'hello'
print(a)
print(b)

a = "helle, word : hola, mundo"
b = 'no se me ocurre nada'

print(len(a), len(b))

print(a[2:21])
print(b[4:5])
print(a[0:10])
print(b[17:20])

print (a[-5:-2])
print (b[4:2])

listas1 = [1,2,3,4,5,6,7,8,9,10]
print (listas1[-1])
print (listas1[-2])
print (listas1[-5])
print (listas1[-7])
print (listas1[-8])
#1
mensaje = 'Bienvenido Python'
print(mensaje)
#2
cadenaMulti = 'Vuestro amigo, es la respuesta a vuestras necesidades'
poema = str(cadenaMulti)
print(poema)

#3
cadena = 'programcion Python'
sudacadena = cadena[12:18]

print(sudacadena)

#4
cadena = 'abcdefjhij'
print(cadena[2:6])

#5
cadena = 'Python es genial'
parte = cadena[7:]
print(parte)

print(a.upper())
print(a.lower())


a = '    hello, word'
print(a)
print(a.strip())
print(a.replace('h','j'))
print(a.replace('llo','lou'))
print(a.split(','))
print(a.split('o'))

b = '    1,2,3,4    '
print(b)
print(b.strip())

a = 'hello'
b = 'word'
print(a+b)


edad = 34
cadena = 'mi nombre es Texto y tengo {}'
print(cadena.format(edad))

superMercado = 'La despensa de don juan'
cantidadComida = 3
precioLibra = 1.40
total = precioLibra*cantidadComida
ordenSuper = 'fui a {} y compre {} libras de frijoles a un precio de {} dolares cada libra y gaste un total de {}dolare'
print(ordenSuper.format(superMercado,cantidadComida,precioLibra,total))

#Tarea

#Ejerecio 1
programacion = 'Programacion es arte y ciencia, un lenguaje que crea la realidad, una forma de dar vida a la inteligencia, y al mundo digital una identidad'
print (programacion.split())
#Ejercio 2
abecedario = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
print(len(abecedario))
print(abecedario[:20])
print(abecedario[32:51])
print (abecedario[::-1])
