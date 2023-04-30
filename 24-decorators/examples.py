"""
a decorator is a special type of function that can be used to modify the behavior of another function or class.
A decorator takes a function or class as its argument and returns a new function or class with some additional functionality.
"""

def add_welcome_message(func):
    def wrapper(*args, **kwargs):
        print("Welcome!")
        return func(*args, **kwargs)
    return wrapper

@add_welcome_message
def say_hello(name):
    print("Hello, " + name)

say_hello("Marinario")


def login_required(auth):
    def authenticated(func):
        def wrapper(*args, **kwargs):
            if auth == True:
                print("Welcome")
            else:
                print("You need to login")
            return func(*args, **kwargs)
        return wrapper
    return authenticated

@login_required(True)
def dashboard():
    print("Your are authenticated")

@login_required(False)
def dashboard_f():
    return "test"

dashboard()
dashboard_f()