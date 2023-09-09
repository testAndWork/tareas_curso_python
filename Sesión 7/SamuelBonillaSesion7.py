thislist = ["apple", "banana", "cherry"]
print(thislist)

vegetalesLst = ["Tomate", "Papa", "Coliflor", "Zanahoria", "Cebolla"]
print(len(vegetalesLst))

paises = [
    'El Salvador', 'Guatemala', 'Costa Rica', 
    'Panama', 'Honduras', 'Nicaragua'
]
print(len(paises))
print(paises)

listas = [3,4,5,6,7,8,3,3,3]
print(listas)
print(len(listas))

#Ejemplo appened
thislist = ["apple", "banana", "cherry"]
thislist.append("jocote")
print(thislist)

emptylist = []
print(emptylist)
emptylist.append('Vacio1')
print(emptylist)
emptylist.append('Ya esta vacio')
print(emptylist)

#Ejemplo 
list4 = ["abe", 34, True, 10, "male"]
list4
print(type(list4[0]))
print(type(list4[1]))
print(type(list4[2]))
print(type(list4[3]))

lst5 = [
    'Juan', 350, True, {'pais': 'El Salvador', 'Ciudad': 'San Salvador'},
    [1,2,3,4]
]

print(lst5)

#Indice positivo

print(len(lst5))
print(lst5[4])
print(type(lst5[4]))
print(lst5[3])
print(type(lst5[3]))

lst5.append(23)
lst5.append("Hola mundo")
lst5.append(False)

print(lst5)

#Con Indice negativo

frutas = ['papaya', 'jocote', 'piña', 'melon', 'sandia']

print(frutas[-1])
print(frutas[-2])
print(frutas[-3])
print(frutas[-4])
print(frutas[-5])

#Ejemplo
frutas = ['papaya', 'jocote', 'piña', 'melon', 'sandia']
fruta1, fruta2, *sobran = frutas

print(fruta1)
print(fruta2)
print(sobran)

#Ejemplo
numTest = [1,2,3,4,5,6,7,8,9,10,11,12,13]

n1,n2, *nVarios, nPenultimo, nUltimo  = numTest
print(n1)
print(n2)
print(nVarios)
print(nPenultimo)
print(nUltimo)

#Ejemplo
numTest2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
nInicio, *ncentrales, nUltimo = numTest2
print(nInicio)

ncentral = []
for num in ncentrales:
    ncentral.append(int(num))
print(ncentral)
print(2*ncentrales)
print(nUltimo)

#Slicing

frutas = ['papaya', 'jocote', 'piña', 'melon', 'sandia']
print(len(frutas))

todoFruta = frutas[0:5]
print(todoFruta)

pruebaFrutas = frutas[0:]
print(pruebaFrutas)

slice1 = frutas[1:3]
print(slice1)

slice2 = frutas[2:4]
print(slice2)

slice3 = frutas[1:4]
print(slice3)

print(frutas[1:])
print(frutas[::2])

#Ejemplo

frutas = ['papaya', 'jocote', 'piña', 'melon', 'sandia']

frutas[-4]
frutas[-3:-1]
frutas[-3]
frutas[::-1]

#Ejemplo de agregar elementos en cualquier posicion
frutas = ['papaya', 'jocote', 'guineo', 'piña', 'melon', 'sandia']

frutas[2] = 'fresas'

print(frutas)

#Buscar 
frutas = ["manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa",
          "papaya", "piña", "cereza", "limón", "granada", "frambuesa", "mandarina", "durazno", "coco", "ciruela"]

'melon' in frutas

'papaya' in frutas

for fruta in frutas:
    if fruta == 'papaya':
        print('si hay')
    else:
        print('no hay')
        
#Insertar elementos

frutas = ["manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa",
          "papaya", "piña", "cereza", "limón", "granada", "frambuesa", "mandarina", "durazno", "coco", "ciruela"]

frutas.insert(3, 'jocote')

'jocote' in frutas

print(frutas)

frutas.insert(6, 'guineo')

print(frutas)
#Ejemplo de remover elementos en una lista

print(frutas)
frutas.remove('guineo')
print(frutas)

#Ejemplo de eliminar elementos con el metodo pop()

print(frutas)
frutas.pop(20)

#Ejemplo de eliminar elementos con el metodo del()
print(frutas)
del frutas[0]

print(frutas)

del frutas[4:9]
print(frutas)

del frutas
print(frutas)

#Clear() limpiar elementos

paisescentroamericanos = ["Belice", "Costa Rica", "El Salvador", "Honduras",
                          "Nicaragua", "Panama"]
print(paisescentroamericanos)
paisescentroamericanos.clear()

#Copiar una lista

paisesNorteamerica = ["Estados Unidos", "Canada", "Mexico"]

NewPaises = paisesNorteamerica.copy()
print(NewPaises)

#Unir lista

paisescentroamericanos = ["Belice", "Costa Rica", "El Salvador", "Honduras",
                          "Nicaragua", "Panama"]
paisesNorteamerica = ["Estados Unidos", "Canada", "Mexico"]

casiAmerica = paisescentroamericanos + paisesNorteamerica

print(casiAmerica)

#ordenar
frutas2 = ['papaya', 'jocote', 'piña', 'melon', 'sandia']
fruta2.sort()
print(fruta2)

frutas2 = ['papaya', 'jocote', 'piña', 'melon', 'sandia']
print(sorted(frutas2))

edades = [22, 19, 24, 25, 26, 24, 25, 24]
print(sorted(edades, reverse=True))

#tupla

thistupla = ("apple", "banana", "cherry")
print(len(thistupla))

#crear tupla

frutatupla = ["manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa",
          "papaya"]

print(frutatupla)

print(frutatupla[0])
print(frutatupla[6])
print(frutatupla[9])

print(frutatupla[-1])
print(frutatupla[-6])
print(frutatupla[-9])

#Slicing en las tuplas

frutatupla = ["manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa",
          "papaya"]

tpl1 = frutatupla[0:4]
print(tpl1)

tpl2 = frutatupla[2:8]
print(tpl2)

tpl3 = frutatupla[-3:]
print(tpl3)

#Cambiando tuplas a listas

lst2tpl = list(tpl3)

print(type(lst2tpl))

print(lst2tpl)

lst2tpl.append('coco')
tpl3 = tuple(lst2tpl)
print(tpl3)

#Busqueda

'fresa' in tpl3

#Unir tuplas

jointpl = tpl1+tpl3
print(jointpl)

#Borrar tuplas

del jointpl

print(jointpl)

#Conjunto set()

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

set1 = {"apple", "banana", "cherry", "apple"}

print(set1)

for fruit in set1:
    print(fruit)
    
#Agregar elementos

set1.add('piña')
print(set1)

set2.update("naranja", "melocoton", "jocote")
print(set1)

#Eliminar elementos en un set

set1.pop()

set1.clear()

del set1

#Diccionario

myfamily = {
    "childl" : {
    "name" : "Emil",
    "year": 2004
    },
    "child2" : {
    "name" : "Tobias",
    "year" : 2007
    },
    "child3" : {
    "name" : "Linus",
    "year" : 2011
    }
}

print(myfamily)

