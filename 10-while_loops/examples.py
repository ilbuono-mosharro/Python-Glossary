b = 0

while b < 10:
    b += 1
    if b == 11:
        break # With the break statement we can stop the loop even if the while condition is true
    if b == 6:
        continue # Continue to the next iteration if i is 3 
    print(b)
else:
    print("b is no longer less than 10")