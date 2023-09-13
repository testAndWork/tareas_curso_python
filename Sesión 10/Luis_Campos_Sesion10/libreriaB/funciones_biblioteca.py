#modulo de funciones de biblioteca
"""
las funciones a desarrollar son:
funcion agregar libro:
mostrar libro:
buscar libro:
"""
import datetime

#lista que contendra la informacion de los libros

libro = []
def agregar_libros(titulo, autor, fecha):
    libro.append({'Titulo':titulo,'Autor':autor,'Fecha':fecha})
def mostrar_libro():
    for it in libro:
        print(f"Titulo:{it['Titulo']},Autor:{it['Autor']}, fecha publicacion{it['Fecha']}")
def buscar_libros(tituloLibro):
    encontrado = False
    for it in libro:
        if tituloLibro.lower() in it ['Titulo'].lower():
            print(f"Titulo:{it['Titulo']},Autor:{it['Autor']}, fecha publicacion{it['Fecha']}")
            encontrado = True
            break
    if not encontrado:
        print('no exite el libro')
def eliminar_libro(tituloLibro):
    eliminar = False
    for it in libro:
        if tituloLibro.lower() in it ['Titulo'].lower():
            print(f"Titulo:{it['Titulo']},Autor:{it['Autor']}, fecha publicacion{it['Fecha']}")
            libro.remove(it)
            eliminar = True
            break
    if not eliminar:
        print('no exite el libro')
