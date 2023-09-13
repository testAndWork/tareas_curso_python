#1
if 10:
    print("Número es igual a 10")
#2
numero = 8
if numero < 10 :
    print('numero es menor que 10')
#3
numero = 8
if numero > 5 :
    print('numero es mayor a 5')
#4
numero = 3
if numero % 2 == 0 :
    print('numero es par')
else :
    print('numero es impar')
#5
valor = 'python'
if valor == 'python':
    print('el valor es python')
else:
    print('el valor no es python')
          

#6
edad = 18
if edad == 18:
    print('tienes 18 años')
else:
    print('tienes otra cosa')

#7
valor = 'Hola'
if valor.startswith("H"):
    print(valor)
#8
nota = 75
if nota >= 90:
    print('A') 
elif nota >= 80:
    print('B')
elif nota >= 70:
    print('C')
else:
    print('D')

#9
numero = 10 
if numero == 10:
    print('numero es igual a 10')


flag = 0 
while flag < 5 :
    print(flag)
    flag = flag + 1

flag = 0 
while flag < 5 :
    print(flag)
    flag += 1
flag = 0 
while flag < 5 :
    print(flag)
    flag += 1
else:
    print(f'el valor de flag es:{flag}')
#ejercicio
numero = int(input('digite el numero para adivinar'))
flag = 8
while numero != flag:
    numero = int(input('intente de nuevo'))
else:
    print('felicidades ADIVINASTE')
flag = 4
estado = False
while not estado:
    numero = int(input('Digite el numero adividar'))
    if numero== flag:
        print('vuelva a intentarlo')
        estado = True
else:
     print('adivinaste el numero')

i = 1 
suma = 0 
n = 1000
while  i <= n :
    suma += i
    i += 1
print(f'la suma de los numeros es :{suma}')

n = 4 
factorial = 1 
contador = 1
while contador <= n:
    factorial*= contador
    contador+=1
print(f'el factorial del numero {n} es:{factorial}')


flag = 0 
while flag < 100 :
    print(flag)
    flag += 1
    if flag==34:
        print('valor break',flag)
        break


i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('esta es otraopcion')

frutas = ['mango','jocote','piña','guineo']
for x in frutas:
    print(x)
frutas = ['mango','jocote','piña','guineo']
for i in frutas:
    print(i)

cadena = 'hola como esta'
for i in cadena:
    print(i)

tupla = (0,1,2,3,4)
for elementos in tupla:
    print(elementos)

tupla = ('a','b','c')
for elementos in tupla:
    print(elementos)

informacionPersonal = {
          'nombre':'ash',
          'apellido':'ketchum',
          'edad':'10',
          'municipio':'kanto',
            }
for info in informacionPersonal:
    print(info)
for info, valor in informacionPersonal.items():
    print(info, valor)
frutas = ['mango','jocote','piña','guineo']
for it in frutas:
    print(it)
    if it == 'jocote':
        break
tupla = ('a','b','c')
for letra in tupla:
    print(letra)
    if letra== 'b':
        break
frutas = ['mango','jocote','piña','guineo']
for it in frutas:
    if it == 'jocote':
        continue
    print(it)
for it in range(2,6):
    print(it)
for it in range(4,30,4):
    print(it)
for it in range(30,2,-4):
    print(it)
list = list(range(0,10,2))
print(list)

for it in range(6):
    print(it)
else :
    print('finalizo ciclo')

frutas = ['mango','jocote','piña','guineo','papaya']
estado = ['verda','maduro','podrido','picado']

for it in frutas:
    for jt in estado:
        print(f'este {it} esta muy {jt}')
#tabla de multiplicar 
numero = 1
for it in range (1,11):
    resultado = numero * it
    print( f'{numero} x {it} = {resultado}')

# contador de vocales 
frase = 'tres tristes tigres comen trigo en un trigal'
contador = 0 
for letra in frase:
    if letra in 'aeiouáéíóú':
        contador +=1
print('numero de vocales:', contador)

frase = 'tres tristes tigres cOmen trigo en un trigal'
contador = 0 
vocales = 'aeiouáéíóú'
for letra in frase:
    if letra.lower() in vocales:
        contador +=1
print('numero de vocales:', contador)