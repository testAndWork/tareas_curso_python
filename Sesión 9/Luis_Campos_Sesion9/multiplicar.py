import libraryE.tabla_multi as tm


while True:
    nun = int(input('ingresar el numero de la tabla de multiplicar'))
    print(('1- multiplicar \n5- Para salir'))
    opcion = int(input('elige una opcion:'))
    
    if opcion == 1:
        print('')
        print('Resultado es:', tm.multiplicar(nun))
    elif opcion == 5:
        break
    else:
        print('opcion incorrecta') 