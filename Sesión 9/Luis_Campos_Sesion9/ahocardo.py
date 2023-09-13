import time
import random
palabras = ['python','programar','lista']
palabra = random.choice(palabras)
letras_adivinadas = []

nombre = input('como te llamas?\n')
print(f"hola {nombre} es hora de jugar")
print("")
time.sleep(1)
print('comienza el nombre')
time.sleep(0.5)
vidas = 8

while vidas>0:
    letra = input('Ingrese letra:')
    letras_adivinadas.append(letra)
    palabra_oculta = ""
    fallas = 0
    for it in palabra:
        if it in letras_adivinadas:
            palabra_oculta += it
        else:
            palabra_oculta += "_"
            fallas+=1
        
    print(palabra_oculta)
    if fallas ==0:
        print("adivinaste la palabra!!!")
        break
    if letra not in palabra:
        vidas -= 1
        print('equivocacion')
        print(f'tu tienes {vidas} vidas')
    if vidas == 0 :
        print('perdiste *_*')
else:
    print('gracias por participar')