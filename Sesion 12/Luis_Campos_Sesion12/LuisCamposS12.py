f = open('lorem.txt')
f = open('lorem.txt', 'rt')

print(f)

print(f.read())

f = open('lorem.txt')
txt = f.read()
print(txt)
print(type(txt))

f.close()

f = open('lorem.txt')
print(f.read(10))

print(f.read(20))
f.close()

f = open('lorem.txt')
line = f.readline()
print(type(line))
print(line)

print(f.readline())
print(f.readline())
f.close()


archivo = 'lorem.txt'

f = open(archivo)
lines = f.readlines()
print(lines)
f.close()

f= open(archivo)
lines = f.read().splitlines()
print(lines)
f.close()

with open(archivo) as f:
    lines = f.read().splitlines()
    print(lines)

with open(archivo, 'a') as f:
    f.write('\n este texto debe ir al final del archivo')

#crear archivo

with open(archivo,'x'):
    pass
file2= 'myfile.txt'
with open(file2,'x'):
    pass
file3= 'archivit.txt'
with open(file3,'x'):
    pass


with open('preuba.txt','a') as f:
    f.write('crea un nuevo archivo python')

import os
os.remove('archivito.txt')

if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print('no existe el archivo')


try:
    if os.path.exists('myfile.txt'):
        os.remove('myfile.txt')
        print('archivo eliminado')
    else:
        raise FileNotFoundError('no existe el archivo')
except FileNotFoundError as err:
    print(err)
finally:
    print('fin del programa')

os.rmdir('borrado/')
os.mkdir('prueba/')

datos_dct ={
    'nombre':'john doe',
    'pais':'austrailia',
    'ciudad':'sidney',
    'habilidades':['javascrip','react','python']
} 

datos_jason =  """{
    "nombre": "John dane",
    "pais": "Australia",
    "ciudad": "Sidney",
    "habilidades": ["Javascrip", "React", "Python"]
}"""

type(datos_dct), type(datos_jason)

import json

datos_dct = json.dumps(datos_jason)
type(datos_dct), type(datos_jason)

import csv

with open('auto-mpg.csv') as f:
    csv_reader = csv.reader(f,delimiter= ',')
    line_count = 0
    for fila in csv_reader:
        if line_count ==0:
            print(f'el nombre de la columna es {",".join(fila)}')
            line_count+=1
        else:
            print(f'{fila[8]}')
            line_count =+1

import pandas as pd

data = pd.read_csv('auto-mpg.csv')
data
data.tail


import pickle
datos_dict = {'nombre':'Doe', 'edad:':30} 

#creando archivo pickle
with open('archivito.pkl','wb') as file:
    pickle.dump(datos_dict, file)
import pandas as pd
data = pd.read_csv('auto-mpg.csv')
import matplotlib.pyplot as plt
plt.figure()
plt.hist(data['horsepower'])
plt.show()

import csv

alumnos =[
    {'Nombre': 'Doe','Nota': 6.0},
    {'Nombre': 'Snow','Nota': 9.0},
    {'Nombre': 'Harry','Nota': 1.0}
    ]

with open('registro_alumnos.csv','w', newline = '' ) as file:
    campos   = ['Nombre','Nota']
    escribir = csv.DictWriter(file, fieldnames= campos)
    escribir.writeheader()
    for alumno in alumnos:
        escribir.writerow(alumno)
        
    
with open('registro_alumnos.csv','r') as file:
    leer = csv.DictReader(file)
    print('Este es un regitro de alumnos')
    for alumno in leer:
        print(f'El alumno es: {alumno["Nombre"]} con nota de {alumno["Nota"]}')

