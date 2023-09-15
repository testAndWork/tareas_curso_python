class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname (self):
        print(self.fname, self.lname)

persona_1 = Person('Jhon','Snow')
persona_1.printname()

#class Studen(Person):
#    pass

#studen_1 = Studen('Albert', 'Einstein')
#studen_1.printname()

#class Studen(Person):
#    def __init__(self, fname, lname):
#        Person.__init__(self , fname, lname)

class Studen(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print('Bienvenido',self.fname, self.lname, 'a la clase del', self.graduationyear)

studen_1 = Studen('Mike','Tyson',2009)
studen_1.welcome()

class Animal:
    def __init__(self, name, nfeet, raza):
        self.name = name
        self.nfeet = nfeet
        self.raza = raza
class Gato(Animal):
    def __init__(self, name, nfeet, raza):
        super().__init__(name, nfeet, raza)

gatito = Gato('minino',4,'angora')
print('El nombre del gato es:',gatito.name)
print('El numero de pata es:',gatito.nfeet)
print('La raza del gato es:',gatito.raza)

class Dog(Animal):
    def __init__(self, name, nfeet, raza):
        super().__init__(name, nfeet, raza)
perrito = Dog('Scot', 4, 'labrador')
print('El nombre del perito es:',perrito.name)
print('El numero de pata es:',perrito.nfeet)
print('La raza del perrito es:',perrito.raza)

x = 'Hello, Word'
len(x)


mytuple = ('cat','dog','fish','horse')
len(mytuple)

mydyct = {
    'Nombre':'Jhon',
    'Apellido':'Doe'
}
len(mydyct)

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print('A conducir')
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print('A navegar')
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print('A volar')

carro_1 = Car('Tojota','gorrola') 
bote_1 = Boat('Bavaria','Yachts')
avion_1 = Plane('Boeing','AirBus')

for it in (carro_1, bote_1, avion_1):
    it.move()


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def move(self):
        print('A conducir')

class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print('A navegar')
class Plane(Vehicle):
    def move(self):
        print('A navegar')

carro_1 = Car('Tojota','gorrola',2009) 
bote_1 = Boat('Bavaria','Yachts',2020)
avion_1 = Plane('Boeing','AirBus',2023)

for it  in (carro_1, bote_1, avion_1):
    print(it.brand)
    print(it.model)
    it.move()

