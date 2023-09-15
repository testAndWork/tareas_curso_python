import random

print('****************************************')
print('ADIVINA EL NUMERO')
print('****************************************')

intentos = 0

numero = random.randint(1,10)

while intentos < 5:
    intentos += 1
    x = int(input("Elige un numero del 1 al 10: "))
    if numero > x:
        print('El numero es menor')
    if numero < x:
        print('El numero es mayor')

if numero == x:
    print ("Eres un genio....")
    print (" lo lograste con %d intentos" % (intentos))
    print ("Nos vemos....")

if numero != x:
    print ("Has perdido!!!!! :( ")


