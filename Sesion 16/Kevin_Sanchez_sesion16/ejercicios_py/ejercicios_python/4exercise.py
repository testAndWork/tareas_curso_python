# Escribir un programa que, dado un número, 
# imprima todos los números primos menores que ese número

num = int(input('Ingrese un numero: '))

if num > 0:
    for i in range(2, num):
        count = 2
        esPrimo = True
        while esPrimo and count < i:
            if i % count == 0:
                esPrimo = False
            else:
                count += 1
        if esPrimo:
            print(f' {i} es Primo')
else:
    print('El numero ingresado no es correcto, intentelo nuevamente.')


