#Python allows you to assign values to multiple variables in one line

name, last_name, age = "Marinario", "Mustafa", 31
print(name)
print(last_name)
print(age)

#Multiple values to one variable

name = first_name = nick_name = "Marinario"
print(name)
print(first_name)
print(nick_name)


# unpacking a collection

person = ['Marinario', 'Mustafa', 31]

name, last_name, age = person

print(name)
print(last_name)
print(age)