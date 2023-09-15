"""
Funciones a desarrolar son las siguientes

Funcion agregar libro
Funcion mostrar libro
Funcion buscar libro
"""

import datetime

#lista que contendra la informacion de los libros
libro = []

def agregarLibros(titulo,autor,fecha):
    libro.append({'Titulo' : titulo, 'Autor' : autor,'Fecha' : fecha})


def mostar_libro():
    for it in libro:
        print(f'Titulo : {it["Titulo"]}, Autor : {it["Autor"]}, Fecha de Publicacion : {it["Fecha"]}')

def buscar_libro(tituloLibro):
    encontrado = False
    for it in libro:
        if tituloLibro.lower() in it['Titulo'].lower():
            print(f'Titulo : {it["Titulo"]}, Autor : {it["Autor"]}, Fecha de Publicacion : {it["Fecha"]}')
            encontrado = True
            break
    if not encontrado:
        print('Libro no encontrado')


def eliminar_libro(tituloLibro):
    encontrado = False
    for it in libro:
        if tituloLibro.lower() in it['Titulo'].lower():
            print(f"Eliminando libro:")
            print(f'Titulo : {it["Titulo"]}, Autor : {it["Autor"]}, Fecha de Publicacion : {it["Fecha"]}')
            libro.remove(it)
            encontrado = True
            break
    if not encontrado:
        print('Libro no encontrado')






"""
buscar_libro(tituloLibro)
    libro.remove(tituloLibro)
    print('Libro eliminado con exito')
**************************************************************
    if buscar_libro(tituloLibro):
        libro.remove(tituloLibro)
        print('Eliminacione exitosa!')
**************************************************************
def Eliminar_Libro(tituloLibro):
    encontrado = False
    for it in libro:
        if tituloLibro.lower() in it['Titulo'].lower():
            print(f"Eliminando libro:")
            print(
                f"Titulo: {it['Titulo']}, Autor: {it['Autor']}, fecha_de_publicacion: {it['Fecha']}")
            libro.remove(it)
            encontrado = True
            break
    if not encontrado:
        print('Libro no encontrado')


"""

