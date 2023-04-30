# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def speed(self):
        return f"{self.brand} 250 km"

class Motor:
    def __init__(self, brand):
        self.brand = brand

    def speed(self):
        return f"{self.brand} 150 km"

c = Car("Mercedes")
m = Motor("Suzuki")

for vehicle in (c, m):
    print(vehicle.speed())

# Inheritance Class Polymorphism

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    
    def speed(self):
        return f"{self.brand} 240 km"

class Moto(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def speed(self):
        return f"{self.brand} 150 km"

c = Car("Mercedes")
m = Motor("Suzuki")

for vehicle in (c, m):
    print(vehicle.speed())
    


    
