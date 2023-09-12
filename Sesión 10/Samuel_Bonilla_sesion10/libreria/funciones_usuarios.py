import datetime

#lista que contendra info de los libros
libro = []
def agregar_libros(titulo, autor, fecha):
    libro.append({'Titulo': titulo, 'Autor': autor,'Fecha': fecha})

def Mostrar_Libro():
    for it in libro:
        print(
            f"Titulo: {it['Titulo']}, Autor: {it['Autor']}, Fecha_de_publicacion: {it['Fecha']}")
        
def buscar_libros(TituloLibro):
    encontrado = False
    for it in libro:
        if TituloLibro.lower() in it['Titulo'].lower():
            print(
            f"Titulo: {it['Titulo']}, Autor: {it['Autor']}, Fecha_de_publicacion: {it['Fecha']}")
            encontrado = True
            break
    if not encontrado:
        print("No existe el libro")