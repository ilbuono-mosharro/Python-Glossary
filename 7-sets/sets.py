# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets cannot have two items with the same value.
# The values True and 1 are considered the same value in sets, and are treated as duplicates
# Once a set is created, you cannot change its items, but you can add or remove new items.
"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others

"""

myset = {"shoes", "jeans", "t-shirt", "blue"}
print(myset)
print(len(myset))
myset.add("new-item") # Add item intro current set
print(myset)
# To add items from another set into the current set
second_set = {"eur", "usd", "yen", "shoes"}

myset.update(second_set) # The update() method inserts the items in second_set into myset
print(myset)

myset.union(second_set) # The union() method returns a new set with all items from both sets
print(myset)

myset.intersection(second_set) # The intersection() method will return a new set, that only contains the items that are present in both sets
print(myset)

myset.isdisjoint(second_set) # Returns whether two sets have a intersection or not
print(myset)

myset.issubset(second_set) # Returns whether another set contains this set or not
print(myset)

myset.issuperset(second_set) #Returns whether this set contains another set or not
print(myset)

myset.intersection_update(second_set) # The intersection_update() method will keep only the items that are present in both sets
print(myset)

myset.difference(second_set) # Returns a set containing the difference between two or more sets
print(myset)

myset.symmetric_difference_update(second_set) # The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
print(myset)

myset.symmetric_difference(second_set) # The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets
print(myset)

myset.remove("blue") # If the item to remove does not exist, remove() will raise an error.
print(myset)

myset.discard("shoes") # If the item to remove does not exist, discard() will NOT raise an error.
print(myset)

myset.pop() # Remove a random item by using the pop() method:
print(myset)

myset.clear() # clear the set
print(myset)

# del myset  # delete the set