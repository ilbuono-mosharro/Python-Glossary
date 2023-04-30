#Text Type:	str

variable_double = "Hello World"
print(variable_double)
print(type(variable_double)) #Will print "str"

variable_single = 'Hello World'
print(variable_single)
print(type(variable_single)) #Will print "str"

variable_multiple_line_double = """
Marinario
Mustafa
31
"""
print(variable_multiple_line_double)
print(type(variable_multiple_line_double)) #Will print "str"

variable_multiple_line_single = '''
Marinario
Mustafa
31
'''
print(variable_multiple_line_single)
print(type(variable_multiple_line_single)) #Will print "str"