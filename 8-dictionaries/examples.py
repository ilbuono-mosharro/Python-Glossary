"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""

my_dict = {
    "brand": "Mercedes",
    "model": "C 220",
    "year": 2014,
}

print(my_dict)
print(my_dict['brand']) # Get the value of the "model" key
print(my_dict.get("brand")) # Get the value of the "model" key
print(len(my_dict))
print(my_dict.keys()) #The keys() method will return a list of all the keys in the dictionary
print(my_dict.values()) # The values() method will return a list of all the values in the dictionary.
my_dict['model'] = "E 220" # Update dhe value of key model
print(my_dict)
my_dict.update({"model": "D 220"}) # Update dhe value of key model
print(my_dict)
my_dict['color'] = "Red" # Add a new item to the original dictionary
print(my_dict)
#loop through a dictionary
for item in my_dict.items():
    print(item)
for item in my_dict.keys():
    print(item)
for item in my_dict.values():
    print(item)
new_dict = my_dict.copy() # Copy a Dictionary
new_dict1 = dict(my_dict) # Copy a Dictionary
print(new_dict)
print(new_dict1)
print((my_dict.items())) # The items() method will return each item in a dictionary, as tuples in a list
print(my_dict.pop("model")) # The pop() method removes the item with the specified key name
print(my_dict.popitem()) # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
# del thisdict["model"] # Remove the item 
# del thisdict # Delete the dictionary completely
print(my_dict.clear()) # Clear the entire dictionary


nested_dict = {
    "car_1" : {
    "brand": "Mercedes",
    "model": "C 220",
    "year": 2014,
    },
    "car_2": {
    "brand": "Bmw",
    "model": "v2",
    "year": 2015,
    }
}

print(nested_dict["car_1"]["model"])

