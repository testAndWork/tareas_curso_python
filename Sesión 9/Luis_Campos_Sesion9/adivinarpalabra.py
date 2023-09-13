import random
palabras = ['python','programar','lista']
palabra = random.choice(palabras)
letras_adivinadas = []

while True:
    letra = input('Ingrese letra:')
    letras_adivinadas.append(letra)
    palabra_oculta = ""
    for it in palabra:
        if it in letras_adivinadas:
            palabra_oculta += it
        else:
            palabra_oculta += "_"
    print(palabra_oculta)
    if "_" not in palabra_oculta:
        print("adivinaste la palabra!!!")
        break