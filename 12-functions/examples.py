def myfunction():
    print("Hello from a function")


myfunction() # To call a function, use the function name followed by parenthesis

"""
Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.
"""

def myfunction(firstname, lastname):
    print(f"{firstname} {lastname}")

myfunction("Marinario", "Mustafa")

"""
The terms parameter and argument can be used for the same thing: information that are passed into a function.
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""
#Arguments are often shortened to args in Python documentations.

def myfunction(*peoople): # *people is a tuple of arguments
    print(peoople)

myfunction("Marinario", "Lukas", "Maria")

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

def myfunction(**peoople): # **person is a dictionary
    print(peoople)

myfunction(name="Marinario", age=31)


#Passing a list as argument

fruits_list = ["cherry", "banana", "apple"]

def myfunction(fruits):
    for fruit in fruits:
        print(fruit)

myfunction(fruits_list)

# Return Values
def myfunction(number):
    return number * 5

print(myfunction(2))

"""
Recursion
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. 
It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, 
or one that uses excess amounts of memory or processor power. 
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
"""

def myfunction(number):
    if number > 0:
        results = number + myfunction(number - 1)
        print(f"Results: {results}")
    else:
        results = 0
    return results

myfunction(6)




