"""
Imagina que estás creando un sistema para administrar una biblioteca de libros. 
Quieres organizar tus funciones en módulos para mantener el código ordenado y modular. 
Utilizarás módulos incorporados como datetime para manejar fechas.

Crea un archivo llamado biblioteca.py que contendrá tu programa 
principal y un módulo personalizado llamado funciones_biblioteca.py que 
contendrá las funciones relacionadas con la administración de la biblioteca.
"""

#Archivo Principal
import librerias.funcionesBiblioteca as fb

print('Bienvenido al Sistema de Biblioteca')

while True:
    print('Seleccione la opcion a utilizar')
    print('1. Agregar Libros')
    print('2. Mostrar Libro')
    print('3. Buscar Libro')
    print('4. Eliminar Libro')
    print('0. Salir')
    
    op = int(input('Ingrese el numero de la opcion: '))
    
    if op == 0:
        print('Gracias por usar el sistema')
        break
    elif op == 1:
        titulo = input('Ingrese el titulo del libro: ')
        autor = input('Ingrese el nombre del autor: ')
        fecha = input('Ingrese la fecha de publicacion AAAA-MM-DD: ')
        fb.agregarLibros(titulo,autor,fecha)
    elif op == 2:
        print(fb.mostar_libro())
    elif op == 3:
        busqueda = input('Digite el nombre del titulo: ')
        print(fb.buscar_libro(busqueda))
    elif op == 4:
        libroT = input('Digite el titulo a eliminar: ')
        fb.eliminar_libro(libroT)
        
    else:
        print('Opcion Invalida')















