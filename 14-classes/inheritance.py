"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""

#Parent Class
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"
    
p1 = Person("Marinario", "Mustafa")
print(p1.get_full_name())

# Child Class

class Student(Person):
    def __init__(self, firstname, lastname, age):
        # Python also has a super() function that will make the child class inherit all the methods and properties from its parent
        super().__init__(firstname, lastname)
        self.age = age

    def get_student_data(self):
        return f"{self.get_full_name()} {self.age}"
    
p2 = Student("Marinario", "Mustafa", 31)
print(p2.get_full_name())
print(p2.get_student_data())