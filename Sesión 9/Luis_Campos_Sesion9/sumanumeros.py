import libraryE.suma as sl

print('BIENVENIDOS AL SUMADOR DE NUMEROS')

while True:
    print('DIgite la opcion a utlizar:\n 1-agregar numeros:\n 2- mostrar numeros:\n0-salir del sistema:')
    opcion = int(input('Ingrese la opcion:'))

    if opcion == 0:
        print('\nGracias por usar el sistema!!!')
        break
    elif opcion ==1 :
        numero = int(input('ingrese el numero:'))
        sl.agregar_num(numero)
    elif opcion == 2 :
        print('el total de la lista sumada es:\n')
        sl.sum_num()
    else:
        print('opcion invalida')