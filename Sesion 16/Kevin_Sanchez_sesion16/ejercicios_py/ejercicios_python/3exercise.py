#Escribir un programa que, dada una lista de números, 
# imprima la lista de números sin duplicados.

data = [1,2,3,2,4,5,6,7,3,2,2,1,4,3,6,5]
listnum = []

for i in data:
    if i not in listnum:
        listnum.append(i)

print(listnum)

