cadena = "Python"

subcadena = cadena[2:5]

print(subcadena)



cadena = "Python es genial" 
parte = cadena[7:9]
print(parte)

print(cadena.replace("bien", "muy"))


a,b = 5,3

c=a+b #suma 
print(c)
c=a-b
print(c)
c=b-a #resta
print(c)
c=a*b #multiplicacion
print(c)

c=a/b
print(c)

c=a//b
print(c)


#ejercicio1
precio = float(input('Digite el precio:'))
PorcentajeDescuento = float(input('digite el descuento: '))

descuento = precio*(PorcentajeDescuento/100)
precioFinal = precio-descuento

print('El precio final despues del descuento es:',precioFinal)

#Ejercicio2
PesoKilogramos = float(input('Dijite Su peso:'))
AlturaMetros = float(input('Escriba su altura:'))

Imc = PesoKilogramos / (AlturaMetros**2)

print('Su IMC es de: ',Imc)

#Ejercico3
MontoComida = float(input('Ingrese el monto de la comida: '))
Propina = float(input('Ingrese porcentaje de la popina: '))

TotalPagar = MontoComida + Propina 

print('EL total a pagar es: ',TotalPagar)


#Aplicando conocimientos 

a = 10
b = 15
c = 8

resultado1 = a + (b *c)
resultado2 = (a+b)*c
resultado3 = (a/b)*c
resultado4 = a/(b*c)
resultado5 = (a**b)+c
resultado6 = a**(b+c)

print(f'El resultado 1 es :{resultado1} \nEl resultado 2 es :{resultado2} \nEl resultado 3 es :{resultado3} \nEl resultado 4 es :{resultado4} \nEl resultado 5 es :{resultado5} \nEl resultado 6 es :{resultado6}')