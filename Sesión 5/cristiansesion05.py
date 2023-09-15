#verificar el numero par

Numero = int(input('Inserte el numero a verificar: '))

if Numero  % 2 == 0:
    print(f'El numero es par {Numero}')
else :
    print (f'El numero es impar {Numero}')

#verificar contraseña 
Contraseña = input('Ingrese la contraseña: ')

if Contraseña == '1234':
    print('La contraseña es correcta')
else:
    print('La contraseña es incorrecta')




