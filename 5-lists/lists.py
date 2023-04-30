"""
List Methods

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""

mylist = ["t-shirt", "jeans", "shoes", "shoes"] #Since lists are indexed, lists can have items with the same value
print(mylist)

print(len(mylist)) #List Length

print(mylist[0]) #The first item has index 0
print(mylist.index("t-shirt")) #Returns the index of the first element with the specified value

print(mylist[2:4]) #List of indexes

print(mylist.count("shoes")) #Returns the number of elements with the specified value

mylist.sort()
mylist.sort(reverse=True)
print(mylist) #Sorts the list

mylist.reverse() #Reverses the order of the list
print(mylist) #Reverse the order of the list

copy_list = mylist.copy()
print(copy_list) #Returns a copy of the list

second_list = ["eur", 'usd', 'pound']
new_list = second_list + mylist
print(new_list) #Join two list

mylist.extend(second_list)
print(mylist) #Extends mylist


#loop throught the list
for item in mylist:
    print(item)

print([item for item in mylist]) #List comprehension

mylist[2] = "nike"
print(mylist)

mylist.append("adidas")
print(mylist) #Add new item in the list

mylist.insert(0, "first Item") 
print(mylist) #Add new item by index

mylist.remove("t-shirt") 
print(mylist) #Remove t-shirt from the list

mylist.pop(0) #If you do not specify the index, the pop() method removes the last item
print(mylist) #Remove first item by index

del mylist[0] #Remove first item by index
# del mylist remove entire list
print(mylist)

mylist.clear() #clear the list content
print(mylist)







