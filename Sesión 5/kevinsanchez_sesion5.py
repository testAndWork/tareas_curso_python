#Sentencias IF
"""num = int(input("inserte el numero a comparar : "))

if(num % 2 == 0):
    print(f'El numero es par {num}')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

contrasenia = input('Ingrese la contraseña: ')

if contrasenia == 'entrada123':
    print('Contraseña Correcta')

#########################################################

#Sentencia ELIF
x = 7
y = 3

if x > y:
    print(f'El numero mayo es x = {x}')
elif x == y:
    print('Los numero son iguales')
""""""""""""""""""""""""""""""""""""""""""""""""""""""
if x > y:
    print(f'El numero mayo es x = {x}')
elif x == y:
    print('Los numero son iguales')
else:
    print('El numero mayo es y = {y}')
""""""""""""""""""""""""""""""""""""""""""""""""""""""
if x > y:
    print(f'El numero mayo es x = {x}')
else:
    print('El numero mayo es y = {y}')"""

#########################################################

"""
Elaborar una solucion la cual, dado un valor, verifique si es positivio
negativo o es cero

numero = float(input("Digite un numero: "))

if numero > 0:
    print('El numero es positivo')
elif numero < 0:
    print('El numero es negativo')
else:
    print('El numero es cero')"""

#########################################################
#Abreviaciones

"""a = 6
b = 3

if a > b : print('a is greater than b')
""""""""""""""""""""""""""""""""""""""""""""""""""""""
contrasenia = input('Ingrese la contraseña: ')

if contrasenia == 'entrada123': print('Contraseña Correcta')
""""""""""""""""""""""""""""""""""""""""""""""""""""""
a = 3

print('a es positivo') if a > 0 else print('a es negativo')

if a > 0:
    print('a es positivo')
else:
    print('a es negativo')


a = 2
b = 5

print('El mayor es A') if a > b else print('El mayor es B')

print('El mayor es A') if a > b else print('A y B son iguales') if a == b else print('El mayor es B')"""
#########################################################

"""
Verificar si un numero es Par que imprima 'El numero es par' en caso contrario que 
imprima es impar 


valor = float(input('Ingrese un numero: '))

print('El numero es par') if valor % 2 == 0 else print('El numero es impar')"""

#########################################################
#Calcular descuento 

"""valorCompra = 100.9

if valorCompra >= 100:
    descuento = 0.15
    preciaFinal = valorCompra - valorCompra * descuento
    print(f'El precio final a pagar es: {preciaFinal}')
else:
    descuento = 0.10
    preciaFinal = valorCompra - valorCompra * descuento
    print(f'El precio final a pagar es: {preciaFinal}')

valorCompra = 85

descuento = 0.15 if valorCompra >= 100 else 0.10
preciaFinal = valorCompra - valorCompra * descuento
print(f'El precio final a pagar es: {preciaFinal}')"""
#########################################################
#Calculo del salario de un empleado
# 10,000 -> 30% de impuesto
# 5,000 -> 205 de impusto
#menos de lo anterior 10%

"""ingreso = 9000
impuesto = 0.30 if ingreso > 10000 else 0.2 if ingreso > 5000 else 0.1
impuestoAPagar = ingreso * impuesto
salario = ingreso - impuestoAPagar
print(f'El salario del empleado es: {salario}')"""
#########################################################

#Operador Logico
"""a = 220
b = 33
c = 500

if a>b and c>a:
    print('Both conditions are True')
""""""""""""""""""""""""""""""""""""""""""""""""""""""
edad = 20
estatura = 165

if edad >= 18 and estatura >= 160:
    print('Eres apto para escalar una montaña')
else:
    print('No cumples los requisitos')"""
#########################################################
#Servicio de cable

"""pago = True
membresia = True
accesoContenido  = membresia and pago

if accesoContenido:
    print('Bienvenido a nuestro programa')
else:
    print('Pago o membresia invalida')"""
#########################################################

#Calculos de notas
"""nota = 7

if nota >= 0 and nota <= 0:
    print('Nota Valida')
elif nota == 0:
    print('Nota es cero')
else:
    print('Nota fuera de rango')
#########################################################

#Verificar si el valor dado es un numero par y entero positivo,
#impar y entero positivo
#valor es cero
#vaalor es negativo

valor = float(input('Digite un numero: '))

if valor > 0 and valor % 2 == 0:
    print('Es un numero positivo y par') 
elif valor > 0 and valor % 2 != 0:
    print('Es un impar positivo')
elif valor==0:
    print('El numero es cero')
else:
    print('El numero es negativo')"""
#########################################################

#Operador OR
"""a = 200
b = 33
c = 500

if a > b or a > c:
    print('At least one of the conditions is True')
#########################################################

#Verificar si un año es bisiesto
anio = 2012

anioBisiesto = True if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0 else False
print(anioBisiesto)"""
#########################################################

#Clasificacion de un triangulo
#Equilatero -> 3 lados iguales
#Isoceles -> 2 lados iguales
#Escaleno -> no tiene lados iguales

"""lado1 = 3
lado2 = 3
lado3 = 3

if lado1 == lado2 == lado3:
    print('el triangulo es equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('El triangulo es Isoceles')
else:
    print('El triangulo es Escaleno')"""
#########################################################

"""a = 33
b = 200
if not a > b:
    print('a is NOT greater than b')

b = 45
a = 4

if not b > a:
    print('b>a')
#########################################################

a = 0

if a > 0:
    if a % 2 == 0:
        print('Es par y positivo')
    else:
        print('impar y positivo')
elif a == 0:
    print('El numero es cero')
else:
    print('Es negativo')"""
#########################################################

#Validacion de ticket
"""validacionEntrada = True
validacionPelicula = True

if validacionEntrada and validacionPelicula:
    print('tienes derecho al descuento del parque')
    
#########################################################
condicionPrincipal = True
condicionAlternativa = False

if condicionPrincipal:
    pass
elif condicionAlternativa:
    pass
else:
    pass
""""""""""""""""""""""""""""""""""""""""""""""""""""""
condicion = False

if condicion:
    pass
else:
    print('La condicion no se cumple')"""
#########################################################

"""mi_edad = int(input('Digite la edad: '))

tu_edad= int(input('Digite tu edad: '))

if mi_edad > tu_edad:
    result = mi_edad - tu_edad
    print(f'Tengo {result} años mas que tu')
    if mi_edad != tu_edad + 1:
        print('Eres un año mayor que yo')
    elif mi_edad < tu_edad:
        result = tu_edad - mi_edad
        print(f'Tu tienes {result} años que yo')"""
#########################################################

#1
"""valor = float(input('Digite un numero: '))

if valor > 0:
    print('El numero es positivo')
elif valor == 0:
    print('El numero es cero')
else:
    print('El numero es negativo')"""

#2
"""valor = int(input('Digite un numero: '))

if valor % 2 == 0 and valor % 3 == 0:
    print('El numero es par y es divisble entre 3')
    if valor % 2 != 0 and valor % 3 == 0:
        print('El numero es impar y divisible entre 3')
    else: 
        print('El numero es impar y no es divisible entre 3')
else:
    print('El numero es par y no es divisible entre 3')"""
    
#3
"""letra = input('Ingrese una letra: ')

if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print('La letra es una vocal')
else:
    print('La letra es una consonante')"""

#4
age = int(input('Digite la edad: '))

if age > 18:
    print('Eres lo suficiente mayor para conducir')
elif age < 18:
    print('Te faltan mucho para poder conducir')



"""
mia = 27
tio = 47

tio > mia
result = mi_edad - tu_edad = 20
if result >= 1
imprime años
else: año

result > 1
tu eres mayor 20 años
else
tu eres un año mayor 
"""
#5
"""mi_edad = int(input('Digite la edad: '))
tu_edad= int(input('Digite tu edad: '))

if mi_edad > tu_edad:
    result = mi_edad - tu_edad
    if result > 1:
        print(f'Tienes {result} años ')
    if mi_edad == tu_edad:
        print(f'Tu tienes {result} la misma edad que yo')
    elif mi_edad < tu_edad:
        result = mi_edad - tu_edad
        print('')"""
    





