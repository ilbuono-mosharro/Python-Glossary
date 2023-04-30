"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
Python has a built-in package called re, which can be used to work with Regular Expressions.
"""
"""
RegEx Functions
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
"""
"""
Metacharacters
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group
"""
"""
Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
"""
"""
Sets
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""

import re

#The findall() function returns a list containing all matches.

find_characters = "The rain in Albania"
#Find all lower case characters alphabetically between "a" and "m"
results = re.findall("[a-m]", find_characters)
print(results)

results0 = re.findall("a", find_characters)
print(results0)

find_digit = "Albania 1992"
#Check if the string contains any digits (numbers from 0-9)
results1 = re.findall("\d", find_digit)
print(results1)

find_sequence = "Hello Albania"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o"
results2 = re.findall("He..o", find_sequence)
print(results2)

start_with_albania = "Albania 1992"
#Check if the string starts with 'Albania'
results3 = re.findall("^Albania", start_with_albania)
print(results3)

end_with_albania = "Hello Albania"
#Check if the string ends with 'Albania'
results4 = re.findall("Albania$", end_with_albania)
print(results4)

text = "Hello Albania"
#Search for a sequence that starts with "Al", followed by 0 or more  (any) characters, and an "a":
results5 = re.findall("Al.*a", text)
print(results5)

text1 = "Hello Albania"
#Search for a sequence that starts with "Al", followed by 1 or more  (any) characters, and an "a":
results6 = re.findall("Al.+a", text1)
print(results6)

text2 = "Hello Albania"
#Search for a sequence that starts with "Al", followed by 0 or 1  (any) character, and an "a":
results7 = re.findall("Al.?a", text2)
print(results7)

text3 = "Hello Albania"
#Search for a sequence that starts with "Al", followed excactly 2 (any) characters, and an "a"
results8 = re.findall("Al.{4}a", text3)
print(results8)

text4 = "Albania travel 2023"
#Check if the string contains either "summer" or "travel"
results9 = re.findall("travel|summer", text4)
print(results9)
#Check if the string starts with "Al"
results10 = re.findall("\AAl", text4)
print(results10)
#Check if "travel" is present at the beginning of a WORD
results11 = re.findall(r"\btravel", text4)
print(results11)
#Check if "travel" is present, but NOT at the end of a word
results12 = re.findall(r"trav\B", text4)
print(results12)
#Return a match at every no-digit character
results13 = re.findall("\D", text4)
print(results13)
#Return a match at every white-space character
results14 = re.findall("\s", text4)
print(results14)
#Return a match at every NON white-space character
results15 = re.findall("\S", text4)
print(results15)
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character)
results16 = re.findall("\w", text4)
print(results16)
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.)
results17 = re.findall("\W", text4)
print(results17)
#Check if the string ends with "2023"
results18 = re.findall("2023\Z", text4)
print(results18)
#Check if the string has any a, l, or b characters
results19 = re.findall("[alb]", text4)
print(results19)
#Check if the string has other characters than a, l, or b
results20 = re.findall("[^alb]", text4)
print(results20)

text5 = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
results21 = re.findall("[0-5][0-9]", text5)
print(results21)
#Check if the string has any characters from a to z lower case, and A to Z upper case
results22 = re.findall("[a-zA-Z]", text4)
print(results22)

"""
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned
"""
text6 = "Albania travel, summer in Albania"
results23 = re.search("Albania", text6)
print(results23)

#The split() function returns a list where the string has been split at each match
results24 = re.split("\s", text6)
print(results24)
#Split the string at the second white-space character
results25 = re.split("\s", text6, 2)
print(results25)
#The sub() function replaces the matches with the text of your choice
results26 = re.sub("\s", "#", text6)
print(results26)
