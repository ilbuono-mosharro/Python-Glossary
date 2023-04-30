"""
abs()	Returns the absolute value of a number
all()	Returns True if all items in an iterable object are true
any()	Returns True if any item in an iterable object is true
ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()	Returns the binary version of a number
bool()	Returns the boolean value of the specified object
bytearray()	Returns an array of bytes
bytes()	Returns a bytes object
callable()	Returns True if the specified object is callable, otherwise False
chr()	Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()	Returns the specified source as an object, ready to be executed
complex()	Returns a complex number
delattr()	Deletes the specified attribute (property or method) from the specified object
dict()	Returns a dictionary (Array)
dir()	Returns a list of the specified object's properties and methods
divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()	Evaluates and executes an expression
exec()	Executes the specified code (or object)
filter()	Use a filter function to exclude items in an iterable object
float()	Returns a floating point number
format()	Formats a specified value
frozenset()	Returns a frozenset object
getattr()	Returns the value of the specified attribute (property or method)
globals()	Returns the current global symbol table as a dictionary
hasattr()	Returns True if the specified object has the specified attribute (property/method)
hash()	Returns the hash value of a specified object
help()	Executes the built-in help system
hex()	Converts a number into a hexadecimal value
id()	Returns the id of an object
input()	Allowing user input
int()	Returns an integer number
isinstance()	Returns True if a specified object is an instance of a specified object
issubclass()	Returns True if a specified class is a subclass of a specified object
iter()	Returns an iterator object
len()	Returns the length of an object
list()	Returns a list
locals()	Returns an updated dictionary of the current local symbol table
map()	Returns the specified iterator with the specified function applied to each item
max()	Returns the largest item in an iterable
memoryview()	Returns a memory view object
min()	Returns the smallest item in an iterable
next()	Returns the next item in an iterable
object()	Returns a new object
oct()	Converts a number into an octal
open()	Opens a file and returns a file object
ord()	Convert an integer representing the Unicode of the specified character
pow()	Returns the value of x to the power of y
print()	Prints to the standard output device
property()	Gets, sets, deletes a property
range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()	Returns a readable version of an object
reversed()	Returns a reversed iterator
round()	Rounds a numbers
set()	Returns a new set object
setattr()	Sets an attribute (property/method) of an object
slice()	Returns a slice object
sorted()	Returns a sorted list
staticmethod()	Converts a method into a static method
str()	Returns a string object
sum()	Sums the items of an iterator
super()	Returns an object that represents the parent class
tuple()	Returns a tuple
type()	Returns the type of an object
vars()	Returns the __dict__ property of an object
zip()	Returns an iterator, from two or more iterators
"""

abs_example = abs(-7.25)
print(abs_example) # Returns the absolute value of a number
all_example = [True, True, False] 
print(all(all_example)) # Returns True if all items in an iterable object are true
any_example = [True, False, False]
print(any(any_example)) # Returns True if any item in an iterable object is true
ascii_example = "Hèllo World"
print(ascii(ascii_example)) # Returns a readable version of an object. Replaces none-ascii characters with escape character
bin_example = 34
print(bin(bin_example)) # Returns the binary version of a number
bool_example = bool(0) # False # Empty is False
bool_example1 = bool(1) # True
print(bool_example) # Returns the boolean value of the specified object
print(bool_example1) # Returns the boolean value of the specified object
bytearray_example = bytearray(5)
print(bytearray_example) # Returns an array of bytes
bytes_example = bytes(5)
print(bytes_example) # Returns a bytes object
def callable_example():
    pass
print(callable(callable_example)) # Returns True if the specified object is callable, otherwise False
print(callable(bytes_example)) # Returns True if the specified object is callable, otherwise False
chr_example = 97
print(chr(chr_example)) # Returns a character from the specified Unicode code
code = """
def my_function(x, y):
    return x + y

result = my_function(3, 4)
print(result)
"""

compiled_code = compile(code, "<string>", "exec")
exec(compiled_code) # Returns the specified source as an object, ready to be executed
complex_example = complex(3, 5)
print(complex_example) # Returns a complex number
class Car:
    brand = "Mercedes"
    model = "E 220"

delattr(Car, "brand") # Deletes the specified attribute (property or method) from the specified object
getattr(Car, "model") # Returns the value of the specified attribute (property or method)
hasattr(Car, "model") # Returns True if the specified object has the specified attribute (property/method)
setattr(Car, "model", "C 220") # Sets an attribute (property/method) of an object
dict_example = dict(brand="Mercedes", model="E220")
print(dict_example) # Returns a dictionary (Array)
print(dir(Car)) # Returns a list of the specified object's properties and methods
divmod_example = divmod(5, 2)
print(divmod_example) # Returns the quotient and the remainder when argument1 is divided by argument2
enumerate_example = ("test0", "test1", "test2")
enum = enumerate(enumerate_example)
print(list(enum)) # Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval_example = 'print(2 + 2)'
eval(eval_example) # Evaluates and executes an expression
exec(code) # Executes the specified code (or object)
nums = [1, 5 , 8, 10]

def myfunction(num):
    return num > 5

results = filter(myfunction, nums)
print(list(results)) # Use a filter function to exclude items in an iterable object
result_map = map(myfunction, nums)
print(list(result_map)) # Returns the specified iterator with the specified function applied to each item
float_example = "3.15"
print(float(float_example)) # Returns a floating point number
format_example = format(0.5,"%")
"""
The format you want to format the value into.
Legal values:
'<' - Left aligns the result (within the available space)
'>' - Right aligns the result (within the available space)
'^' - Center aligns the result (within the available space)
'=' - Places the sign to the left most position
'+' - Use a plus sign to indicate if the result is positive or negative
'-' - Use a minus sign for negative values only
' ' - Use a leading space for positive numbers
',' - Use a comma as a thousand separator
'_' - Use a underscore as a thousand separator
'b' - Binary format
'c' - Converts the value into the corresponding unicode character
'd' - Decimal format
'e' - Scientific format, with a lower case e
'E' - Scientific format, with an upper case E
'f' - Fix point number format
'F' - Fix point number format, upper case
'g' - General format
'G' - General format (using a upper case E for scientific notations)
'o' - Octal format
'x' - Hex format, lower case
'X' - Hex format, upper case
'n' - Number format
'%' - Percentage format
"""
print(format_example) # Formats a specified value
globals_example = globals()
# print(globals_example) # Returns the current global symbol table as a dictionary
locals_example = locals()
# print(locals_example) # Returns an updated dictionary of the current local symbol table
hash_example = hash("Hello World")
print(hash_example) # Returns the hash value of a specified object
# help_example = help()
# print(help_example)
hex_example = hex(255)
print(hex_example) # Converts a number into a hexadecimal value
print(id(hex_example)) # Returns the id of an object
# input_example = input("Enter your usename: ")
# print(input_example) # Allowing user input
int_example = int(3.5)
print(int_example) # Returns an integer number
print(isinstance(5, int)) # Returns True if a specified object is an instance of a specified object
print(isinstance("Hello", str)) # Returns True if a specified object is an instance of a specified object
class Test(Car):
    issub_class = True

    def __init__(self) -> None:
        super().__init__() # Returns an object that represents the parent class
print(issubclass(Test, Car)) # Returns True if a specified class is a subclass of a specified object
print(vars(Test)) # Returns the __dict__ property of an object
iter_example = iter([1, 2, 3, 4]) # Returns an iterator object
print(next(iter_example)) #  Returns the next item in an iterable
print(next(iter_example)) # Returns the next item in an iterable
print(len(nums)) # Returns the length of an object
list_test = list((1, 2, 3))
print(list_test)
max_example = max(list_test)
print(max_example) # Returns the largest item in an iterable
min_example = min(list_test)
print(min_example) # Returns the smallest item in an iterable
memoryview_example = memoryview(b"Hello")
print(memoryview_example) # Returns a memory view object
object_example = object() # Returns a new object
print(dir(object_example))
oct_example = oct(12)
print(oct) # Converts a number into an octal
f = open("test.txt") # Opens a file and returns a file object
print(f.read()) 
print(ord("a")) # Convert an integer representing the Unicode of the specified character
print(pow(3, 4)) # Returns the value of x to the power of y
print("Hello from print") # Prints to the standard output device
print(list(range(6))) # Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
print(list(reversed(list_test))) # Returns a reversed iterator
print(round(3,5569)) # Rounds a numbers
print(set((1, 2, 3, 3))) # Returns a new set object
slice_example = slice(2) # Returns a slice object
print(list_test[slice_example])
print(sorted(list_test, reverse=True)) # Returns a slice object
print(str(3.05)) # Returns a string object
print(sum(list_test)) # Sums the items of an iterator
print(tuple((1,2,3))) # Returns a tuple
print(type(3)) # Returns the type of an object
print(list(zip(list_test, nums))) # Returns an iterator, from two or more iterators

