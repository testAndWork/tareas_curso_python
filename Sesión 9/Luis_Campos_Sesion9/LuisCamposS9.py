import math
raiz = math.sqrt(4)
print('la raiz cuadrada es:', raiz)

print(math.pow(3,2))
print(math.pi)

print(math.log10(20))

from math import pi, e, sqrt, pow

print(e)

print(sqrt(4))

from statistics import *

ages = [30,25,40,20,26]
print(mean(ages))

print(stdev(ages))

from random import random, randint

print(random())
print(randint(1,9))

import mymodule
print(mymodule.sumar(5,5))

from mymodule import sumar
print(sumar(4,5))

import library.areas as ar
print('el area de rectangulo es:',ar.area_rectangulo(4,5))

import library.mixmodule as mx
archivo = "Power.csv"
carga_datos = mx.cargar_datos(archivo)

print(carga_datos.head())

lst = [1, 2, 3, 4, 5]
prom = mx.calcular_promedio(lst)

print('EL promedio es : ', prom)