lista_numeros = []

numero = int(input("Ingresa los valores: "))

#Debe ingresar los numeros, cuando al ingresar 0 la operacion se termina y dara el resultado de la suma
while numero!=0:
    lista_numeros.append(numero)
    numero = int(input("Ingresa los valores: "))
    
list_numeros = sum(lista_numeros)
print(list_numeros)