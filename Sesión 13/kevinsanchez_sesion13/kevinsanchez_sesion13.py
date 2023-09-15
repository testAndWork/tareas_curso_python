"""class MyClass:
    x = 5
    y = 10.1
    z = 'Hola, estoy dentro de una clase'

objeto1 = MyClass()

print(objeto1.x)
print(objeto1.y)
print(objeto1.z)
##############################################################
class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age

x = Persona('Jonh', 23)
y = Persona('Maria', 18)
z = Persona('Karen', 26)

person1 = Persona('Jonh', 23)

print(person1.name, person1.age)
"""
##############################################################

"""#Funcion __str()__
class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} has {self.age} years old'

person1 = Persona('Jonh', 23)

print(person1)
"""
##############################################################
# Nota: El parametro self es una referencia a la instancia actual de la clase
# y se utiliza para acceder a las variables que pertenecen a las clases
"""class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} has {self.age} years old'
    def myfunc(self):
        print(f'Hello, names is: {self.name}')

persona1 = Persona('Jonh', 23)

print(persona1.myfunc())"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.skill = []
    def __str__(self):
        return f'Nombre: {self.name}, Edad: {self.age} years old'
    def add_skills(self,skill):
        self.skill.append(skill)

#Crear una instancia de la clase persona
persona1 = Person('Jonh Doe', 30)

#Agregar habilidades a la instancia
persona1.add_skills('python')
lista1 = ['SQL', 'Java', 'JavaScript', 'Tomar cafe a toda hora']
for skill1 in lista1:
    persona1.add_skills(skill1)

print(persona1)
print(f'Habilidades {persona1.skill}')

# Modificar edad
print(persona1)
persona1.age = 23

print(persona1)

print(persona1)
persona1.name = 'Jonh Snow'

print(persona1)

# Eliminar
del persona1.age

print(persona1)
"""
##############################################################
"""class Person:
    pass"""
##############################################################

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year  = year

carro1 = Car('toyota','corrola','2023')

print(f'descripcion del carro: {carro1.brand}, {carro1.model}, {carro1.year}')


