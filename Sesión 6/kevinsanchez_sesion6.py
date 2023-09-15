#Ejercicio_1

#if 10:
#    print('numero es igual a 10')
"""
Correccion: faltaba dos puntos
"""

#Ejercicio_2

#numero = 5
#if numero < 10:
#    print('numero es menor que 10')

"""
Correccion: faltaba dos puntos y inicializar la variable, tambien el then se borro.
"""

#Ejercicio_3
#numero = 8
#if numero > 5:
#    print('Numero es mayor que 5')
"""
Correccion: no tiene ningun problema.
"""


#Ejercicio_4
"""numero = 3
if numero % 2 == 0:
    print('Numero es par')
else:
    print('El numero es impar')"""
"""
Correccion: faltaba el else con el mensaje de que el numero es impar.
"""

#Ejercicio_5
"""numero = 3
if numero % 2 == 0:
    print('Numero es par')
else:
    print('El numero es impar')"""
"""
Correccion: faltaba el else con el mensaje de que el numero es impar.
"""

#Ejercicio_6
"""valor = 'Pyhton'
if valor != "pyhton":
    print('El valor es Pyhton')"""
"""
Correccion: 
"""

#Ejercicio_7
"""edad = 18
if edad == "18":
    print('Tienes 18 años')"""
"""
Correccion: la edad se esta igualando a un string y 
"""
#####################################################################

#Ciclo While

"""flag = 0
while flag < 5:
    print(flag)
    flag = flag + 1

flag = 0
while flag < 5:
    print(flag)
    flag += 1
"""
#####################################################################
"""flag = 0

while flag < 5:
    print(flag)
    flag += 1
else:
    print(f'El valor de flag es: {flag}')
"""
#####################################################################
"""
Implemente la solucion la cual adivine un numero previamente definido por un usuario
y que otro usuario digite otro valor tratando de adivinar el definido

Mensaje de inicio: Digita el numero para adivinar.
si no adivina el mensaje es: intentea de nuevo
si adivino: felicidades adivinaste
"""

"""num = 7
valor = int(input('Digita el numero para adivinar: '))

while valor != num:
    valor = int(input('intentea de nuevo: '))
else:
    print('!!Felicidades Adivinaste')"""
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""i = 6
suma = 0
n = 6

while i < n:
    suma += i
    i += 1

print(f'La suma de los numeros es: {suma}')"""

#####################################################################

#Factorial de un numero
"""n = 4
factorial = 1
contador = 1

while contador <= n:
    factorial *= contador
    contador += 1

print(f'El factorial de un numero es: {n} es {factorial}')"""
#####################################################################

#BREAK AND CONTINUE

"""flag = 0

while flag < 100:
    print(flag)
    flag += 1
    if flag == 34:
        print('valor de break', flag)
        break"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""flag = 0

while flag < 10:
    print(flag)
    if flag == 5:
        continue
    print('valor desues del continue', flag)
    flag += 1
#####################################################################

i = 1

while i < 6:
    print(i)
else:
    print('Esta es otra opcion')"""
#####################################################################

#ciclo For

"""frutas = ['mango','Jocote','piña','guineo','papaya','fresa','pera']

for x in frutas:
    print(x)"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""cadena = 'hola como estan'

for i in cadena:
    print(i)"""
#####################################################################
"""tupla = (0,1,2,3,4,5)

for elementos in tupla:
    print(elementos)

tupla = ('a','b','c')
for elementos in tupla:
    print(elementos)"""
#####################################################################

informacionPersonal = {
    'Nombre':'Ash',
    'Apellido':'Ketchum',
    'edad':'10',
    'Municipio':'Ciudad Paleta',
}

"""for info in informacionPersonal:
    print(info)

for info,valor in informacionPersonal.items():
    print(info,valor)"""
#####################################################################

#frutas = ['mango','Jocote','piña','guineo','papaya','fresa','pera']

"""for it in frutas:
    print(it)
    if it == 'piña':
        break
#####################################################################

tuplaLetras = ('a','b','c')

for letras in tuplaLetras:
    print(letras)
    if letras == 'b':
        break

tuplaNumeros = (1,2,3,4,5,6,7)

for num in tuplaNumeros:
    print(num)
    if num == 5:
        break"""
#####################################################################

"""frutas = ['mango','Jocote','piña','guineo','papaya','fresa','pera']

for it in frutas:
    if it == 'piña':
        continue
    print(it)"""
#####################################################################

"""for it in range(6):
    print(it)

for it in range(2,6):
    print(it)

for it in range(4,30,4):
    print(it)


for it in range(30,2,-4):
    print(it)

lista = list(range(0,10,2))
print(lista)

lista1 = list(range(10))
print(lista1)

lista2 = list(range(0,100,12))
print(lista2)

#####################################################################
for x in range(6):
    print(x)
else:
    print('finalizado el ciclo for')

#####################################################################

frutas = ['mango','Jocote','piña','guineo','papaya']
estado = ['verde','maduro','podrido','picado']

for it in frutas:
    for jt in estado:
        print(f'este {it} esta muy {jt}')
"""
#####################################################################
#for x in [0,1,2]:
#    pass

"""numero = 4

for it in range(1,10):
    result = numero * it
    print(f'{numero} x {it} = {result}')"""
#####################################################################

#contador de vocales, dada una frase o vocales

frase = 'tres tristes tigres comen trIgO en un trigal'
vocales = 'aeiou'
contador = 0

for letra in frase:
    if letra.lower() in vocales:
        contador += 1
print('Numeros de vocales',contador)










