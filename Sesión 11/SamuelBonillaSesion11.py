#Manejo de Excepciones

#try:
    #print(x) #Generador o donde ocurre el error
#except:
    #print("An exception ocurred") #Nos dice que tipo fue el error
    
def division_seguro(numerador, denominador):
    
    try:
        resultado = numerador / denominador
        return resultado

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")
        
    except ValueError:
        print("Error: Ha ocurrido algun problema")

x = int(input("Ingrese numerador: "))
y = int(input("Ingrese denominador: "))


print(division_seguro(x,y))

def convert_2_int(cadena):
    try:
        entero = int(cadena)
        return entero
    except ValueError:
        print("Error, la cadena no es valida")

cad = '23423424'

print(convert_2_int(cad))

print(type(intcad))

def validar(num):
    try:
        if num >0:
            print('El numero es positivo')
            return num
        elif num == 0:
            print('El numero es cero')
        else:
            print('El numero es negativo')

    except TypeError:
        print('Error: ha ocurrido un problema')

num = int(input('Ingrese un numero: '))
validar(num)

#Conversion de entrada

entrada = input("Ingrese un numero: ")

try:
    numero = int(entrada)
    print(numero)
except ValueError:
    print("Error en la entrada, ese numero no es valido")
else:
    print("La conversion fue exitosa")
    
#Finally en excepciones

try:
    print(x)
except:
    print("Error 1")
    
finally:
    print("El bloque try except finalizo")
    
try:
    numerador = float(input("Ingrese el numerador: "))
    denominador = float(input("Ingrese el denominador: "))
    
    resultados = numerador / denominador
    
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")
    
else:
    print("El resultado es: ", resultados)
    
finally:
    print("El codigo ha sido ejecutado con éxito")
    
    
conexion: None
try:
    conexion = "Conexion Abierta"
except Exception as e:
    print("Error:", e)
finally:
    if conexion:
        print("Cerrando la conexion...")
        conexion = None
        
#raise

string = "Hello"

if not type(string) is int:
    raise TypeError("Solo necesitabamos enteros")

#Eejmplo

try :
    numerador   = float(input('Ingrese el Numerador: '))
    denominador = float(input('Ingrese el denominador: '))
    
    if denominador == 0:
        
        raise ZeroDivisionError("No se puede dividir por cero")
    
    resultado = numerador / denominador

except ZeroDivisionError:
    print('Error: No se puede dividir entre cero')

else: 
    print('El resultado es: ', resultado)
    
finally:
    print('El codigo ha sido ejecutado con éxito')
    
    
#Ejemplo

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
    
    
#Ejemplo
class MenorDeEdadError(Exception):
    pass

try:
    edad = int(input("Digite la edad"))
    if edad < 18:
        raise MenorDeEdadError("Error: debes ser mayor de edad")
except MenorDeEdadError as e:
    print('Error', e)
else:
    print("Eres mayor de edad!")
    
finally:
    print("Al fin se termino")
    
#Tarea
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
    
except RaizNegativaError as er:
    print("Error", er)
    
except ValueError:
    print("Error: Ingrese un valor numerico Valido")

else:
    print(f"La raiz cuadrada de {numero} es: {resultado : .2f} ")
finally:
    print(24*'\*')
    print("\nEjecución terminada con Exito\n")
    print(24*'\*')