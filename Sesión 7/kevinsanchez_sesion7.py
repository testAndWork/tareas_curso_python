#Colecciones

#Lista en pyhton
"""thislist = ['apple','cherry','banana']
print(len(thislist))

vegetalesLST = ['Tomate','Papa','Cliflor','zanahoria','cebolla']
print(len(vegetalesLST))

paises = ['El Salvador','Guatemala','Costa Rica','Panama','Honduras','Nicaragua']
print(len(paises))

listas = [3,4,5,6,7,8,3,4,3,3,3]
print(listas)
print(len(listas))"""
#############################################################################
#Agregar elementos a una lista

"""thislist = ['apple','cherry','banana']
print(thislist)
print(len(thislist))
thislist.append('Jocote')
thislist.append('Piña')
print(thislist)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
emptyList = []
print(emptyList)
emptyList.append('vacio1')
print(emptyList)
emptyList.append('vacio2')
print(emptyList)"""
#############################################################################
#Elementos - Tipos de datos

"""lista1 = ['apple','banana','cherry']
lista1 = [1,5,7,9,3]
lista1 = [True,False,False]
lista1 = [2.0,5.5,6.7,8.8]

listaA = ["abe",34,True,10,'male']

print(type(listaA[0]))
print(type(listaA[1]))
print(type(listaA[2]))
print(type(listaA[3]))

listaB = [
    'Juan', 350, True, { 'pais' : 'El Salvador', 'Ciudad' : 'San Salvador' }, [1,2,3,4]
]

len(listaB)
print(listaB[4])
print(type(listaB[4]))
print(listaB[3])
print(type(listaB[3]))

listaB.append(23)
listaB.append('Hola Mundo')
listaB.append(False)

lstNew = [listaB[0], listaB[1], listaB[2], listaB[3]]

print(lstNew)

indiceFinal = len(lstNew)-1
print(indiceFinal)
print(lstNew[3])

frutas = ['sandia','melon','papaya','jocote','piña']

print(frutas[-1])
print(frutas[-2])
print(frutas[-4])
print(frutas[-5])

fruta1,fruta2,*sobran = frutas

print(fruta1)
print(fruta2)
print(sobran)"""
#############################################################################

"""numTest = [1,2,3,4,5,6,7,8,9,10,11,12,13]

n1,n2,*nvarios,nPenultimo,nUltimo = numTest

print(n1)
print(n2)
print(nPenultimo)
print(nUltimo)
print(nvarios)

numTest2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]

nInicio,*nCentrales,nUltimo = numTest2

print(nInicio)

nCentral = []
for num in nCentrales:
    nCentral.append(int(num))
print(nCentral)

print(2*nCentrales)
print(nUltimo)"""
#############################################################################

#Slicing
"""frutas = ['sandia','melon','papaya','jocote','piña']

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

print(frutas[4])
print(frutas[1:])
print(frutas[::2])
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
frutas = ['sandia','melon','papaya','jocote','piña']

print(frutas[-4])
print(frutas[-3:-1])
print(frutas[-3])

print(frutas[::-1])"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Agregar elementos a las lista en cualquier posicion
"""frutas = ['sandia','melon','guineo','papaya','jocote','piña']

frutas[2] = 'fresas'
print(frutas[2])
print(frutas)"""

#Buscar elementos en una lista

"""frutas = [
    'sandia','melon','guineo','papaya','jocote','piña','manzana','uva','kiwi','limon','cerez',
    'granada'
    ]

print('melon' in frutas)
print('papaya' in frutas)
print('cereza' in frutas)

for fruta in frutas:
    if fruta == 'cereza':
        print('si hay')
    else:
        print('si hay')
"""

#Insertar elementos en una lista
"""frutas = [
    'sandia','melon','guineo','papaya','jocote','piña','manzana','uva','kiwi','limon','cerez',
    'granada'
    ]

frutas.insert(3,'pera')

print('papaya' in frutas)

frutas.insert(6,'pera')
print(frutas)"""

#Remove para eliminar un elemento en especifico de una lista
"""frutas = [
    'sandia','melon','guineo','papaya','jocote','piña','manzana','uva','kiwi','limon','cerez',
    'granada'
    ]

frutas.remove('guineo')
print(frutas)
print('guineo' in frutas)

#Remove para eliminar un elemento en un indice especifico en una lista utilizando el metodo pop()

frutas.pop(0)
frutas.pop(5)
print(frutas)

#Para eliminar un elemento en especifico, un grupo especifico o toda la lista en una lista 
#utilizamos el metodo del()
frutas = [
    'sandia','melon','guineo','papaya','jocote','piña','manzana','uva','kiwi','limon','cerez',
    'granada'
    ]

del frutas[0]
print(frutas)

del frutas[4:9]
print(frutas)

del frutas
print(frutas)"""
#############################################################################

#Limpiar items de listas 
#el metodo clear limpia elementos de una lista

"""paisesCentroAmerica = ['Costa Rica', 'Panama','Guatemala', 'Honduras', 'Nicaragua', 'Belice', 'El Salvador']

paisesCentroAmerica.clear()

print(paisesCentroAmerica)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Copiar Lista
paisesNorteAmerica = ['Mexio','Canada','Estados Unidod']
newPaises = paisesNorteAmerica.copy()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Unir Listas
paisesCentroAmerica = ['Costa Rica', 'Panama','Guatemala', 'Honduras', 'Nicaragua', 'Belice', 'El Salvador']
paisesNorteAmerica = ['Mexio','Canada','Estados Unidod']

casiAmerica = paisesNorteAmerica + paisesCentroAmerica

print(casiAmerica)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Contando elemento en una lista con el metod coun()

#utlilizando el metodo extend()

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = ['a', 'b', 'c']

lista1.extend(lista2)
print(lista1)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#utlilizando el metodo count()
lista1.append(1)
print(lista1)
lista1.count(1)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Elementos para buscar en una lista
#utlilizando el metodo index()

print(lista1.index(3))
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#utlilizando el metodo reverse()
lista1 = [1, 2, 3, 4, 5, 6]
#print(lista1)

#print(reversed(lista1))

for x in reversed(lista1):
    print(x)
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#utlilizando el metodo sort()
frutas2 = ['mago','guineo','piña','manzana']
frutas2.sort()
print(frutas2)
print(sorted(frutas2))

edades = [22,19,24,25,26,24,25,24]
edades.sort(reverse=True)
print(edades)"""
#############################################################################
"""thistuple = ('appel','banana','cherry')
print(thistuple)
emptytuple = ()
print(emptytuple)

thistuple = ('appel','banana','cherry')
print(len(thistuple))

thistuple = ("appple",)
print(type(thistuple))

#not tuple
thistuple = ("appple")
print(type(thistuple))"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""frutasTuple = (
    'sandia','melon','guineo','papaya','jocote','piña','manzana','uva','kiwi','limon','cerez',
    'granada'
)

print(frutasTuple)

print(frutasTuple[0])
print(frutasTuple[6])
print(frutasTuple[9])

print(frutasTuple[-1])
print(frutasTuple[-6])
print(frutasTuple[-9])"""

#No se puede modificar
#frutasTuple[0] = 'mango'
#print(frutasTuple)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Slicing en las tuplas

"""frutasTuple = (
    'sandia','melon','guineo','papaya','jocote','piña','manzana','uva','kiwi','limon','cerez',
    'granada'
)

tpl1 = frutasTuple[0:4]
print(tpl1)

tpl1 = frutasTuple[2:8]
print(tpl1)

tpl1 = frutasTuple[-3]
print(tpl1)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
frutasTuple = (
    'sandia','melon','guineo','papaya','jocote','piña','manzana','uva','kiwi','limon','cerez',
    'granada'
)

lst2tpl = list(frutasTuple)

print(type(lst2tpl))

lst2tpl.append('coco')
frutasTuple = tuple(lst2tpl)
print(lst2tpl)

print('fresa' in frutasTuple)"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Unir tuplas

"""tpl1 = ('sandia','melon','guineo','papaya','jocote','piña')
tpl3 = ('manzana','uva','kiwi','limon','cerez','granada')


jointuple = tpl1 + tpl3

print(jointuple)

#borrar tplas
del jointuple
print(jointuple)"""
#############################################################################
#Conjuntos

"""thisset = {'manzana','banana','piña'}
print(thisset)

thisset = {'manzana','banana','piña'}
print(len(thisset))"""

"""set1 = {'apple','cherry','banana','apple'}
print(set1)
print('apple' in set1)

for fruit in set1:
    print(fruit)

set2 = {1,2,3,4,5,4,4,4,6,7,4,1}
print(set2)
print(len(set2))
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Agregar elementos en los set
#usando el metodo add()
#se agregar un elemento, si desea agregar varios utilice update()

set1 = {'apple','cherry','banana','apple'}

set1.add('piña')
print(set1)

set2 = {'naranja','melocoton','jocote'}
set1.update(set2)
print(set1)"""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Eliminar elementos en un set()
#se utiliza remove,pop

"""set1 = {'apple','cherry','banana','apple'}
#print(set1)

#set1.pop()
#print(set1)

set1.remove('cherry')
print(set1)

set1.clear()
print(set1)

del set1
print(set1)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Union de conjuntos union()
#Convertir listas a Conjuntos
set1 = {1,2,3,4,5}
set2 = {2,6,9,8}

set3 = set1.union(set2)
print(set3)

lsSet = [1,2,3,4,5,'y','t','r','r','t']
setConvert = set(lsSet)
print(setConvert)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Interseccion de Conjuntos
set1 = {1,2,3,4,5}
set2 = {2,6,9,8}

set3 = set1.intersection(set2)
print(set3)

#Diferencia simetrica en conjuntos
set1 = {1,2,3,4,5}
set2 = {2,6,9,8}

set3 = set1.symmetric_difference(set2)
print(set3)"""
################################################################

"""thisdict = {
    "brand" : 'Ford',
    'Model' : 'Mustang',
    'year' : 1994
}

print(thisdict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
print(len(myfamily))

print(myfamily["childl"])
print(myfamily["child2"])
print(myfamily["child3"])"""

person = {
    'first_name'
    'country' : 'Failand',
    
}

















