class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        print(self.fname, self.lname)
        
persona = Person('Jon', 'Snow')
persona.printname()

#CLASE SECUNDARIA
class Student(Person):
    pass

student_1 = Student('Albert', 'Einstein')
student_1.printname()

#Agregar funcion init

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
#Funcion super()

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#Agregar propiedades a la clase heredada:
        
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year        

student_1 = Student('Mike', 'Tyson', 2009)

#Agregar metodos

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year  
    
    def Welcome(self):
        print("Bienvenido", self.fname, self.lname, "a la clase del", self.graduationyear)
        
student_1 = Student('Mike', 'Tyson', 2009)
student_1.Welcome()

#Ejemplo 

class Animal:
    def __init__(self, name, nfeet, raza):
        self.name = name
        self.nfeet = nfeet
        self.raza = raza
        
class Cat(Animal):
    def __init__(self, name, nfeet, raza):
        super().__init__(name, nfeet, raza)
        
gatito = Cat('minimo', 4, 'Angora')
print('El nombre del gato es: ',gatito.name)
print('El numero de patas es: ',gatito.nfeet)
print('La raza del gato es: ',gatito.raza)

class Dog(Animal):
    def __init__(self, name, nfeet, raza):
        super().__init__(name, nfeet, raza)

perrito = Dog('Scoth', 4 , 'labrador')
print('El nombre del perro es: ',perrito.name)
print('El numero de patas es: ',perrito.nfeet)
print('La raza del perro es: ',perrito.raza)

#Poliformismo

x = "Hello World"

len(x)

mytuple = ('Cat', 'Dog', 'fish', 'horse')
len(mytuple)

mydyet = {
    'Nombre': 'John',
    'Apellido': 'Doe'
}
len(mydyet)

#poliformismo para clase

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print('A conducir')
        
    def nomove(self):
        print("No se movio")
    
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print('A navegar')
        
    def nomove(self):
        print("No se movio")
        
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print('A volar')
        
    def nomove(self):
        print("No se movio")
        
carro_1 = Car('Toyota', 'gorrola')
bote_1 = Boat('Bavaria', 'Yachte')
avion_1 = Plane('Boeing', 'Airbus')

for it in (carro_1, bote_1, avion_1):
    it.move()
    
for it in (carro_1, bote_1, avion_1):
    it.nomove()
    
#poliformismo de la clase herencia

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def moves(self):
        print('A conducir')
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def moves(self):
        print('A conducir')
        
class Plane(Vehicle):
    def moves(self):
        print('A conducir')

carro_1 = Car('Toyota', 'gorrola', 2009)
bote_1 = Boat('Bavaria', 'Yachte', 2001)
avion_1 = Plane('Boeing', 'Airbus', 2002)

for it in (carro_1, bote_1, avion_1):
    print(it.brand)
    print(it.model)
    it.moves()
    
#Ejemplo

class Figura:
    def calcular_area(self):
        pass
    
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return self.lado *self.lado
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base *self.altura
    
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura/2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi*self.radio**2
    
cuadrado = ma.Cuadrado(4)
print('EL area de un cuadrado es :', cuadrado.calcular_area())

rectangulo = ma.Rectangulo(5, 4)

print(f'El area de un Rectangulo es: {rectangulo.calcular_area() : .1f}')


triangulo = ma.Triangulo(5, 4)
print('El area de un triangulo es : ', triangulo.calcular_area())

circulo = ma.Circulo(4)

print(f'EL area del circulo es : {circulo.calcular_area(): .2f}')