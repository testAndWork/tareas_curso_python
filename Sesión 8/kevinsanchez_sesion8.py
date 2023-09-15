"""
Ejemplo de funcion

def my_function():
    print('Mi funcion')
    print('***********************')


my_function()


def saludar():
    print('Hola muy buenos dias!!!!!')

print('Me gusta saludar', saludar())


def saludar(nombre):
    print(f'Hola muy buenos dias {nombre}!!!!!')

print(saludar('Juan'))

def sumar(x,y):
    suma = x + y
    return suma

result = sumar(4,5)

print(f'La suma es {result}')


def print_name(name):
    print(name + ' es el nombre')

print(print_name('siri'))


def my_function(nombre1,nombre2):
    print(nombre1 +' '+ nombre2)

print(my_function('Juan','Pablo'))


def my_function(nombre1,nombre2):
    print(nombre1 +' '+ nombre2)

print(my_function('Juan'))
"""
######################################################################
#Funcion para calcular el area de un triangulo

"""def area_rectangulo(base,altura):
    return base * altura

area = area_rectangulo(4,5)

print(f'El area de un rectangulo es {area}')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def imprimir_lista(lista):
    for it in lista:
        print(it)

lst = [1,2,'hola']
print(imprimir_lista(lst))

lst = [1,2,2.9,4.5]
print(imprimir_lista(lst))


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = 5

if es_par(num):
    print('El numero es par')
else:
    print('El numero es impar')
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Funcion que regresa una lista de numeros pares

"""def lista_pares(n):
    lstPares = []
    for it in range(n + 1):
        if it % 2 == 0:
            lstPares.append(it)
    return lstPares

#nPares = 10
print(lista_pares(20))

######################################################################
def my_function(*nombre):
    print('El nombre es ' + nombre[2])

my_function('Juan','Mario','Pablo')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def imprimir_argumentos(*args):
    for arg in args:
        print(arg)

print(imprimir_argumentos(1,2,3,'Hola','mundo',['a','b']))


def prom_notas(*notas):
    totalNotas = 0
    for nota in notas:
        totalNotas += nota
    promedio = totalNotas/len(notas)
    return promedio

notas = [6,8,7,9,10,8,9,9]
promedioFinal = prom_notas(*notas)
print(promedioFinal)
"""
######################################################################
"""def concatenar(*args):
    result = " ".join(args)
    return result

frutas = 'guineo','naranja','limon'
mixFrutas = concatenar(*frutas)
print('Mix de frutas', mixFrutas)
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""def media_aritmetica(*args):
    total = sum(args)
    cantidad = len(args)
    media = total/cantidad
    return media

notas = [6,8,7,9,10,8,9,9]
promedioFinal = media_aritmetica(*notas)
print('El promedio es: ', promedioFinal)


def productoria(*args):
    producto = 1
    for it in args:
        producto *= it
    return producto

numeros = [1,3,4,5,6,7]
totalMulti = productoria(*numeros)
print('El total es: ', totalMulti)
######################################################################

def miNombres(nombre1,nombre2,nombre3):
    print(nombre1 + ' ' + nombre2 + ' ' + nombre3)

print(miNombres(nombre1='Juan',nombre2='Mario',nombre3='Pablo'))

def saludarH(nombre1,mensaje):
    print(f'{nombre1} {mensaje}')

print(saludarH(nombre1='Juan',mensaje='Buenos dias!'))

def miNombres(nombre1,nombre2,nombre3,nombre4='Lopez'):
    print(nombre1 + ' ' + nombre2 + ' ' + nombre3)

print(miNombres(nombre1='Juan',nombre2='Mario',nombre3='Pablo'))


def generar_informe(titulo,contenido,autor):
    informe = f'Titutlo: {titulo}\n Contenido: {contenido}\n Autor{autor} '
    print(nombre1 + ' ' + nombre2 + ' ' + nombre3)

print(miNombres(nombre1='Juan',nombre2='Mario',nombre3='Pablo'))
"""
##########################################################################################
"""def myFunction(**kid):
    print('El ultimo nombre es: ', kid['unnombre'])

print(myFunction(fnombre='Juan',mname='Maria',lname='Pablo'))

def crear_perfil(**kwargs):
    perfil = {}
    for clave,valor in kwargs.items():
        perfil[clave] = valor
    return perfil

usuario = crear_perfil(nombre='Ana',edad=28,Ciudad='Barcelona')
print('perfil de usuario: ', usuario)
##########################################################################################

def function():
    pass

##########################################################################################
#Factorial sin recursividad
def factorial_no_recursivo(n):
    result = 1
    for it in range(1,n+1):
        result *= it
    return result

n = 3
print(f'El factorial de {n} es {factorial_no_recursivo(3)}')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def facorial(n):
    print(" -->", n)
    if n == 0:
        return 1
    else:
        print('else se llama ella misma')
        return n * facorial(n - 1)

numero = 3
result = facorial(numero)

print(f'El factorial de {numero} es {result}')


def suma_sin_recursiva(n):
    sumar = 0
    for it in range(1, n + 1):
        sumar += it
    return sumar

print(f'La suma es: {suma_sin_recursiva(4)}')

def suma_con_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + suma_con_recursiva(n - 1)

print(f'La suma es: {suma_con_recursiva(4)}')
"""
##########################################################################################

#Lambda
"""x = lambda a : a + 10

print(x(5))


f = lambda x : x**2 + 2*x + 3

print(f(3))
"""

#filtrar listas
"""id_empleados = [234,456,676,233,356,897,623,985,892]

pares = filter(lambda x : x%2 == 0, id_empleados)

print(list(pares))"""

def filtrado_par(*d_empleados):
    return filter(lambda x : x%2 == 0, id_empleados)

id_empleados = [234,456,676,233,356,897,623,985,892]
pares = filtrado_par(*id_empleados)
print(list(pares))












