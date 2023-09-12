#Crear una calculadora con funciones 
import math

print('1: Suma, 2: Resta, 3: Multiplicacion, 4: Division, 5: Salida de calculadora')
signo = int(input("Escriba el numero del signo: "))
salir = False

import Calculos as cal
while salir == False:
    if signo == 1:
        x = float(input('Escriba el numero 1: '))
        y = float(input('Escriba el numero 2: '))
        print('la suma es: ',cal.sumar(x,y))
    elif signo == 2:
        x = float(input('Escriba el numero 1: '))
        y = float(input('Escriba el numero 2: '))
        print('la resta es: ',cal.restar(x,y))
    elif signo == 3:
        x = float(input('Escriba el numero 1: '))
        y = float(input('Escriba el numero 2: '))
        print('la multiplicacion es: ',cal.multiplicar(x,y))
    elif signo == 4:
        x = float(input('Escriba el numero 1: '))
        y = float(input('Escriba el numero 2: '))
        print('la division es: ',cal.dividir(x,y))
    elif signo == 5:
        print('Gracias por usar la calculadora')
        break
    salir = True
else:
    print('Seleccione bien la lista')