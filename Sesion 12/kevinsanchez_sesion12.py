# read()

"""f = open('lorem.txt')

txt = f.read()

print(txt)

print(f.read(10))

f.close()

######################################################

f = open('lorem.txt')
linea = f.readline()
print(linea)

print(f.readline())
f.close()
######################################################

f = open('lorem.txt')
lines = f.readlines()
print(lines)
f.close()

######################################################

file = 'lorem.txt'
f = open(file)
lines = f.read().splitlines()
print(lines)
f.close()

######################################################
#with
file = 'lorem.txt'
with open(file) as f:
    lines = f.read().splitlines()
    print(lines)

######################################################
file2 = 'myfile.txt'
with open(file2, 'x'):
    pass

#file2 = 'myfile.txt'
with open('archivivto.txt', 'w'):
    pass

with open('prueba.txt', 'a') as f:
    f.write('un nuevo archivo')
    pass

######################################################
import os 

os.remove('archivivto.txt')

if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print('no existe el archivo')

import os 

try:
    if os.path.exists('myfile.txt'):
        os.remove('myfile.txt')
        print('Archivo eliminado')
    else:
        raise FileExistsError('no existe el archivo')
except FileNotFoundError as err:
    print(err)
finally:
    print('Fin del programa')    

######################################################
#Archivos

import json

datos_dct = {
    'Nombre':'John Doe',
    'Pais':'Australia',
    'Ciudad':'Sydney',
    'Habilidades': ['JavaScript','Python','Java']
}
"""
datos_json = """{
    'Nombre':'John Doe',
    'Pais':'Australia',
    'Ciudad':'Sydney',
    'Habilidades': ['JavaScript','Python','Java']
}"""

"""print(type(datos_dct), type(datos_json))

#cambiando json a diccionario
datos_dct = json.loads(datos_json)


print()"""

######################################################

"""import csv

with open('auto-mpg.csv') as f:
    csv_reader = csv.reader(f,delimiter=',')
    linecount = 0
    for fila in csv_reader:
        if linecount == 0:
            print(f'El nombre de la columna es: {",".join(fila)}') 
            linecount += 1
        else:
            print(f'{fila[8]}')
            linecount += 1
"""

import pandas as pd

data = pd.read_csv('auto-mpg.csv')

print(data)
print(data.head())
print(data.tail())
print(data['car name'])
print(data['horsepower'].mean())
print(data['horsepower'].sum())
print(data['horsepower'].round(1))

import matplotlib.pyplot as plt

plt.figure()
print(plt.hist(data['horsepower']))
plt.show()

"""
import matplotlib.pyplot as plt

plt.hist(data['horsepower'])
"""

######################################################
# archivos pickle

"""import pickle

dastos_dic = {
    'nombre': 'Doe',
    'edad': 30
}

# creando un archivo serealizado
with open('archivito.pkl', 'wb') as file:
    pickle.dump(dastos_dic, file)

with open('archivito.pkl', 'rb') as file:
    dastos_info = pickle.load(file)
    print('Los datos', dastos_info)
"""
######################################################
# Leer y crear un archivo CSV

"""import csv

alumnos = [
    {'Nombre': 'Doe', 'Nota': 6.0,},
    {'Nombre': 'Snow', 'Nota': 9.0,},
    {'Nombre': 'Harry', 'Nota': 1.0,}
    ]

alumnos = list(alumnos)

with open('registro_alumnos.csv', 'w') as file:
    campos = ['Nombre','Nota']
    escribir = csv.DictWriter(file, fieldnames= campos)
    escribir.writeheader()
    for alumno in alumnos:
        escribir.writerow(alumno)

with open('registro_alumnos.csv', 'r') as file:
    leer = csv.DictReader(file)
    print('este es un registro de alumnos')
    for alumno in leer:
        print(f'El alumno es: {alumno["Nombre"]} con nota de {alumno["Nota"]}')
"""

