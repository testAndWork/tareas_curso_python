# Escribir un programa que, dado un conjunto de numeros, imprima el 
# numero mas grande y el numero mas pequeño

numeros = []

rango = int(input('Digite el rango: '))

for i in range(rango):
    num = int(input('Digite el numero: '))
    numeros.append(num)



def numMayor():
    mayor = numeros[0]
    for j in numeros:
        if j > mayor:
            mayor = j
    return mayor

def numMenor():
    menor = numeros[0]
    for j in numeros:
        if j < menor:
            menor = j
    return menor


print(f'El numero mayor es: {numMayor()}')

print(f'El numero menor es: {numMenor()}')

