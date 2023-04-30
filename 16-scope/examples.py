# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
    myvar = 1
    return myvar

print(myfunc())

# Function Inside Function
#the variable firstvar is not available outside the function, but it is available for any function inside the function

def onefunction():
    firstvar = 2
    def secondfunction():
        print(firstvar)
    secondfunction()

onefunction()

# Global Scope


var_global = 3


def myfunc():
    print(var_global)

myfunc()

# Naming Variables
"""
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, 
one available in the global scope (outside the function) and one available in the local scope (inside the function)
"""

glob_var = 4 

def myfunc():
    # If you need to create a global variable, but are stuck in the local scope, you can use the global keyword
    # global glob_var
    glob_var = 5
    print(glob_var)

myfunc()
print(glob_var)