#1

if 10:
    print('Numero es igual a 10')
#Cambio de 2 puntos 

#2
numero = 8
if numero < 10: 
    print('Numero es menor que 10')
#Declarar numero y borrar then 

#3
if numero > 5:
    print("Número es mayor que 5")

# 4
if numero % 2 == 0:
 print("Número es par")
else:
    print('numero es impar')
#agregar else

# 7
edad = 18
if edad == 18:
 print("Tienes 18 años")
#borrar comillas 

#Ejemplo while => Hacer mientras

n = 4
Numero = int(input('Ingresa numero a adivinar: '))
while Numero != n:
      Numero = int(input('Intenta de nuevo: '))
else: 
   print('Felicidades adivinastes')
   
i = 1
suma = 0
N = 1000

while i<=N:
   suma += i
   i += 1

   print(f'La suma es: {suma}')

#4
c = 5 
factorial = 1
contador = 1 

while contador <= c:
   factorial *= contador
   contador += 1
print(f'EL factorial del numero {c} es {factorial} ')

#5
i = 1 
while i < 6:
    print (i)
    i += 1
else:
    print('es otra opcion')

#For

frutas = ['mango', 'jocote', 'piña', 'guineo', 'papaya']

for x in frutas: 
    print (x) 


informacionPersonal = {
   'nombre':'Cristian',
   'apellido':'Velasco',
   'edad':'10',
   'Municipio':'Nejapa'
}
for info in informacionPersonal:
   print(info)

for info, valor in informacionPersonal.items():
   print(info, valor)


    








