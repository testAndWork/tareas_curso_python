#archivo principal del proyecto
"""Este sistema sera desarrollado para automatizar los procesos de una 
biblioteca; contiene la funciones basicas para llevar un control del usuario """

import libreriaB.funciones_biblioteca as fb

print('BIENVENIDOS AL SISTEMA BIBLIOTECAS')

while True:
    print('DIgite la opcion a utlizar:\n 1-agregar libros:\n 2- mostrar libros: \n 3-buscar libros:\n 4-Eliminar libro: \n0-salir del sistema:')
    opcion = int(input('Ingrese la opcion:'))

    if opcion == 0:
        print('\nGracias por usar el sistema!!!')
        break
    elif opcion ==1 :
        titulo = input('ingrese el titulo del libro:')
        autor =  input('ingrese el autor del libro:')
        fecha = input('ingrese la fecha del libro AAAA-MM-DD:')
        fb.agregar_libros(titulo, autor,fecha)
    elif opcion == 2 :
        print('el libro a mostras:\n')
        fb.mostrar_libro()
    elif opcion ==3:
        buqueda = input('digite el nombre de titulo:\n')
        fb.buscar_libros(buqueda)
    elif opcion==4:
        libroT = input('Digite el titulo de libro a eliminar')
        fb.eliminar_libro(libroT)
        print('libro eliminado con exito\n')
        fb.mostrar_libro()
    else :
        print('opcion invalidad')