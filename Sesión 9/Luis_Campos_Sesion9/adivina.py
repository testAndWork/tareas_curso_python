import random
intentos = 0


numero = random.randint(1,20)
print('adivina el numero del 1 al 20')
while intentos < 20:
    adivina = int(input())
    if adivina < numero:
        print('¡El numero ingresado es menor!')
    if adivina > numero:
        print('¡El numero ingresado es mayo!')
    if adivina == numero:
        break
if adivina == numero:
    print('Felicidades acertastes el numero')
    