# Escribe un programa que dado una lista de numeros imprima
# la suma de dos numero pares

ni = int(input('Ingrese numero incial: '))
nf = int(input('Ingrese numero final: '))

sumar = 0

for i in range(ni, nf + 1):
    if i % 2==0:
        sumar += i

print(f'La suma es: {sumar}')

