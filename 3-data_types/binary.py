#Binary Types:	bytes, bytearray, memoryview

variable_bytes = b"Hello"	
print(variable_bytes)
print(type(variable_bytes)) #Will print "bytes"

variable_byte_array = bytearray(5)	
print(variable_byte_array)
print(type(variable_byte_array)) #Will print "bytearray"

variable_memory_view = memoryview(bytes(5))
print(variable_memory_view)	
print(type(variable_memory_view)) #Will print "memoryview"