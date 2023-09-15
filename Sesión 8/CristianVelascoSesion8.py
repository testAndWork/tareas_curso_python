def saludar (nombre):
    print(f'Hola muy buenos dias {nombre}!!!')
saludar('juan')     

def sumar (x,y):
    suma=x+y
    return suma
resultado = sumar(4,5)
print('la suma es : ', resultado)

def area_rectangulo (base, altura):
    return base*altura
area = area_rectangulo(4,5)
print('El area del rectangulo es: ', area)

def imprimir_lista(lista):
    for it in lista:
        print(it)

lst = [1,2, 'hola']
print(lst)

def es_par (numero):
    if numero % 2 == 0:
        return True
    else:
        return False
num = 5 
if es_par(num):
    print('el numero es par')
else:
    print('el numero es impar')

def lista_pares(n):
    lstPares = []
    for it in range (n + 1):
        if it % 2 == 0:
            lstPares.append(it)
    return lstPares
print(lista_pares(20))

def my_funcion(nombre1,nombre2,nombre3,nombre4='Lopez'):
    print(nombre1+' '+ nombre2+ ' '+nombre3+' '+nombre4)

my_funcion(nombre1='Juan',nombre2='Jose',nombre3='Henry')