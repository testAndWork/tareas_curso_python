# 1
if 10:
 print("Número es igual a 10")

#Correccion: Falta dos puntos

# 2
numero = 5

if numero < 10:
 print("Número es menor que 10")

#Correccion: hay que definir la variable numero para que funcione y then no tiene
#funcion en ella 

# 3
numero = 8
if numero > 5:
    print("Número es mayor que 5")

#Correccion: hay poner sangria el print, porque sin sangria no funcionara

# 4
numero = 3
if numero % 2 == 0:
 print("Número es par")
else:
    print("Numero impar")

#Correccion: hay que poner un else

# 5
numero = 3
if numero % 2 == 0:
 print("Número es par")
else:
    print("Numero impar")

#Correccion: hay que poner un else

# 6
valor = "Python"
if valor == "python":
 print("El valor es Python")
else:
    print("El valor no es Python")

#Correccion: hay que poner el igualy poner el else

# 7
edad = 18
if edad == 18:
    print("Tienes 18 años")
else:
    print("otra cosa")

#tiene que definir como int, no string

# 8
numero = 7
if numero >= 5:
 print("Número es mayor que 5")

#Correccion: hay que definir la variable numero

#9
valor = "Hola"
if valor.startswith("H"):
    print("Es hola")

#While -> hacer mientras cumpla las condiciones

flag= 0

while flag < 5:
    print(flag)
    flag = flag +1

flag= 0
while flag < 5:
    print(flag)
    flag += 1

flag= 0
while flag < 5:
    print(flag)
    flag += 1
else:
    print(f"El valor de flag es :{flag}")

#Ejemplo

flag = 4
numero = int(input('Digita el numero para adivinar: '))

while numero !=  flag:
    numero = int(input('Intenta de nuevo: '))
else:
    print('Felicidades adivinastes')

#Ejemplo version 2

flag = 4

estado = False

while not estado:
    numero = int(input("Digita el numero para adivinar: "))

    if numero == flag:
        print("Felicidades, Adivinaste")
        estado = True
    else:
        print("Intente de nuevo: ")

#Ejemplo suma de los primeros n numeros 
i = 1
suma = 0
n = 6

while suma <= n:
    suma += i
    i    +=1
print(f"La suma de los numeros es: {suma}")


#Calcular el factorial de un numero
#Numero al que necesito calcular el factorial

n = 4
factorial = 1
contador = 1

while contador <= n:
    factorial *= contador
    contador += 1

print(f"El factorial del numero {n} es {factorial} ")

#break

flag = 0

while flag < 100:
    print(flag)
    flag += 1
    if flag== 34:
        print("valor de break",flag)
        break

#Continue

flag = 10

while flag < 10:
    if flag < 10:
        continue
        print("valor de continue",flag)
    flag += 1

#Else de un ciclo repetitivo

i= 1

while i < 6:
    print(i)
    i += 1
else:
    print("Esta es otra opcion")

#Ciclo for

frutas = ['mango','jocote','piña','guineo','papaya']

for i in frutas:
    print(i)

#Bucle a traves de cadena

cadena = 'hola como estan'

for i in cadena:
    print(i)
    
#ciclo for por tuplas

tupla = (0,1,2,3,4)

for elementos in tupla:
    print(elementos)
    
#for sobre diccionarios

informacionpersonal = {
    'Nombre':'ash',
    'Apellido':'ketchum',
    'Edad':'10',
    'Municipio':'kanto'
}

for info in informacionpersonal:
    print(info)

for info, valor in informacionpersonal.items():
    print(info, valor)
    
#ruptura for

frutas = ['mango','jocote','piña','guineo','papaya']

for it in frutas:
    print(it)
    if it == 'jocote':
        break
    
tupla = ('a','b','c')

for letras in tupla:
    print(letras)
    if letras == 'b':
        break
    
tuplanumeros = (1,2,3,4,5,6,7)

for numeros in tuplanumeros:
    print(numeros)
    if numeros == 5:
        break
    
#continue - for 

frutas = ['mango','jocote','piña','guineo','papaya']

for it in frutas:
    if it == 'piña':
        continue
    print(it)
    
#fucion range

for it in range(6):
    print(it)

for it in range(2,6):
    print(it)

for it in range(4,30, 4):
    print(it)
    
for it in range(30,2, -4):
    print(it)
    
lista = list(range(0,10,2))
print(lista)

lista = list(range(10))
print(lista)

lista = list(range(0,100,12))
print(lista)

#Else ciclo for

for it in range(6):
    print(it)
else:
    print("finalizamos el ciclo for")
    
#Bucles anidados

frutas = ['mango','jocote','piña','guineo','papaya']

estado = ['verde', 'maduro', 'podrido', 'picado']

for it in frutas:
    for jt in estado:
        print(f'esta {it} esta muy {jt}')
        
#Declaracion pass

#tabla de multiplicar

numero = 1

for it in range(1,11):
    resultado = numero * it
    print(f'{numero}X{it} = {resultado}')
    
#Contador de vocales, dada una frase o cadena, contar las vocales que tiene

frases = 'tres tristes tigres comen trigo en un trigal'
contador = 0

for letra in frases:
    if letra in 'aeiouáéíóú':
        contador += 1
        
print("Numero de vocales:", contador)

#Ejemplo

frases = 'tres tristes tigres comen trigo en un trigal'
vocales = 'aeiouáéíóú'
contador = 0

for letra in frases:
    if letra.lower() in vocales:
        contador += 1
        
print("Numero de vocales:", contador)

