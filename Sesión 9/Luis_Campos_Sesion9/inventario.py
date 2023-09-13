#archivo principal del proyecto
"""Este sistema sera desarrollado para automatizar los procesos de una 
inventario; contiene la funciones basicas para llevar un control del usuario """

import libraryE.funciones_inventario as fi

print('BIENVENIDOS AL SISTEMA INVENTARIO')

while True:
    print('DIgite la opcion a utlizar:\n 1-agregar producto: \n 2-Eliminar productos: \n 3- actualizar productos \n0-salir del sistema:')
    opcion = int(input('Ingrese la opcion:'))

    if opcion == 0:
        print('\nGracias por usar el sistema!!!')
        break
    elif opcion ==1 :
        codigo = input('ingrese el codigo del producto:')
        producto =  input('ingrese el nombre del producto:')
        cantidad = input('ingrese la cantidad de producto')
        fecha = input('ingrese la fecha entrad de producto AAAA-MM-DD:')
        fi.agregar_inventario(codigo, producto, cantidad, fecha)
    elif opcion==2:
        codigoP = input('Digite el codigo del producto a eliminar')
        fi.eliminar_inventario(codigoP)
        print('libro eliminado con exito\n')
    elif opcion == 3 :
        fi.mostrar_inventario()
    else :
        print('opcion invalidad')
