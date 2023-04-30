"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""

sum_numbers = lambda a : a + 5

result = sum_numbers(5)
print(result)

sum_numbers = lambda a, b: a + b

result = sum_numbers(5, 5)
print(result)


def myfunction(n):
    return lambda a: a * n

results = myfunction(5)

print(results(5))
