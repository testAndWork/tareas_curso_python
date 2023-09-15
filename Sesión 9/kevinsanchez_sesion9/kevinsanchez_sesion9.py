#Modulos

#import libreria.mymodulo as mm
#import libreria.areas as ar
import libreria.mix_modulo as mx

"""print(mm.sumarN(4,5))
print(mm.resatrN(4,5))

print(ar.area_rectangular(5,4))
"""

archivo = "power.csv"
cargar_datos = mx.cargar_datos(archivo)
print(cargar_datos.head())

lst = [1,2,3,4,5]
prom = mx.calcular_promedio(lst)

print('El promedio es: ', prom)

