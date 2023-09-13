import libraryE.calculadora as cal


nun1 = float(input('ingrese primer numero:'))
nun2 = float(input('ingrese segundo numero'))
while True:
    print(('1- Suma \n2- Resta \n3- Miltiplicacion \n4- Divicion \n5- Para salir'))
    opcion = int(input('elige una opcion:'))
    if opcion == 1:
        print('')
        print('Resultado de la suma es:', cal.sumar(nun1,nun2))
    elif opcion == 2:
        print('')
        print('Resultado de la suma es:', cal.restar(nun1,nun2))
    elif opcion ==3:
        print('')
        print('Resultado de la multiplicacion es:', cal.multiplicacion(nun1,nun2))
    elif opcion ==4:
        print('')
        print('Resultado de la division es:', cal.division(nun1,nun2))
    elif opcion == 5:
        break
    else:
        print('opcion incorrecta') 










   
   
