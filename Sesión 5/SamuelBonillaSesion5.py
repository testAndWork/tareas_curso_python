#Verificar si el numero dado es un numero par.

numero = int(input("Inserte el numero a verificar"))

if numero % 2 == 0:
    print(f"El numero es par {numero}")

# Verificar contraseña

contrasenia = input("Ingrese la contraseña: ")

if contrasenia == "entrada123":
    print("Contraseña Correcta")

#Sangria

contrasenia = input("Ingrese la contraseña: ")

if contrasenia == "entrada123":
    print("Contraseña Correcta")

#elif
x = 3
y = 7

if x > y :
    print(f"El numero mayor es x: {x} ")

elif x == y:
    print(f"Los numeros son iguales")

#Else

x = 3
y = 7

if x > y :
    print(f"El numero mayor es x: {x} ")

elif x == y:
    print(f"Los numeros son iguales")

else:
    print(f"El numero mayor es y : {y} ")

# Elaborar una solucion en la cual , dado un valor, veriifque si es positivo o si es negativo o si es cero

valor = int(input("Ingrese un numero: "))

if valor >= 1 :
    print(f"El numero es positivo {valor}")

elif valor == 0 :
    print(f"El valor es cero {valor}")

else:
    print(f"El valor es negativo {valor}")

#Sentencia if corta o abreviada
a = 6
b = 3
if a > b: print("a is greater than b")

#Sentencia else if abreviada

a = 3

print("A es positivo") if a>0 else print("A es negativo")

if a>0: 
    print("A es positivo")
else:
    print("A es negativo")

#Practica
number = int(input('Ingrese un numero: '))

print(f'El numero es par: {number}') if number % 2 == 0 else print(f'El numero es impar: {number}')

#Ejemplo

valorCompra = 50

if valorCompra >=  100:
    descuento = 0.15
    precioFinal = valorCompra - valorCompra*descuento
    print(f"El precio final es: {precioFinal}")
else:
    descuento = 0.10
    precioFinal = valorCompra - valorCompra*descuento
    print(f"El precio final es: {precioFinal}")

#Practica

valorCompra = 85

descuento = 0.15 if valorCompra >=  100 else 0.10
precioFinal = valorCompra - valorCompra*descuento
print(f"El precio final es: {precioFinal}")

#Calculo del salario
# $10,000 -> 30% del impuesto
# $5,000 -> 20% del impuesto

ingreso = 4800

impuesto = 0.30 if ingreso > 1000 else 0.2 if ingreso > 5000 else 0.1

impuestoaPagar = ingreso*impuesto

salario = ingreso - impuestoaPagar

print(f"El salario del empleado es: {salario}")

#operador logico and

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both Condition are True")

#verificacion de datos

edad = 20
estatura = 165

if edad >= 18 and estatura >= 160:
    print("Eres apto para escalar una montaña")
else:
    print("No cumples los requisitos")

#Servicio Netflix o Disney

pago      = True
membresia = True

acceso_a_contenido = membresia and pago

if acceso_a_contenido:
    print("Bienvenido a nuestros programas")
else:
    print("Pago o membresia invalida")

#Calculo de nota final

nota = 7

if nota >= 0 and nota <= 10:
    print("Nota valida")
elif nota == 0:
    print("Nota es cero")
else:
    print("Nota invalida fuera de rango")

#Practica
#Verificar si es valor es numero par y entero positivo
#impar y entero positivo
#valor es cero
#valor es negativo

valor = 1

if valor > 0 and valor % 2 == 0:
    print("es un numero positivo y par")
elif valor > 0 and valor % 2 != 0:
    print("es un impar positivo")
elif valor == 0:
    print("el numero es cero")
else:
    print("el numero es negativo")

#operador logico or

a = 200
b = 33
c = 500

if a > b or c > a:
    print("At least one of the condition is True")

#verificar si un año es biciesto

anio = 1998

anioBisiesto = True if (anio % 4 == 0 and anio % 100 !=0) or anio %400 == 0 else False

print(anioBisiesto)

#calificar un triangulo
#Equilatero -> tres lados iguales
#Isosceles -> dos lados iguales
#Escaleno -> no tiene lados iguales

lado1= 4
lado2= 4
lado3= 3

if lado1 == lado2 == lado3:
    print("Triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: 
    print("Triangulo es isosceles")
else:
    print("Triangulo es escaleno")

#Operador logico not
a = 33
b = 200

if not a > b:
    print("At least one of the condition is True")

b = 45
a = 4
if not b > a :
    print("b > a ")

#Setencia if anidados

a = 10
if a > 0:
    if a % 2 == 0:
        print("Es par y positivo")
    else:
        print("impar y positivo")
elif a == 0:
    print("El numero es cero")
else:
    print("es negativo")

#Declaracion Pass

if condicion_principal:
    #Bloque de codigo principal
    pass
elif condicion_alternativa:
    #Bloque de codigo alternativo
    pass
else:
    #Bloque de codigo por defecto
    pass

condicion = False
if condicion:
    pass
else:
    print("La condicion no se cumple")

#Practica
mi_edad = int(input('Ingresa mi edad: '))
tu_edad = int(input("Ingresa tu edad"))

if mi_edad > tu_edad:
    resultado = mi_edad-tu_edad
    print(f'tengo {resultado} años mas que tu')
    if mi_edad != tu_edad + 1:
        print('tienes un anio mas que yo')
elif mi_edad < tu_edad:
    resultado = tu_edad - mi_edad
    print(f'tu tienes {resultado} años mas que yo')

else:
    print('Tenemos la misma edad')

#Aplicando conocimientos

#Ejercicio 1

numero = int(input("Ingrese un numero: "))

if numero >= 1:
    print("Es un numero positivo")
elif numero == 0:
    print("El numero es cero")
else:
    print("Es un numero negativo")

#Ejercicio 2

numeroEntero = int(input("Ingrese un numero: "))

if numeroEntero % 2 == 0 and numeroEntero % 3 == 0:
    print("Es par y Es divisible entre 3")
elif numeroEntero !=0 and numeroEntero % 3 == 0:
    print("Es impar y Es divisible entre 3")
else:
    print("El numero no tiene ninguno de las condiciones")

#Ejercicio 3

letra = input("Ingrese una letra: ")

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("La letra es una vocal")
elif letra == "B" or letra == "C" or letra == "D" or letra == "F" or letra == "G" or letra == "H" or letra == "J" or letra == "K" or letra == "L" or letra == "M" or letra == "N" or letra == "P" or letra == "Q" or letra == "R" or letra == "S" or letra == "T" or letra == "V" or letra == "W" or letra == "X" or letra == "Y" or letra == "Z":
    print("La letra es una consonante") 
else:
    print("No es una letra")

#Ejercicio 4

edad = int(input("Ingrese tu edad: "))

if edad >= 18:
    print("Eres lo suficientemente mayor para conducir")
else:
    print("No eres mayor de edad, te falta", 18 - edad, "años")

#Ejercicio 5

mi_edad = int(input("Ingrese mi edad: "))
tu_edad = int(input("Ingrese tu edad: "))

if mi_edad > tu_edad:
    edad = mi_edad-tu_edad
    print(f"Tengo {edad} años mayor que tu")
    if mi_edad != tu_edad + 1:
        print('tienes un año mas que yo')
elif mi_edad < tu_edad:
    edad = tu_edad-mi_edad
    print(f"Tienes {edad} años mayor que yo")
else:
    print("Tenemos la misma edad")