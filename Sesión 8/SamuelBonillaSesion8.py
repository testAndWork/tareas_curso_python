def my_function():
    print("Hola Mundo desde una funcion ")
    print("*****************************")
    
my_function()

def saludar():
    print("Hola, buenos dias")
    
saludar()
print("Me gusta saludar ", saludar())

#Argumento

def saludar(nombre):
    print(f"Hola, buenos dias {nombre}!!!")
    
saludar("Juan")

def sumar(x,y):
    suma = x+y
    return suma

resultado = sumar(4,5)
print(f"La suma es: {resultado}")

def print_name(name):
    print(name + " es el nombre")
    
print_name("Juan")
print_name("Maria")

#Numero de argumentos

def my_function(nombre1, nombre2):
    print(nombre1 + ' ' + nombre2)
    
my_function('Juan','Pablo')

#Ejemplo: calcular el area de un triangulo

def area_rectangulo(base, altura):
    return base * altura

area = area_rectangulo(4,5)
print("El area del triangulo es", area)

#Ejemplo 2: Funcion para imprimir una lista

def imprimir_lista(lista):
    for it in lista:
        print(it)
        
lst = [1, 2, "Hola"]

imprimir_lista(lst)

#Ejemplo 3: Funcion para verificar si un numero es par

def es_par(numero):
    if numero % 2==0:
        return True
    else:
        return False
    
num = 6

if es_par(num):
    print("El numero es par")
else:
    print("El numero es impar")
    
#Ejemplo 4: Funcion que regresa una lista de numeros pares

def lista_pares(n):
    lstPares = []
    for it in range(n+1):
        if it % 2 == 0:
            lstPares.append(it)
        return lstPares
    
print(lista_pares(20))

#Argumento arbritarios

def my_function(*nombre):
    print('El nombre es '+ nombre[0])
    
my_function('Juan', 'Mario', 'Pablo')

#Ejemplo

def imprimir_argumento(*args):
    for arg in args:
        print(arg)
        
imprimir_argumento(1,2,3, 'Hola', 'Mundo',['a','b'])

#Ejemplo

def prom_notas(*notas):
    totalNotas = 0
    for nota in notas:
        totalNotas += int(nota)
    promedio = totalNotas/len(notas)
    return promedio

notas = [6,7,8,9,6,9,8,10]

promedioFinal = prom_notas(*notas)
print(round(promedioFinal,1))

#Join

def concatenar(*args):
    resultado = " ".join(args)
    return resultado

frutas = 'guineo', 'naranja', 'limon'

mixFrutas = concatenar(*frutas)
print('Mix de frutas: ', mixFrutas)

#media aritmerica

def media_aritmerica(*args):
    total = sum(args)
    cantidad = len(args)
    media = total/cantidad
    return media

notas = [6,7,8,9,6,9,8,10]

promedioFinal = media_aritmerica(*notas)
print("El promedio es: ",round(promedioFinal,1))

#Ejemplo

def productoria(*args):
    producto = 1
    for it in args:
        producto *= it
    return producto

numeros = [1,2,3,4,5,6,7]

totalMultiplicacion = productoria(*numeros)

print("El total es : ",totalMultiplicacion)

#Argumento de palabras clave

def my_function(nombre1, nombre2, nombre3):
    print(nombre1 + ' ' + nombre2 + ' ' + nombre3)
    
my_function(nombre1 = 'Juan', nombre2 = 'Pablo', nombre3 = 'José')

def saludar(nombre, mensaje):
    print(f"{mensaje}, {nombre}!")
    
saludar(nombre="Juan", mensaje="Hola a todos")

#kwargs

def my_function(**kid):
    print('El ultimo nombre es '+ kid['mname'])
    
my_function(fname = 'Juan',mname = 'Maria', lname = 'Pablo')

#Factorial sin recursividad

def factorial(n):
    print(" ->>",n)
    if n == 0:
        return 1  # Caso base: factorial de 0 es 1
    else:
        print('else se llama ella misma')
        return n * factorial(n - 1)  # Caso recursivo

numero = 3
resultado = factorial(numero)

print(f"El factorial de {numero} es {resultado}")


def factorial_no_recursivo(n):
    result = 1
    for it in range(1,n+1):
        result *= it
    return resultado

n=3
print(f"El factorial de {n} es {factorial_no_recursivo(n)}")

def suma_sin_recursividad(n):
    suma = 0
    for it in range(1, n + 1):
        suma += it
    return suma
def suma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n - 1)
n = 4
    
print(f'Lasuma es : {suma_sin_recursividad(n)}')    
print(f'Lasuma es : {suma_recursiva (n)}')

#lambda

x = lambda a: a + 10

print(x(5))
print(x(2))

f = lambda x: x**2 + 2*X + 3
f(3)

x = lambda a, b, c : a + b + c

print(x(5, 6, 2))

x = lambda a, b : a * b

print(x(5, 6))

#Filtrar listas

id_empleados = [341,45, 435, 676, 345,345, 676, 764,242]

pares = filter(lambda x: x%2 == 0, id_empleados)

print(list(pares))