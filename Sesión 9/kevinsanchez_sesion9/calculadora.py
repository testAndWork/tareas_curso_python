import librarys.my_modulo as mm

salir = True
while True:
    print('*****************************************')
    print('********* MENU *********')
    print('*****************************************')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('Digite la opcion: ')
    
    if op ==  1:
        num1 = float(input('Digite primer numero: '))
        num2 = float(input('Digite primer numero: '))
        print('El resultado de la suma es: ', mm.sumarN(num1,num2))
    elif op == 2:
        num1 = float(input('Digite primer numero: '))
        num2 = float(input('Digite primer numero: '))
        print('El resultado de la resta es: ',  mm.restarN(num1,num2))
    elif op == 3:
        num1 = float(input('Digite primer numero: '))
        num2 = float(input('Digite primer numero: '))
        print('El resaultado de la multiplicacion es: ', mm.multiplicarN(num1,num2))
    elif op == 4:
        num1 = float(input('Digite primer numero: '))
        num2 = float(input('Digite primer numero: '))
        print('el resultado de la division es: ', mm.dividirN(num1,num2))
    elif op == 0:
        print('Gracias por usar la calculadora')
        break





