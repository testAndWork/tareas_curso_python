#Manejo de Excepciones
#try, except,finally,else

"""try:
    print(x)
except:
    print('An exception ocurred')


#Example
x = int(input('Digite el numerador: '))
y = int(input('Digite el denominador: '))

print(x/y)
"""
################################################################
"""def divisin_segura(numerador, denominador):
    try:
        result = numerador / denominador
        return result
    except ZeroDivisionError:
        print('Error: No se puede dividir entre 0')
    except ValueError:
        print('Error: Ha ocurrido un problema')


x = int(input('Digite el numerador: '))
y = int(input('Digite el denominador: '))
print(divisin_segura(x,y))
"""
################################################################
#Ejercicio 2
#Convert str to int

"""def convert_2_int(cadena):
    try:
        entero = int(cadena)
        return entero
    except ValueError:
        print('Error: la cadena no es valida')

cad = '23232'  #'fgh'

print(convert_2_int(cad))
"""
################################################################
#Ejercicio 3
#Cree un programa que solicite al usuario ingresar un numero positivo
# y maneje excepciones en caso de entrada invalida

"""def num_entero(numero):
    try:
        if numero > 0:
            print('Es un numero entero positivo')
        elif numero == 0:
            print('El numero es cero')
    except ValueError:
        print('El numero es negativo')
        return numero
    except TypeError:
        print('Error: el valor no es correcto.')

number = int(input('Digite un numero: '))

print(num_entero(number))
"""
################################################################
# else manejo de excepciones 

"""try:
    print(x)
except:
    print('Error mesage')
else:
    print('Error mesae 2')
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Conversion de entrada
"""
entrada = input('Ingrese un numero: ')

try:
    numero = int(entrada)
    print(numero)
except ValueError:
    print('Error: La entrada, es un numero no valido')
else:
    print('La conversion fue exitosa')
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
try:
    print(x)
except:
    print('Error 1)
finally:
    print('El bloque try except finalizo)
################################################################
try:
    numerador = float(input('Ingrese numerador: '))
    denominador = float(input('Ingrese denominador: '))
    
    result = numerador / denominador
except ZeroDivisionError:
    print('Error: No podemos dividir entre 0')
else:
    print(f'El resultado es: {result}')
finally:
    print('El codigo ha sido ejecuatdo con exito!!!')
"""
################################################################
"""conexion = None

try:
    #Simulacion de la conexion a la base de datos
    conexion = 'Conexion abierta'
    #Operaciones a la base de datos
except Exception as e:
    print('Error', e)
finally:
    if conexion:
        
"""
################################################################
"""string = 'Hello'

if not type(string) is int:
    raise TypeError('Solo necesitamos enteros')
"""
################################################################
"""try:
    numerador = float(input('Ingrese numerador: '))
    denominador = float(input('Ingrese denominador: '))
    
    if denominador == 0:
        raise Exception('No se puede dividir por 0')
    
    result = numerador / denominador
except ZeroDivisionError:
    print('Error: No podemos dividir entre 0')
else:
    print(f'El resultado es: {result}')
finally:
    print('El codigo ha sido ejecuatdo con exito!!!')
"""
################################################################
#Validacion de edad
"""try:
    age = int(input('Ingrese la edad: '))
    if age < 18:
        print()
        raise Exception('Error: Menor de edad.')
except:
    print('El usuario debe ser mayor de edad.')
else:
    if age >= 18:
        print('El usuario es mayor de edad.')
"""

"""class MenorDeEdadError(Exception):
    pass

try:
    age = int(input('Ingrese la edad: '))
    if age < 18:
        raise MenorDeEdadError('Debe ser mayor de edad.')
except MenorDeEdadError as e:
    print('Error', e)
else:
    print('Eres mayor de edad')
finally:
    print('al fin se termino!')
"""
################################################################
#Raiz cuadrada
import math

class RaizNegativaError(Exception):
    pass

class ValorNumericoError(Exception):
    pass

def calcular_raiz(numero):
    if numero < 0:
        raise RaizNegativaError('No se pueden calcular raices de numeros negativos')
    return math.sqrt(numero)

try:
    numero = float(input('Ingresa el numero al que calcularas la raiz cuadrada:  '))
    result = calcular_raiz(numero)
except RaizNegativaError as e:
    print('Error:', e)
except ValueError:
    print('Error: Ingrese un valor numerico valido')
else:
    print(f'La raiz cuadrada de {numero} es: {result: .2f}')
finally:
    print('Ejecucion terminada con exito')






