thislist = ['apple','cherry','banana']
print(thislist)

thislist = ['apple','cherry','banana']
print(len(thislist))

vegetalesLst = ['tomate','papa','coliflor','zanahoria','cebolla']
print(len(vegetalesLst))

paisesLst = ['El salvador','Guatemala','Costa rica',
             'panama','honduras','nicaragua'
             ]
print(len(paisesLst))

thislist.append('oragen')
print(thislist)



lista4 = ['abe',34,True,10,'male']
print(lista4)
print(type(lista4[0]))
print(type(lista4[1]))
print(type(lista4[2]))
print(type(lista4[3]))


lst5 = ['juan',350,True,
        {'pasis:':'el salvador','ciudad':'san salvador'},
        [1,2,3,4,5],
        [2.0,3.0,4.0]
        ]
print(lst5)
print(len(lst5))
print(lst5[3])
print(type(lst5[3]))

lstNew = [lst5[0],lst5[1],lst5[2],lst5[5]]
indiceFinal = len(lstNew)-1
print(indiceFinal)
print(lstNew)
print(lstNew)

frutas = ['papaya','jocote','piña','melon','sandia']
print(frutas[-1])
print(frutas[-2])
print(frutas[-4])
print(frutas[-5])

frutas = ['papaya','jocote','piña','melon','sandia']
fruta1,fruta2, * sobran = frutas
print(fruta1)
print(fruta2)
print(sobran)

numTest = [1,2,3,4,5,6,7,8,9,10,11,12,13]
n1, n2, * nvarios, npenultimo, nultimo = numTest
print(n1)
print(n2)
print(nvarios)
print(nultimo)

numTest2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]
nInicio,  * nCentrales, nUltimo = numTest2
print(nInicio)
print(2*nCentrales)
print(nUltimo)

frutas = ['papaya','jocote','piña','melon','sandia']
print(len(frutas))
todoFruta = frutas[0:4]
print(todoFruta)

pruebafrutas = frutas[0:]
print(pruebafrutas)
slice = frutas[1:3]
slice2 = frutas[2:4]
slice3 = frutas[1:4]
print(slice)
print(slice2)
print(slice3)
print(frutas[4])
print(frutas[1:])
print(frutas[::2])

frutas = ['papaya','jocote','piña','melon','sandia']
print(frutas[-4])
print(frutas[-3:-1])
print(frutas[-3:])
print(frutas[::-1])
#agregar elementos a la lista en cualquier pocision
frutas = ['papaya','jocote','guineo','piña','melon','sandia']
frutas[2] = 'fresas'
print(frutas)

frutas = ["manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa",
          "papaya", "piña", "cereza", "limón", "granada", "frambuesa", "mandarina", "durazno", "coco", "ciruela"]

'melón' in frutas

'papaya' in frutas

for fruta in frutas:
    if fruta == 'papaya':
        print('si hay')
    else:
        print('no hay')

#INSERTAR ELEMENTOS EN UNA LISTA
frutas = ["manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa",
          "papaya", "piña", "cereza", "limón", "granada", "frambuesa", "mandarina", "durazno", "coco", "ciruela"]
frutas.insert(3,'jocote')
'jocote' in frutas
print(frutas)
frutas.insert(6,'guineo')
print(frutas)

#eliminar elementos en una lista el metodo 
print(frutas)
frutas.remove('guineo')
print(frutas)
#eliminar elementos en una lista pop()
print(frutas)
frutas.pop()
frutas.pop(19)
print(frutas)
#eliminar elementos en una lista del
print(frutas)
del frutas [0]
print(frutas)
del frutas [4:9]
print(frutas)
#del frutas
#print(frutas)

#limpipiar items de lista
paisesCentroamerica = ['belice','El salvador','Guatemala','Costa rica',
             'panama','honduras','nicaragua'
             ]
print(paisesCentroamerica)
paisesCentroamerica.clear()
print(paisesCentroamerica)

#copiar lista
paisesNorteamerica = ['estados unidos','canda','mexico']
paisesCentroamerica = ['belice','El salvador','Guatemala','Costa rica',
             'panama','honduras','nicaragua'
             ]
newpaises = paisesNorteamerica.copy()
print(newpaises)
print(paisesCentroamerica)
print(paisesNorteamerica)

#unir lista
casiamerica = paisesNorteamerica + paisesCentroamerica
print(casiamerica)

lista1 = [1,2,3,4,5,6]
lista2 = ['a','b','c']
lista1.extend(lista2)
print(lista1)

lista1.append(1)
print(lista1)
lista1.count(1)

lista1.index(3)

frutas2 = ['banana','guineo','mango','limon','sandia']
frutas2.sort()
print(frutas2)

frutas2 = ['banana','guineo','mango','limon','sandia']
frutas2.reverse()
print(frutas2)

edades = [22,19,24,25,26,24,25,24]
edades.sort(reverse= True)
print(edades)

thistuple = ('apple','cherry','banana')
print(len(thistuple))


thistuple = ('apple',)
print(type(thistuple))

frutasTupla = ("manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa",
          "papaya")
print(frutasTupla)

print(frutasTupla[-1])
print(frutasTupla[-6])
print(frutasTupla[-9])

#slicing
frutasTupla = ("manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa",
          "papaya")
tupla1 = frutasTupla[0:4]
print(tupla1)

tupla2 = frutasTupla[2:8]
print(tupla2)

#cambiando tuplas a listas
lst2tpl = list(tupla2)
print(type(lst2tpl))
print(lst2tpl)
lst2tpl.append('coco')
tupla2 = tuple(lst2tpl)
print(tupla2)

'fresa' in tupla2

joinTpl = tupla1+tupla2
print(joinTpl)

#del joinTpl
#print(joinTpl)

thisset = {'apple','banana','cherry'}
print(len(thisset))

set1 = {'apple','banana','cherry','apple'}
print(set1)

set2 = {1,2,3,4,3,4,3,4,3,4,3,4,1}
print(len(set2))

set1 = {'apple','banana','cherry','apple'}
'apple' in set1

for fruit in set1:
    print(fruit)

#agregando elemento add
set1 = {'apple','banana','cherry','apple'}
set1.add('piña')
print(set1)
set2 = {'naranja','melocoton','jocote'}
set1.update(set2)
print(set1)

set1.pop()
set1.remove('cherry')
print(set1)

#set1.clear()
#print(set1)

#del set1
#print(set1)


set1 = {1,2,3,4,5}
set2 = {2,6,9,8}

set3 = set1.union(set2)
print(set3)

listaset = [1,2,3,4,5,'t','y','r']
setConvert = set(listaset)
print(setConvert)


#convertir listas a conjunto
set1 = {1,2,3,4,5}
set2 = {2,6,9,8}
print(set1)
set3 = set1.intersection(set2)
print(set3)  

set1 = {1,2,3,4,5}
set2 = {2,6,9,8}

set3 = set1.symmetric_difference(set2)
print(set3)  

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

print(myfamily ['childl'])
print(myfamily['child2'])
print(myfamily['child3'])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['age'])
person['City'] = 'Inventada' 
print(person)



