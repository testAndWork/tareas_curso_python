numeros = [12, 12, 3, 1, 10, 2, 2, 3, 3, 4, 5]

def numerosunicos(numeros):

    lista_de_numeros_unicos = []

    numeros_unicos = set(numeros)

    for numero in numeros_unicos:
        lista_de_numeros_unicos.append(numero)

    return lista_de_numeros_unicos


print(numerosunicos(numeros))