# To insert characters that are illegal in a string, use an escape character.

txt = 'It\'s alright.' # Single Quote
print(txt) 

txt = "This will insert one \\ (backslash)." # Backslash
print(txt) 

txt = "Hello\nWorld!" # New Line
print(txt) 

txt = "Hello\rWorld!" # Carriage Return	
print(txt) 

txt = "Hello\tWorld!" # Tab
print(txt) 

txt = "Hello \bWorld!" # Backspace
print(txt) 

txt = "\110\145\154\154\157" # Octal value
print(txt) 

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) # Hex value
