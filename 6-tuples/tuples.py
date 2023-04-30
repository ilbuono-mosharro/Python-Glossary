# A tuple is a collection which is ordered and unchangeable.
# One item tuple, remember the comma


mytuple = ("t-shirt", "shoes", "shoes", "jeans")
print(mytuple)
print(mytuple[0])

"""
since tuples are immutable, in order to add a new item or remove an item, 
you have to convert it into a list and then convert it back into a tuple.

"""
add_item = list(mytuple)
add_item.append("new-item")
new_mytuple = tuple(add_item)
print(new_mytuple)

# Add tuple to a tuple

two_tuple = mytuple + new_mytuple

print(two_tuple)

(tshirt, shoes, *rest) = two_tuple # Unpack tuple
print(tshirt) 
print(shoes)
print(rest)

print(two_tuple.count("shoes"))
print(two_tuple.index("shoes"))