#Escribir un programa que, dada una lista de números, imprima la suma de los números pares.
inicio = int(input('ingrese numero inicial:'))
final = int(input('ingrese numero final:'))

suma = 0
print('los numero pares del rango son')
while inicio <= final:
    if inicio % 2 == 0:
        print(inicio)
        suma = suma+inicio
    inicio+=1
print('la suma de los numeros pares es',suma)

#Escribir un programa que, dado un número, imprima la siguiente secuencia:
i = 1
print(i)
print(i,i)
print(i,i,i)
#Escribir un programa que, dada una lista de números, imprima la lista de números sin duplicados.
data = [5,5,3,2,4,7,3,2,2,1,4]
result = []
for item in data:
    if item not in result:
        result.append(item)
        
result
#Escribir un programa que, dado un número, imprima todos los números primos menores que ese número.
comprobar = True
while comprobar:
    n= int(input('ingrese un numero entero positivo'))
    if n > 0 :
        comprobar == False
        i = 2
        while i < n:
            creciente = 2
            esprimo = True
            while esprimo and creciente < i :
                if i & creciente == 0 :
                    esprimo = False
                else:
                    creciente += 1
            if esprimo:
                print(i,'es primo')
            i += 1
            
else:
    print('el numero ingresado no es correcto. intente nuevamente')

#Escribir un programa que, dado un conjunto de números, imprima el número más grande y el número más pequeño.
lista=[2,5,12,54,1,10]


mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]

menor=lista[0]
posicion=0
for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x
print(menor)
print(mayor)

