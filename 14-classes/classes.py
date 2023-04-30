"""
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
"""

class Student:
    name = "Marinario"


c1 = Student()
print(c1.name)

# the built-in __init__() function
# The __init__() function is called automatically every time the class is being used to create a new object.
# he self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

class Student:
    def __init__(self, name):
        self.name = name
    
c2 = Student("Marinario")
print(c2.name)

"""
The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.
"""
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

c3 = Student("Marinario")
print(c3)

"""
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mymethod(self):
        return f"Hello from the Student class {self.age} {self.name}"

c4 = Student("Marinario", 18)
print(c4.mymethod())   
# Modify Object Properties
c4.age = 15
print(c4.mymethod()) 
# Delete Object Properties
del c4.age
# Delete Object
del c4

# property, getter and setter
class Person:
    def __init__(self, name, age):
        self._name = name # private variable
        self._age = age # private variable

    @property
    def name(self):
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting name...")
        self._name = value

    @property
    def age(self):
        print("Getting age...")
        return self._age

    @age.setter
    def age(self, value):
        print("Setting age...")
        self._age = value

#staticmethod
class MyClass:
    @staticmethod
    def my_static_method(x, y):
        return x + y

# Static method call without creating an instance of the class
result = MyClass.my_static_method(2, 3)
print(result)  # Output: 5

# classmethod
class Person:
    def __init__(self, age):
        self.age = age
    
    @staticmethod
    def calculate_age(birth_year):
        return 2023 - birth_year
    
    @classmethod
    def from_birth_year(cls, birth_year):
        """
        this decorator is used to define a class method inside the class.
        Class methods take the class itself as the first parameter instead of the object instance
        """
        age = cls.calculate_age(birth_year)
        return cls(age)

person = Person.from_birth_year(1991)
print(f"{person.age} years old")
