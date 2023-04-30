"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

"""

a = 1
b = 2
c = 2
d = 4

if b == c:
    print("true")
if a != b: 
    print("true")
if b > a:
    print("true")
if b >= a:
    print("true")
if a < b:
    print("true")
if b <= a:
    print("true")

if d > c:
    print("true")
else:
    print("false")

if c < a: 
    print("false")
elif b == c:
    print("true")
else:
    print("finish")

if b == c or d < a:
    print("true")

if b == c and d > a:
    print("true")

if b == c and d < a or c > a:
    print("true")