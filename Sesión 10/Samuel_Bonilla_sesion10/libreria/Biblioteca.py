#Archivo principal del proyecto
import funciones_bibliotecas as fb

print("Bienvenido al Sistema de Biblioteca")

while True:
    print("Digite la opcion a utilizar:\n 1- Agregar libros a la Biblioteca\n 2- Mostrar libros en la Biblioteca\n 3- Buscar titulos de libros en la biblioteca\n 4- Eliminara libro de la Biblioteca\n 0- Salir del sistema")
    
    opcion = int(input("Ingrese el numero de la opcion"))
    
    if opcion == 0:
        print("Gracias por usar el sistema!!!\n\n")
        break
    elif opcion == 1:
        titulo = input('Ingrese el titulo del libro: ')
        autor = input('Ingrese el nombre del autor: ')
        fecha = input('Ingrese la fecha de publicacion AAAA-MM-DD: ')
        fb.agregar_libros(titulo, autor, fecha)
    
    elif opcion == 2:
        fb.Mostrar_Libro()
        print("El libro a mostrar es:\n\n")
        
    elif opcion == 3:
        busqueda = input("digite el nombre del Titulo a buscar: ")
        fb.buscar_libros(busqueda)
        print("El titulo a buscar es:\n\n")
        
    elif opcion == 4:
        libroT = input('digite en nombre del Titulo a eliminar1: \n')
        fb.eliminar_Libro(libroT)
        print('libro eliminado con exito\n')
        fb.mostrar_Libro()
        
    else:
        print("Opción Invalida")