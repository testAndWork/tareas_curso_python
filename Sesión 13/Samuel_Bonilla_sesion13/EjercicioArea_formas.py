import math

class Shape:
    def calcular_area(self):
        pass
    
class Cuadrado(Shape):
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return self.lado *self.lado
    
    def calcular_perimetro(self):
        return self.lado + self.lado + self.lado + self.lado
    
class Rectangulo(Shape):
    def __init__(self, base, altura, longitud, ancho):
        self.base = base
        self.altura = altura
        self.longitud = longitud
        self.ancho = ancho
        
    def calcular_area(self):
        return self.base *self.altura
    
    def calcular_perimetro(self):
        return self.longitud*2 + self.ancho*2 

class Circulo(Shape):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi*self.radio**2
    
    def calcular_perimetro(self):
        return 2*math.pi*self.radio
    
    
cuadrado = Cuadrado(4)
print(f"El area de un cuadrado es: {cuadrado.calcular_area()}")
print(f"El perimetro de un cuadrado es: {cuadrado.calcular_perimetro()}")
print('\t')
rectangulo = Rectangulo(4,7,21,10)
print(f"El area de un rectangulo es: {rectangulo.calcular_area()}")
print(f"El perimetro de un rectangulo es: {rectangulo.calcular_perimetro()}")
print('\t')
circulo = Circulo(10)
print(f"El area de un circulo es: {circulo.calcular_area() : .2f}")
print(f"El perimetro de un circulo es: {circulo.calcular_perimetro() : .2f}")