NombreUsuario = 'Cristian Velasco'
print(f'¡Hola,{NombreUsuario}! Bienvenido a muestro programa.')
print('¡Hola, %s! Bienvenido a nuestro progama.'%(NombreUsuario))


base = 5
altura = 7

areaTriangulo = base*altura/2

print('El area del triangulo es %.2f'%(areaTriangulo))

nombreUsuario = 'Jairo Velasco'
edadUsuario = '30'
ciudadRecidencia= 'Soyapango'

print(f'{nombreUsuario},{edadUsuario},{ciudadRecidencia}')

x = 1

y = 1.45654

z = 2j 

type (x), type(y), type(z)

ejemploInt1 = 32322
ejemploInt2 = -565655
ejemploInt3 = 2
ejemploInt4= 0

print(type(ejemploInt1), type(ejemploInt2), type(ejemploInt4))

x = 35E3
y = 12e4

print(type(x),type(y))

x = 3+5j

y = -5j

print(type(x),type(y))

print(type(3))
print(type(3.14))
print(type(1+8j))
print(type('hello word'))
print(type([1,2,3]))
print(type({1: 'one', 2: 'two', 2: 'three'}))
print(type({1, 2, 3}))
print(type((1, 2, 3)))


totalContador = 0

for i in range(1,5): 
    totalContador = totalContador + i

    print('el tipo de de la variable es:',type(totalContador), 'y su valor final es:',totalContador)


notas = [7.0, 6.0, 9.0, 10.0]

promedio = sum(notas)/len(notas)

print('promedio de notas es',promedio)

usuarioRegistrado = False

if usuarioRegistrado:
    print('Bienvenido al curso')
else:
    print('El usuario no esta en el curso')

nombres = ['Cristian','Denis','Edwin','Velasco']

print(f'lista de nombre:{nombres}')


diaSemana = ('L', 'M', 'M', 'J', 'V')

numeros = (1,2,3,4,5)

print(diaSemana)
print(type(diaSemana)) #saber el tipo de caracter 

print(numeros)
print(type(numeros))


a = 'Hello world:Hola mundo'
b = 'Holaaaaaaaaaaaa'

print(len(a),len(b)) #saber la longitud de un escrito 

print(a[2:15])
print(b[4:5])

#1
mensaje = 'Bienvenido a Python'
print(mensaje)

#2
print(len(mensaje))

print(mensaje[13:19])


subcadena = mensaje[13:19] #crear una subcadena con un recorte

print(subcadena)

#3
cadena='abcdefghij'
print(len(cadena))

print(cadena[2:6])

#4
Mensaje='Python es genial'

print(len(Mensaje))

print(Mensaje[7:16]) #para cortar un mensaje

parte = Mensaje[7:16]

Mensaje='    Python es genial     '
print(Mensaje.strip()) #para separar cada palabra

#Tarea

print('Programar es arte y ciencia, un lenguaje que crea la realidad, una forma de dar vida a la inteligencia, y al mundo digital una identidad'.split())

abecedario = 'abcdefghijklmnopqrstuvwxyz'
print(abecedario[::-1])