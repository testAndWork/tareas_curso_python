import modulo_area as ma

cuadrado = ma.cuadrado(4)
print('El area de un cuadrado es', cuadrado.calcular_area())

rectangulo = ma.Rectangulo(5,4)
print('el area de un rectangulo es', rectangulo.calcular_area())

triangulo = ma.Triangulo(5,2)
print('el area de un triangulo es:', triangulo.calcular_area())

circulo = ma.Circulo(4)
print(f'el area de un circulo es: {circulo.calcular_area():.2f}')