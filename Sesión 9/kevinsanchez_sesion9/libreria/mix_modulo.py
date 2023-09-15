#Modulo Analisis de datos

import pandas as pd
import numpy as np

def cargar_datos(archivo):
    """Cargar datos archivos csv, utilizando pandas"""
    data = pd.read_csv(archivo)
    return data

def calcular_promedio(columna):
    """Calcular el promedio de una columna de valores utilizando numpy"""
    promedio = np.mean(columna)
    return promedio