
x = int(input('digite numerador'))
y = int(input('digite denominador'))
print(x/y)

try:
    print(x)
except NameError:
    print('Variable is not define')
except:
    print('anything else')
#Division segura

def divsion_segura (numerador,denominador):
    try:
        resultado = numerador/denominador
        return resultado
    except ZeroDivisionError:
        print('error de dominio:no se puede dividir entre 0')
    except ValueError:
        print('error: ha ocurrido un problema')

x= float(input('digite numerador'))
y= float(input('digite denominador'))
divsion_segura(x,y)

def convert_2_int (cadena):
    try:
        entero = int(cadena)
        return entero
    except ValueError:
        print('error: ha ocurrido un problema')
cad = '233423423'
intcad = convert_2_int(cad)
type(intcad)

def num_positivo():
    try:
        numero = int(input('ingrese numero'))
        num = numero > 0
        return num
    except TypeError:
        print('error:ingreso letra')
    except SyntaxError:
        print('error el numero es negativo')
    
num_positivo()



entrada = input('ingrese un numero')

try:
    numero = int(entrada)
    print(numero)
except:
    print('ERROR: la entrada, es numero invalido')
else:
    print('la conversion fue exitosa!!!')


try:
    numerador = float (input('ingrese el numerador'))
    denominador = float(input('ingrese el denominador'))
    resultado = numerador/ denominador
except ZeroDivisionError:
    print('error: no se puede dividir entre 0')
else:
    print('el resultado es :', resultado)
finally:
    print('el codigo ha sido ejecutado con exito')



x = -1
if x < 0 :
    raise Exception('no numeros negativos')

string = 'hello'
if not type(string) is int:
    raise TypeError('solo necesitamos enteros')

try:
    numerador = float (input('ingrese el numerador'))
    denominador = float(input('ingrese el denominador'))
    if denominador == 0:
        raise ZeroDivisionError('no se puede dividir por cero')
    resultado = numerador/ denominador
except ZeroDivisionError:
    print('error: no se puede dividir entre 0')
else:
    print('el resultado es :', resultado)
finally:
    print('el codigo ha sido ejecutado con exito')


class MenorDeEdadError(Exception):
    pass

try:
    edad = int(input('Digite la edad: '))
    if edad < 18:
        raise MenorDeEdadError('Error: Debes ser mayor de edad.')
        
except MenorDeEdadError as e:
        print('Error', e)
else:
    print('Eres mayor de edad!')
    
finally:
    print('al fin se terminó')

class MenorDeEdadError(Exception):
    def __init__(Error, edad):
        Error.edad = edad
        Error.mensaje = f"Error! La edad ingresada es menor de 18 años."
def verificar_edad(edad):
    if edad < 18:
        raise MenorDeEdadError(edad)
    else:
        print("Acceso concedido. Puedes continuar.")
try:
    edad = int(input("Ingrese su edad: "))
    verificar_edad(edad)
except MenorDeEdadError as e:
    print(e.mensaje)
except ValueError:
    print("Error: Ingrese un valor numérico válido para la edad.")

import math

class RaizNegativaError(Exception):
    pass

class ValorNumericoError(Exception):
    pass

def calcular_raiz(numero):
    if numero < 0:
        raise RaizNegativaError("No se puede calcular raices de numeros negativos")
    return math.sqrt(numero)

try:
    numero= float(input("Ingrese el numero al que calculara la raiz cuadrada"))
    
    resultado = calcular_raiz(numero)
    
except RaizNegativaError as err:
    print("!!!!Error", err)
    
except ValueError:
    print("Error: Ingrese un valor numerico Valido")

else:
    print(f"La raiz cuadrada de {numero} es: {resultado : .2f} ")
finally:
    print(24*'\*')
    print("\nEjecución terminada con Exito\n")
    print(24*'\*')
