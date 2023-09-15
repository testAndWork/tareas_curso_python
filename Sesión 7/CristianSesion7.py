paises = ['gautemala','el salvador','honduras']
print(len(paises))


list1 = {'pais':'El slavador', 'ciudad':'nejapa'}

print(list1)


frutas = ['papaya','melon','sandia','mango']

print(frutas[-1])
print(frutas[-2])

numTest2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]
nInicio, *ncentrales, nUltimo  = numTest2
print(nInicio)
print(2*ncentrales)
print(nUltimo)


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

frutas.insert(3,'jocote')
'jocote' in frutas

print(frutas)


#remove eliminar elementos en una lista

frutas.remove('manzana')
print(frutas)