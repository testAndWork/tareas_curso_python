#Suma

print(10+5)

a, b= 5,3

#operador suma
c = a + b
print(c)

#operador resta
c = a - b
print(c)

c = b - a
print(c)

#operador multiplicacion
c = a * b
print(c)

#operador division
c = a / b
print(c)

#Division Entera
c = a // b
print(c)

#Modulo
c = a % b
print(c)

#Potenciacion
c = a ** b
print(c)

#Combinaciones de operadores aritméticos

#1
print((4+6)*2)

#2
print(10 ** 2 / 5)

#3
print((15 - 3) * 4 / 2)

#4
print((27 % 5) + 10)

#5
print(19 // 3 - 2)

#6
print(((5 + 2) * 3) **2 / (10 % 3))

#7
#f(x)=(2 * x) + (3 * x) - (5 / x)
#f(4)

x = 4
print((2 * x) + (3 * x) - (5 / x))

#Ecuacion Cuadratica

#6x**2+4x+8=0

import math
a=6
b=9
c=-8

discriminante = b**2 - 4 * a * c
x1 = (-b + math.sqrt(discriminante)) / (2 * a)
x2 = (-b - math.sqrt(discriminante)) / (2 * a)

print(x1,x2)

#Estos resultados son erroneos, ya que no se agruparon correctamente
x1 = -b + math.sqrt(discriminante) / (2 * a)
x2 = -b - math.sqrt(discriminante) / (2 * a)
print(x1,x2)

#operadores de combinacion

X=5
print(x)

X=3
X= X + 4
print(X)

X = 3
X += 4
print(X)

X = 3
X -= 4
print(X)

X = 3
X *= 4
print(X)

X = 3
X /= 4
print(X)

X = 3
X **= 4
print(X)

X = 3
X //= 4
print(X)

X = 3
X %= 4
print(X)

X = 3
X &= 4
print(X)

X = 3
X <<= 4
print(X)

#Practica 1
precioOriginal = 130
porcentajeDescuento = 40

Descuento = precioOriginal * (porcentajeDescuento)/100

precioFinal = precioOriginal - Descuento

print(precioFinal, Descuento)

#Practica 1.2
precioOriginal = float(input("Ingrese el precio original del producto: "))
porcentajeDescuento = float(input("Ingrese el porcentaje de descuento: "))

descuento = precioOriginal * (porcentajeDescuento / 100)
precioFinal = precioOriginal - descuento

print("El precio final después del descuento es:", precioFinal)

#Practica 2
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su peso en metros: "))

IMC = peso / altura**2
Promedio = IMC

print(f"Su IMC es: %.2f"%Promedio)

#Practica 3
horas = float(input("Ingrese la hora: "))
minutos = float(input("Ingrese los minutos: "))

horasSegundos = horas * 3600
minutosSegundos = minutos * 60

print("Las horas en segundos son:", horasSegundos, "segundos", "y los minutos en segundos son:", minutosSegundos, "segundos")

#Practica 4
montoComida = float(input("Ingrese el monto de la comida: "))
porcentajePropina = float(input("Ingrese el porcentaje de la propina: "))

propina = montoComida * porcentajePropina
montoPagar = montoComida + propina 

print("El monto total a pagar es: ", montoPagar)

#Practica 5
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_farenheit = (temperatura_celsius * 9/5) + 32

print("La temperatura en grados Farenheit es:", temperatura_farenheit)

#Practica 6
numero1 = float(input("Ingrese el numero 1: "))
numero2 = float(input("Ingrese el numero 2: "))

cociente = numero1 // numero2
residuo = numero1 % numero2

print("El resultado del cociente de los dos numeros son:", cociente, "y el residuo de los dos numeros es:", residuo)

#Operadores logicos

x = 10
y = 17
z = 40

#and para comparar
# 10 < 17 and 17 < 40

print(x < y)
print(y < z)
print(x < y and y < z)

print(x < y)
print(y > z)
print(x < y and y > z)

#or para comparar
# 10 < 17 and 17 < 40

print(x < y)
print(y > z)
print(x < y or y > z)

#not para comparar
print(not x < y)
print(not y > z)
print(not (x < y or y > z))


#operador is not

x = [1, 2, 3]
y = x

z = [1, 2, 3]

print(x is y)
print(x is z)
print(x is not z)
print(x is not z)

lista = [1, 2, 3, 4]
print(3 in lista)
print(7 in lista)

#precedencia

x = 6
y = 2

z= (x + y) + 2**4
print(z)

#Aplicando conocimiento

a=8
b=5
c=7

resultado1= a + (b * c)
resultado2= (a + b) * c
resultado3= (a / b) * c
resultado4= a / (b * c)
resultado5= (a ** b) + c
resultado6= a ** (b + c)

print("Resultado 1:", resultado1, "\n""Resultado 2:", resultado2, "\n""Resultado 3:", resultado3, "\n""Resultado 4:", resultado4, "\n""Resultado 5:", resultado5, "\n""Resultado 6:", resultado6)
