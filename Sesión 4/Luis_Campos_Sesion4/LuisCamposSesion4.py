#
print (10+5)

a = 5
b = 3
#suma 
c = a + b

print(c)

#resta
d = a-b
e = b-a
print(d)
print(e)

#mulriplicacion
c= a*b
print(c)

#division
c= a/b
print (c)
#division entera
c = a//b
print (c)
#modulo
c = a%b
print(c)

#potenciacion
c = a**b
print(c)
##Combinacion es de operadores aritmeticos
#1
a= 4
b= 6
c = (a+b)*2
print(c)
print(10**2/5)
a=15
b=3
c= (a-b)*4/2
print(c)
a= 27
b=5
c=(a%b)+10
print(c)
print(19//3-2)

print(((5+2)*3)**2/(10%3))

x = 4
print((2*x) + (3 *x) - (5/x))
import math 
a=6
b=9
c=-8
discriminante = b**2-4*a*c
x1= (-b+ math.sqrt(discriminante)) / (2*a)
x2= (-b- math.sqrt(discriminante)) / (2*a)
print(x1,x2)

x= 5
print(x)
x=3
x = x+4
print(x)

x = 3 
x += 4
print(x)

x = 3 
x -= 4
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

x = 3 
x <<= 4
print(x)

precioOriginal= 30
precioDescuento = 3
descuento = precioOriginal*precioDescuento/100
precioFinal = precioOriginal-descuento
print('su precio origina es:',precioOriginal)
print('su precio con el descuento es:',precioFinal)


pesoKilogramos= 68
alturaMetros = 1.65

imc = pesoKilogramos/(alturaMetros)**2

print('su imc es:',imc)


horas = int(input("Ingrese las horas a calcular: "))
minutos = int(input("Ingrese las minutos a calcular: "))
segubdosMinutos = minutos*60
segundosHora = horas*3600
print('La conversion de minutos a segundos es:',segubdosMinutos)
print('La conversion de horas a segundos es:',segundosHora)

totalComida= 30
propina = 10
porcentajePropina = totalComida*propina/100
totalFinal = totalComida+porcentajePropina
print('su precio original es:',totalComida)
print('su precio con la propina es:',totalFinal)

temperaturaCelsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperaturaFahrenheit = (temperaturaCelsius * 9 / 5) + 32
print("La temperatura en grados Fahrenheit es: ", temperaturaFahrenheit)

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))

resultad1 = (n1//n2,) 
resultado2 = (n1%n2)

print('el cociente de la division es:',resultad1,'y el resto de la division es:',resultado2)

#ejemplo de and
x= 10
y= 17
z= 40

print(x<y and y<z)

print(x<y and y>z)

print(x<y or y<z)
print(x<y or y>z)
print(x<y)
print(y>z)
print(x<y or y>z)
print(not x<y)
print(not y>z)
print(x<y or y>z)

l1 =[1,2,3]
l2 = l1
l3 = [1,2,3]
print(l1 is l2)
print(l1 is l3)
print(l1 is not l2)
print(l1 is not l3)

#tarea
a = 12
b = 24
c = 8

v1 = a+b*c
v2 = (a+b)*c 
v3 = (a/b)*c
v4 = a/(b*c)
v5 = (a**b)+c
v6 = a**(b+c)

print("El resultado de la variable 1 es:\n",v1,"\nEl resultado de la variable 2 es:\n",v2,
      "\nEl resultado de la variable 3 es:\n",v3,"\nEl resultado de la variable 4 es:\n",v4,
      "\nEl resultado de la variable 5 es:\n",v5,"\nEl resultado de la variable 6 es:\n",v6)

