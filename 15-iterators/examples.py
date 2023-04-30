"""
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator
"""

mylist = ["apple", "cherry", "banana"]

myiter = iter(mylist)

print(next(myiter))
print(next(myiter))
print(next(myiter))

class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a < 6:
            x = self.a
            self.a += 1
            return x
        else:
            StopIteration

a = Numbers()
b = iter(a)
print(next(b))
print(next(b))
print(next(b))