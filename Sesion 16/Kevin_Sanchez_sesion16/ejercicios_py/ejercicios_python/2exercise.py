# Escribir un programa que, dado un número,
# imprima la siguiente secuencia
# 1
# 1 1
# 1 1 1

n = int(input("ingresa un numero: ")) 

for i in range(1,n+1): 
    for j in range(1,i+1): 
        print(" 1 ",end="")
    print("")


