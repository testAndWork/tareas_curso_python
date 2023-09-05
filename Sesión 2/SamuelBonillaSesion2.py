#Ejercicio1
resultado = max(5, 10, 3, 8)        
print(resultado)

#Ejercicio2
resultado = round(3.14159, 2)
print(resultado)

#Ejercicio3
resultado = min(5, 10, 3, 8)
print(resultado)

#Practica
nombre = 'Samuel Bonilla'
edad = 19
longituddelnombre = len(nombre)
print('Mi nombre es', nombre, 'mi edad es', edad)
print('La longitud del nombre es:', longituddelnombre)

#Uso de la funcion print()-> Imprimir un mensaje en la consola
print('Hola mundo')

#Ejemplo
nombre = 'Juan'
edad = 23
print('mi nombre es ', nombre, 'y mi edad es', edad)


#len()-> nos muestra la longitud de una cadena de caracteres
mensaje = 'buenas tardes, este es un Hola mundo'
Longitud = len(mensaje)
print('La longitud del mensaje es:', Longitud)


#type()
valor = 23
mensaje = 'Buenas tardes, este es hola mundo version2'
print('El tipo de dato de la variable es:', type(valor))

print('El tipo de dato de la variable es:', type(mensaje))

#Ejemplo
cadena = '123'
print('El tipo de dato es la variable cadena es: ', type(cadena))
cadena = int(cadena)
print('El tipo de dato es la variable cadena es: ', type(cadena))

cadena + cadena

#Ejemplo
valor = 14
print('El tipo de dato de la variable es: ', type(valor))

valor = float(valor)
print('El tipo de dato de la variable es: ', type(valor), valor)

#Ejemplo
if True:
    print('Es una prueba de identacion:', 3 + 4)

#Practica
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

#Camel Case
miVariableEjemplo
nombreUsuario
calcularImpuesto

#Pascal Case
miVariableEjemplo
nombreUsuario
crearUsuario

#Snake Case
numero_de_telefono
cantidad_de_prodcutos
mi_variable_ejemplo

#Lower Case
mivariableejemplo
cantidaddeproductos
nombre

#Upper Case
PI
MAXIMO_VALOR
MIVARIABLEEJEMPLO

#Ejemplo
def saludar(nombre):
    mensaje = 'Hola, ' + nombre + '!'
    print(mensaje)

saludar("Alice")

""" Este es un comentario de multilinea,
#aca escribo todo lo que quiera
"""
print('Hola Mundo')

#Ejemplo
x = 10
print(x)

y = 'Jhon'
print(y)

10*y

#Practica
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

#Practica
x, y, z = 2, 'sandia', 23.3

print(x, y, z)
print(x,'\n\n', y,'\n',z,'\n\n\n')

#Ejemplo
x = 'Python is awesome'
y = 'incredible'
z = 'and is easy'

print(x,y,z)
print(x + y + z)

#Practica
m, n, o = 1,2,3
print(m,n,o)

print(m + n + o)

print('La multiplicacion es', 2+3+5,'y la multiplicacion es', 10*2)

#Impresion de strings basicos
print('Hola Mundo')

#Imprimir varias variables en una linea

_nombre = 'Samuel Bonila'
_edad = 19

print('Mi nombre es:', _nombre, 'y tengo', _edad, 'años')

valor_Hora = 17.5
total_horas = 8

sueldodiario = valor_Hora*total_horas

print('Nombre Empleado', _nombre,
'El precio por hora trabajada', valor_Hora,
'y el sueldo diario es:',sueldodiario)

#practica
nombre= 'Juan'
edad = 37
valorHora = 17.5
totalHoras = 8
sueldoDiario = valorHora*totalHoras

print(f'mi nombres es {nombre} y tengo {edad} años.')

print(f'Nombre empleado: {nombre}\n El precio por hora trabajada: {valorHora}\n y el sueldo es: {sueldoDiario}')

print('Mi nombre es %s y tengo %d años.\n\n'%(nombre, edad))

#Ejemplo
nombre = 'Alice'
edad = 30
peso = 120

print('Mi nombre es %s y tengo %d años %d.\n\n'%(nombre,peso,edad))

#Ejemplo
nombre = 'Alice'
preciohora = 17.5
horasTrabajadas = 44

print('Mi nombre es %s, cobro: %d por hora y trabajo %.2f\n\n'%(nombre,horasTrabajadas,preciohora))
print('Mi nombre es %s, cobro: %d por hora y trabajo %.3f\n\n'%(nombre,horasTrabajadas,preciohora))

#Tabulacion en la impresion y salto de lineas

print('Nombre: \t José \n Edad: \t 37')

#Tabulacion en la impresion y salto de lineas

print('Nombre: \n\t José \n Edad: \n\t 37')

#Ejemplo
print('Hola', end= '')
print('mundo')

#Ejemplo 
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

#Ejemplo
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

#Ejemplo
x = str(3)
y = int(3)
z = float(3)

print(4*x)
print(x,y,z)

#Tarea en casa
#Aplicando Conocimientos #1
nombres = "Samuel Ernesto"
primerApellido = "Bonilla"
segundoApellido = "Arias"
edad = 19
nacionalidad = "Salvadoreño"
sexo = "Masculino"

print(f'Mi nombre es {nombres}, mi primer apellido es {primerApellido}, mi segundo apellido es {segundoApellido}, tengo {edad} años de edad, soy {nacionalidad}, y soy {sexo}, estoy en el curso de Python para aprender')
print(f'Mi nombre es {nombres}\n mi primer apellido es {primerApellido}\n mi segundo apellido es {segundoApellido}\n tengo {edad}\n años de edad soy {nacionalidad}\n y soy {sexo}\n estoy en el curso de Python para aprender')
