#crear una clase
class Myclass:
    x = 5
    y = 10.1
    z = ('hola, estoy dentro de una clase')

objeto_1 = Myclass()

print(objeto_1.x)
print(objeto_1.y)
print(objeto_1.z)

class Person:
    def __init__( self, name, age):
        self.name = name
        self.age = age
x = Person('jhon',23)
y = Person('maria',36)

Person_1 = Person('jhon',23)

print(Person_1.name ,Person_1.age )


class Person:
    def __init__( self, name, age):
        self.name = name
        self.age = age

person_1 = Person('jhon',36)

class Person:
    def __init__( self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} has {self.age} years old'

person_1 = Person('jhon',36)
print(person_1)


class Person:
    def __init__( self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} has {self.age} years old'
    
    def myfunc(self):
        print(f'¡hello!, my name is : {self.name}')

person_1 = Person('jhon',36)

print(person_1.myfunc())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    def __str__(self):
        return f'Nombre: {self.name} Edad: {self.age} '
    def add_skills(self, skill):
        self.skills.append(skill)

person_1 = Person('jhon doe',34)



person_1.add_skills('Python')
lista = ['SQL','JavaScript','Tomar cafe a toda hora']
#person_1.add_skills('SQL')
#person_1.add_skills('Python')
#person_1.add_skills('Python')

for skill in lista:
    person_1.add_skills(skill)

print(person_1)

print('Habilidades:', person_1.skills)

person_1.age = 25
print(person_1)

del person_1.age

print(person_1)

del person_1

class Person:
    pass

class Car:
    def __init__(self, brand, model, yeard):
        self.brand = brand
        self.model = model
        self.yeard = yeard

carro = Car('tollota','korrolla','2023')

print(f'Descripcion del Carro: {carro.brand}, {carro.model}, {carro.yeard}')


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def __str__(self):
        return f'{self.name}, {self.age}'
    
    def add_grades(self, grade):
        self.grades.append(grade)
    def print_info(self):
        print(f'Estudiante: {self.name}, Edad:{self.age}, Calificaciones:{self.grades}')

estudiante = Student('Luigi', 23)
print(estudiante)

estudiante.add_grades(10)
estudiante.add_grades(5)
estudiante.add_grades(7)
estudiante.add_grades(8)
estudiante.add_grades(9)

print(estudiante.print_info())

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius**2
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

circulo = Circle(3)
print(f'el Perimetro:{circulo.calculate_perimeter()}')
print(f'El area es: {circulo.calculate_area()}')

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        print(f'El titulo es:{self.title}, Autor es:{self.author}, año es:{self.year}')

librito = Book('Que frio hace', 'yo', '2023')

print(librito.get_info())


class Bank:
    def __init__(self ):
        self.accounts = {}

    def deposit(self, accounts_number, amount):
        if accounts_number in self.accounts:
            self.accounts[accounts_number] += amount
        else:
            self.accounts[accounts_number] = amount
    def withdraw(self, accounts_number, amount):
         if accounts_number in self.accounts:
            if self.accounts[accounts_number] >= amount:
                self.accounts[accounts_number] -= amount
            else:
         
                print('Fondos insufientes')
         else:
             print('cuenta invalida o no encotrada')       
    def get_balance(self, accounts_number):
        return self.accounts.get(accounts_number,0)

banco = Bank()
banco.get_balance('C1234')

banco.deposit('C007',200)
banco.get_balance('C007')
banco.withdraw('C007',5000)
banco.get_balance('C007')
banco.deposit('C006',500)
banco.get_balance('C006')

class OnlineStore:
    def __init__(self):
        self.inventory = {}
        
        self.total_sales = 0

    def add_product(self,product_name,price):
        if product_name in self.inventory:
            self.inventory[product_name] += price
        else:
            self.inventory[product_name] = price
    def purchase(self,product_name, price):
        if product_name in self.inventory:
            if self.inventory[product_name] <= price:
                self.inventory[product_name] -= price
                self.total_sales+=1

            else:
         
                print('Fondos insufientes')
        else:
             print('cuenta producto invalido o no encotrado')  

    def show_sales(self):
        print(self.total_sales())

only = OnlineStore()
only.add_product('celular',100)
only.purchase('celular',120)
only.show_sales()
