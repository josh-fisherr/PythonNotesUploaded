# in Python, strings are defined with single quotes '' or double quotes "" and can contain a combination of letters,
# numbers, symbols and spaces

intro = "My name is Jeff!"

# Slicdes first character
print(intro[0]) # prints M

# This would get the first 2 letters
intro[0:2]

# We can also use negative indices to print the letters from the back. This code would print the word 'Jeff'.
intro[-5:-1]

# The length of a string can be measured using the built-in function len(). 
# It takes the string as an argument to count the characters in the string. 
# Note that whitespaces count as a character.
intro1 = "My name is Jeff!"
intro2 = "Hello all!"
intro3 = "Hi there."
len(intro1) # evaluates 16
len(intro2) # evaluates 10
len(intro3) # evaluates 9

# str.lower(), str.upper(), str.title()
intro = "My name is Jeff!"
print(intro.lower()) # prints 'my name is jeff!' Lower case whole thing
print(intro.upper()) # prints 'MY NAME IS JEFF!' Capitalizes whole thing
print(intro.title()) # prints 'My Name Is Jeff!' Capitalizes first letter of each

# str.split() The built-in function .split() takes a string and splits the string into a list of strings.
# By default, the function splits by whitespace but the separator can be specified as an argument.
intro = "My name is Jeff!"
print(intro.split()) # prints ['My', 'name', 'is', 'Jeff!']
print(intro.split('name')) # prints ['My ', ' is Jeff!']
print(intro.split('!')) # prints ['My name is Jeff', '']

