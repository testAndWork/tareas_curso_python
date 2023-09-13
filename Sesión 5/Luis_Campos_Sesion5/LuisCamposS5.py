#verificar si el numero dado es numero par
numero = int(input('inserte el numero a verificar:'))
if numero%2 == 0:
    print(f'el numero es par {numero}')
print ('La contraseña esentrada123')
#verificar cotraseña
contraseña = input('ingrese la contraseña')
if contraseña == 'entrada123':
    print('contrseña correcta ')

x = 3
y = 7
if x > y :
    print(f'El numero mayor es x = {x}')
elif x == y :
    print('los numeros don iguales')


x = 3
y = 3
if x > y :
    print(f'El numero mayor es x = {x}')
elif x == y :
    print(f'los numeros son iguales')
else:
    print(f'el numero mayor es y ={y}')


if x > y :
    print(f'El numero mayor es x = {x}')
else:
    print(f'el numero mayor es y ={y}')


#ejercicio1
valor = int(input('ingrese el valor'))
if valor > 0:
    print('el numero es positivo ')
elif valor < 0:
    print('el numero es negativo')

a = 6
b = 3

if a > b : print('a is greater than b')

a = 3
print('A es positivo') if a > 0 else print('A es negativo')
if a > 0:
    print('A es positivo')
else:
    print('A es negativo')

a = 2
b = 5
print('A es mayor') if a > b else print('el mayor es b')
b = 5
print('A es mayor') if a > b else print('a yb son iguales') if a == b else print('el mayor es b')

#ejercicio 2
n1 = int(input('ingrese un numero:'))
print('el numero es par') if n1 %2 == 0 else print('el numero es impar')

cantidadProducto = 50
if cantidadProducto >= 100:
    descuento = 0.15
    preciofinal = cantidadProducto - cantidadProducto * descuento
    print(f'el precio final es {preciofinal}')
else:
    descuento = 0.10
    preciofinal = cantidadProducto - cantidadProducto * descuento
    print(f'el precio final es {preciofinal}')

valorCompra = 85 
descuento = 0.15 if valorCompra >= 100 else 0.10
preciofina = valorCompra-valorCompra*descuento
print(f'el precio final es : {preciofina}')

#calculo de salario
#$10,000 ->30% impuestos
#$5,000 -> 20% impuestos
# menos  de lo anterior 10%

ingreso = 4800
impuesto = 0.30 if ingreso > 10000 else 0.02 if ingreso > 5000 else 0.1
impuestoApagar = ingreso* impuesto
salario = ingreso -impuestoApagar
print(f'el salario del empleado es: {salario}')

a = 200
b = 33
c = 500
if a>b and c>a and c>a:
    print('Both conditions are true')
#verificacion de edad
edad = 20
estatura = 165

if edad >= 18 and estatura >= 160:
    print('eres apto para escalar')
else:
    print('no cumples los requisitos')

# servicio de cable 
membresia = True 
pago = True
acceso_a_contenido = membresia and pago 

if acceso_a_contenido:
    print('Bienvenido  nuestro programa')
else:
    print('pago o membresia invalida')

#calculo de notas final
nota = 0
if nota >= 0 and nota <=10:
    print('nota valida')
elif nota == 0:
    print('nota es cero')
else: 
    print('nota invalida')

# par y entero positivo, impar y entero positivo, valor cero y valor negativo
valor = 6
if valor > 0  and valor% 2 == 0:
    print('es numero positivo y par ')
elif valor > 0 and valor% 2!= 0:
    print('es un impar positivo')
elif valor == 0 :
    print('el valor es cero')
else:
    print('el numero es negtaivo') 

a = 200
b = 33
c = 500
if a>b or a>c:
    print('at least one of the condittions is true')

#verificar si un año es bisiesto

año = 2000
año_bisiesto = True if (año%4 == 0 and año % 100 != 0 ) or año%400 == 0 else False
print(año_bisiesto)

lado1 = 4
lado2 = 4
lado3 = 3

if lado1 == lado2 == lado3:
    print('el lado es equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 ==lado3:
    print('triangulos isoceles')
else:
    print('triangulo escaleno')

a= 33
b= 200
if not a>b:
    print('a is NOT greater than b')

a = 8
if a > 0 :
    if a % 2 == 0:
        print('es par y positivo')
    else:
        print('impar y positivo')
elif a == 0:
    print('el numero es cero')
else:
    print('es negativo')
#validacion de un ticket
validacionEntrda = True
validacionPelicula = True

if validacionEntrda and validacionPelicula:
    print('tienes derecho a descuento de parqueo')
elif validacionEntrda or validacionPelicula:
    print('tienes derecho a un descuento')
else:
    print('te toca pagar las 4 horas de parqueo')

condicionPrincipal = True
condicionAlternativa = False

if condicionPrincipal:
    pass
elif condicionAlternativa:
    pass
else:
    pass
condicion = True
if condicion:
    pass
else:
    print('la condicion nose cumple')
#ejercicio
miEdad = int(input('ingresar edad:'))
tuedad = int(input('ingre edad de acopañante'))
if miEdad > tuedad:
    print('Mi edad es mayor a tu edad:')
    difernciaEdad1 = miEdad - tuedad
    if difernciaEdad1 > 0:
        print('la diferencia de edad es:',difernciaEdad1)
elif tuedad > miEdad :
    print('Tu edad es mayor a mi edad:')
    difernciaEdad2 = tuedad- miEdad
    if difernciaEdad2 > 0:
        print('la diferencia de edad es:',difernciaEdad2)
else:
    print('la edad de ambos son iguales ')

#tarea
# 1 
numero1 = int(input('ingrese un numero entero:'))
if numero1 > 0 :
    print('el numero que ingreso es positivo')
elif numero1 < 0 :
    print('el numero que ingreso es negativo')
else:
    print('el numero que ingreso es 0')
#2
numeroEntero = int(input('ingrese un numero entero:'))
if numeroEntero % 2 == 0 and numeroEntero % 3 ==0:
    print ('el numero es par y divisible entre 3')
elif numeroEntero % 2!= 0 and numeroEntero % 3 ==0:
    print ('el numero es impar y divisible entre 3')
else:
    print('el numero no es divisible entre 3')

#3
letra = input('Ingrese una letra:')
if letra == 'a' :
    print('La letra que ingreso es vocal')
elif letra == 'e' :
    print('La letra que ingreso es vocal')
elif letra == 'i' :
    print('La letra que ingreso es vocal')
elif letra == 'o' :
    print('La letra que ingreso es vocal')
elif letra == 'u' :
    print('La letra que ingreso es vocal')
elif letra == 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'ñ' or 'p' or 'q' or 'r' or 's' or 't' or 'v' or 'x' or 'w' or 'y' or 'z':
    print('La letra que ingreso es consonante')
else :
    print('ingreso mas de una letra')

#4
edad = int(input('ingrese su edad:'))
if edad > 18 :
    print('eres lo suficiente mayor para conducir')
elif edad < 0 :
    print('numero ingresado incorrecto')
elif edad < 18 :
    edadConducir = 18 - edad 
    print(f'te falta años {edadConducir}'' para conducir')