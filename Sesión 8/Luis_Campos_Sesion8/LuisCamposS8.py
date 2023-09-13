def my_function():
    print('Hola Mundo')
    print('**************')
my_function()


def my_function(nombre):
    print(f'Hola buenos dias {nombre} !!!!!')
my_function('Luis')


def sumar(x,y):
    suma= x + y
    return suma
resultado = sumar(4,5)

print('la suma es :', resultado)

def print_name(name):
    print(name + ' es el nombre')
print_name('Luis')
print_name('Juan')
print_name('siri')

def my_function(nombre1, nombre2):
    print(nombre1 + '' + nombre2)
my_function('Juan','pablo')

def my_function(nombre):
    print(f'Hola buenos dias {nombre} !!!!!')
    #nombres es parametro
    #Luis es argumento
my_function('Luis')

#ejemplo de funcion para calcular el area de un rectangulo

def area_rectangulo(base , altura):
    return base * altura
    
area = area_rectangulo(4,5)
print('el area de un rectangulo es:', area)

#ejemplo2
def imprimir_lista(lista):
    for it in lista:
        print(it)
lst = [1,2,'hola']
imprimir_lista(lst)

#ejemplo3
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
num = 5
if es_par(num):
    print ('el numero es par')
else:
    print('el numero es impar')

#ejemplo 4 funcion que regresa una lista de numero pares

def lista_pares(n):
    lst_pares = []
    for it in range(n+1):
        if it % 2 == 0:
            lst_pares.append(it)
    return lst_pares

lista_pares(20)

def my_function(*nombre):
    print('el nombres ' + nombre[0])

my_function('Luis','Juan','pablo')

def imprimirArgumentos(*args):
    for arg in args:
        print(arg)
imprimirArgumentos(1,2,3,'hola','mundo',['a','b'])

def prom_notas(*notas):
    totalNotas = 0
    for nota in notas:
        totalNotas += int(nota)
    promedio = totalNotas/len(notas)
    return promedio
notas = [6,7,8,9,6,8,9,10]
promedioFinal = prom_notas(*notas)
print(round(promedioFinal,1))

def concatenar (*agrs):
    resultado = ''.join(agrs)
    return resultado
frutas = 'guineo ' ,'naranja ' ,'limon '
mixFrutas = concatenar(*frutas)
print('mix frutas:', mixFrutas)

def media_aritmetica(*args):
    total = sum(args)
    cantidad = len(args)
    media = total/cantidad
    return media
notas = [6,7,8,9,6,8,9,10]
promedioFinal = media_aritmetica(*notas)
print(round(promedioFinal,1))

def productoria(*args):
    producto = 1
    for it in args:
        producto *= it
    return producto
numeros = [1,2,3,4,5,6,7]
totalMultiplicacion = productoria(*numeros)
print('el total es : ',totalMultiplicacion)

def my_function(nombre1, nombre2, nombre3):
    print(nombre1 + ' ' + nombre2+ ' '+ nombre3)
my_function(nombre1 ='Juan',nombre2='pablo',nombre3='jose')

def my_funcion(nombre1,nombre2,nombre3,nombre4='Lopez'):
    print(nombre1+' '+ nombre2+ ' '+nombre3+' '+nombre4)

my_funcion(nombre1='Juan',nombre2='Jose',nombre3='Luis')

def my_function(**kid):
    print('El ultimo nombre es '+ kid['mname'])
my_function (pnombre= 'juan', mname ='maria',uname = 'pablo')

def crear_perfil(**kwargs):
    perfil = {}
    for clave, valor in kwargs.items():
        perfil[clave] = valor 
        return perfil
usuario = crear_perfil(nombre = 'ana', edad = 28, ciudad= 'barcelona')
print('perfil usuario:', usuario)

def ejemplo (x):
    return x ** 2
print(ejemplo(3))
print(ejemplo(4))
print(ejemplo(5))

def factorial(n):
    if n ==0:
        return 1
    else:
        return n* factorial(n-1)
numero = 3
resultado = factorial(numero)
print(f'el factorial de {numero} es {resultado}')

def factorial_no_recursivo(n):
    result = 1
    for it in range(1,n +1):
        result*= it
    return resultado
n= 3
print(f'el factorial de {n} es {factorial_no_recursivo(n)}')

def suma_sin_recursividad(n):
    suma= 0
    for it in range(1, n+1):
        suma += it
        return suma
n= 4
print(f'la suma es : {suma_sin_recursividad(n)}' ) 

def suma_recusividad(n):
    if n == 1:
        return 1
    else:   
        return n + suma_recusividad(n - 1)
n = 4
print(f'la suma es: {suma_recusividad(n)}')


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

x = lambda a : a + 10

print(x(5))

f = lambda x : x**2 +2 * x + 3
f(3)
x = lambda a, b : a * b

print(x(5, 6))

x = lambda a, b, c : a + b + c

print(x(5, 6, 2))

def myfunc(n):
    return lambda a: a *n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

id_empleados = [341,45,435,676,345,345,676,764,242]
pares= filter(lambda x: x%2 == 0 , id_empleados)
print(list(pares))

datos = [(3, 8), (1, 5), (6, 2)]
ordenado = sorted(datos, key=lambda x: x[1])
print(ordenado) 

potencia = lambda x, n: x ** n
resultado = potencia(2, 3)
print(resultado)

maximo = lambda x, y: x if x > y else y
resultado = maximo(7, 12)
print(resultado)

reversa = lambda cadena: cadena[::-1]
resultado = reversa("Python")
print(resultado)

operacion = lambda x, y: (x ** 2) + (2 * y) - 3
resultado = operacion(4, 7)
print(resultado)

secuencia_pares = lambda n: [i for i in range(2, n*2 + 1, 2)]
num_elementos = 5
pares = secuencia_pares(num_elementos)
print(pares)
