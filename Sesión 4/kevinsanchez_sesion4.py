#Operadores Aritmeticos
"""
Suma
Resta
Multiplicacion
Division
Modulo 
Exponente
Division de piso //
"""

a = 5
b = 3

#Suma
c = a+b

#Resta
c = a-b
print(c)
c = b-a
print(c)

#Multiplicacion
c = a*b
print(c)

#Division
c = a/b
print(c)

#Division Entera
c = a//b
print(c)

#Modulo
c = a % b
print(c)

#Potenciacion
c = a ** b
print(c)

#Combinacion de operadores

#1
a = 4
b = 6
c = 2

result = ((a + b) *2)

print(result)
###################################
#2
print(10**2/5)

###################################
#3
print((15-3)*4/2)

###################################
#4
print((27%5)+10)

print(27%5)
###################################
#5
print(19//3-2)

###################################
#6
print(((5+2)*3)**2/(10%3))

###################################
#7
x = 4
print((2*x)+(3*x)-(5/x))
###################################
#8 ECUACION Cuadratica

import math

a = 6
b = 4
c = -8

discriminante = b**2-4*a*c

x1 = (-b + math.sqrt(discriminante)) / (2*a)
x2 = (-b - math.sqrt(discriminante)) / (2*a)

print(x1)

###################################
#Operadores de Asignacion
"""
operador
=
+=
-=
*=
/=
%=
//=
**=
|=

==
!=
<
>
<=
>=
"""
###################################
x = 5
print(x)

###################################

x = 4
x = x + 4
print(x)

x = 3
x += 4
print(x)

x = 3
x -= 4
print(x)

x = 3
x *= 4
print(x)

x = 3
x /= 4
print(x)

x = 3
x **= 4
print(x)

x = 3
x //= 4
print(x)

x = 3
x %= 4
print(x)

x = 3
x &= 4
print(x)
#########################################################

#producto = 3.85
#subtotal = producto * 0.1
#total = producto - subtotal

#print('El total del producto es {:.2f}'.format(total))

#############################################

p = float(input("Digite su peso en kg: "))

a = float(input("Digite su altura en m: "))

imc = (p/(a*a))

if imc < 18.5:
    print("Peso Bajo")
    if imc >= 18 and imc<=25:
        print("Normal")
    if imc >= 25 and imc<=30:
        print("Sobrepeso")
else:
    print("Obesidad")
    
print(f'Su indice de masa corporal es: {imc}')

#############################################

h = int(input("Ingrese la hora: "))
m = int(input("Ingrese los minutos: "))

hh = h * 3600
mm = m * 60

print()

#############################################

#Operadores Logicos
"""
and
or
not

c and c
v  v  v
v  f  f
f  f  v
f  f  f

c or c
v  v  v
v  v  f
f  v  v
f  f  f
"""

x = 10
y = 17
z = 40

print(x < y )
print(y < z)

print(x < y and y < z)


print(x < y )
print(y > z)

print(x < y and y > z)

#############################################

print(x < y )
print(y < z)

print(x < y or y < z)

print(x < y )
print(y > z)

print(x < y or y > z)

#############################################

print(not x < y)
print( not y > z)
print(not x < y or y > z)

#############################################

#Operadores de Identidad

x = [1,2,3]
y = x
z = [1,2,3]

print(x is y)
print(x is z)


print(x is not y)
print(x is not z)

#############################################

#Comentario por linea
lista1 = [1,2,3,4]
print(3 in lista1)
print(7 in lista1)

#############################################
x = 6
y = 2

z = (x+ y) *2**4

#############################################

#####Practica
#1
producto = 100
subtotal = producto * 0.1
total = producto - subtotal

print('El total del producto es {:.2f}'.format(total))

#2
p = float(input("Digite su peso en kg: "))

a = float(input("Digite su altura en m: "))

imc = (p/(a*a))

if imc < 18.5:
    print("Peso Bajo")
    if imc >= 18 and imc<=25:
        print("Normal")
    if imc >= 25 and imc<=30:
        print("Sobrepeso")
else:
    print("Obesidad")
    
print(f'Su indice de masa corporal es: {imc}')

#3
h = int(input("Ingrese la hora: "))
m = int(input("Ingrese los minutos: "))

hh = h * 3600
mm = m * 60

print(f'las horas en segundos es: {hh}')
print(f'Los minutos en segundo hay: {mm}')

#4
cuenta = float(input('¿Cuál es el monto total a pagar de la cuenta?: '))
porcentaje = float(input('¿Cuál será el porcentaje de la propina a pagar? 10%,15%,20%?: '))

propina = cuenta * (porcentaje/100)

print(f"El total a pagar es: {cuenta}")
print(f'Total de propina es: {propina}')

#5
temp_celcius = float(input("Ingrese la temperatura en grados celcius: "))
temp_farenheit = (temp_celcius * 9/5) + 32

print(f'La Temperatura en grados fahrenheit es: {temp_farenheit}')

#6
num1 = int(input('Ingrese numero: '))
num2 = int(input('Ingrese numero: '))

result = (num1//num2, num1%num2)

print(f'El cociente de la division es {result[0]} y el resto de la division es {result[1]} ')

#############################################

a = 10
b = 35
c = 50

result1 = a + b * c
print(f'El resultado es: {result1}')

result2 = (a + b) * c
print(f'El resultado es: {result2}')

div = (a / b)
result3 = div * c
print(f'El resultado es: {.2}'.format(result3))

mul = b * c
result4 = a / mul
print('El resultado es: {:.4}'.format(result4))

result5 = (a**b) + c
print(f'El resultado es: {.2}'.format(result5))

result6 = a**(b + c)
print(f'El resultado es: {.2}'.format(result6))



