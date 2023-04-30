"""
What is a Module?
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
"""

#The built-in function dir() is used to find out which names a module defines
import fibo
print(dir(fibo))

# how to import module
# from fibo import *
# from fibo import fib, fib2
# from fibo import fib as fib1 # Re-naming a Module

print(fibo.fib(10))
print(fibo.fib2(10))
