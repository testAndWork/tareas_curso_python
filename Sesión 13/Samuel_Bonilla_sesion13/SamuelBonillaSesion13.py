#Crear una clase
class myclass:
    x = 5
    y = 10.1
    z = 'Hola, estoy dentro de la U'
    
#Crear objecto
objecto_1 = myclass()

print(objecto_1.z)

#Funcion Init
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
x = Person('John', 23)
y = Person('Maria', 36)

person_1 = Person('John', 23)
print(person_1.name, person_1.age)

#cambiando self por p

class Person:
    def __init__(p, name, age):
        p.name = name
        p.age = age
        
x = Person('John', 36)
y = Person('Maria', 36)

person_1 = Person('John', 36)
print(person_1.name, person_1.age)

#funcion str
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return print(f'{self.name}has{self.age}')
    
#Metodos de objeto

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []
    
    def __str__(self):
        return print(f'Nombre: {self.name}, Edad: {self.age}')
    
    def add_skills(self, skill):
        self.skills.append(skill)
        
#Crear una instancia de la clase persona
person_1 = Person('John Doe', 34)

#Agregar habilidades de la instancia
person_1.add_skills('Python')
lista =['SQL', 'Java', 'JavaScript', 'Tomar cafe']

for skill in lista:
    person_1.add_skills(skill)
    
#person_1.add_skills('Python')
#person_1.add_skills('Python')

#Obtener informacion de la persona
print(person_1)
print('Habilidades: ', person_1.skills)

#Modificar propiedades

person_1.age = 25

print(person_1)

person_1.name = 'Jon Snow'
print(person_1)

#Eliminar propiedades de objetos

del person_1.age

print(person_1)

#Ejemplo 1:

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
#Instanciando la clase 'Car' y creando un objeto de este tipo

carro = Car('toyota', 'corrola', '2023')

print(f'Descripcion del Carro: {carro.brand}, {carro.model}, {carro.year} ')

#Ejemplo 2:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
        
    def __str__(self):
        return f'{self.name},{self.age}'
    
    def add_grade(self,grade):
        self.grades.append(grade)
        
    def print_info(self):
        print(f'Estudiantes: {self.name}, Edad: {self.age}, Calificaciones {self.print_info}')
        
estudiante = Student('Luigi', 23)

estudiante.add_grade(10)
estudiante.add_grade(8)
estudiante.add_grade(9)
estudiante.add_grade(8)
print(estudiante)
print(estudiante.print_info)

#Ejercicio 3:

import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_perimeter(self):
        return 2*math.pi*self.radius
    
circulo = Circle
print(f'El perimetro es: {circulo.calculate_perimeter()} ')
print(f'El area es: {circulo.calculate_perimeter(): .2f} ')

#Ejercicio 4

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def get_info(self):
        print(f'El titulo es: {tittle},El autor es: {author},El año de publicacion es: {year}')
        
#Instanciar 
librito = Book('Que frio hace', 'yo', '2023')

print(librito.get_info())


#ejercicios 

#Ejercicio 1:

class Bank:
    def __init__(self, accounts):
        self.accounts = {}
        
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
        else:
            self.accounts[account_number] = amount
    
    def withdraw(self, account_number, amount ):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] >= amount
            else:
                print('Fondos insuficientes')
        else:
            print('Cuenta invalida o no encontrada')
    
    def get_balance(self, account_number):
        return self.accounts.get(account_number,0)
    
banco = Bank()

banco.get_balance('C1234')

banco.deposit('C007', 200)
banco.get_balance('C007')

banco.withdraw('C007', 5000)

banco.get_balance('C007')

banco.deposit('C006', 500)
banco.get_balance('C006')

#Ejercicio 2
class OnlineStore:
    def __init__(self):
        self.inventory = {}
        self.total_sales = 0
        
    def add_products(self, product_name, price):
        pass
    
    def purchase(self, product_name):
        pass
    
    def show_sales(self):
        pass