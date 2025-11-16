# In Python, tuples are defined with parentheses () with comma-separated values. 
# Just like lists, tuples are sequences and can hold objects of different data types.

# Why use tuples instead of lists
# Tuples are one of the built-in data structures in Python. 
# Just like lists, tuples can hold a sequence of items and have a few key advantages:
# Tuples are more memory efficient than lists
# Tuples have a slightly higher time efficiency than lists
# Disadvantage is that they are immutable

my_tuple = ('abc', 123, 'def', 456)

# Built in Functions:

# The length of a tuple can be measured using the built-in function len().
# It takes the tuple as an argument to count the items in the tuple.
my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')
print(len(my_tuple)) # prints 6

# The built-in function max() returns the tuple’s maximum value. Note that this function requires 
# all of the values to be of the same data type. If used with numerical values, the function returns the maximum value. 
# If used with string values, the function returns the value at the tuple’s maximum index as if it was sorted alphabetically.
# The string closer to the letter “Z” in the alphabet would have a higher index.
my_tuple = (65, 2, 88, 101, 25)
max(my_tuple) # returns 101
 
my_tuple = ('orange', 'blue', 'red', 'green')
max(my_tuple) # returns "red"
 
my_tuple = ('abc', 234, 567, 'def')
max(my_tuple) # throws an error!

# The built-in function min() returns the tuple’s minimum value. Similar to the max() function, 
# the min() function requires all of the values to be of the same data type. If used with numerical values, 
# the function returns the minimum value. If used with string values, the function returns the value at the 
# tuple’s minimum index as if it was sorted alphabetically.
# The string closer to the letter “A” in the alphabet would have a lower index.
my_tuple = (65, 2, 88, 101, 25)
min(my_tuple) # returns 2

my_tuple = ('orange', 'blue', 'red', 'green')
min(my_tuple) # returns "blue"

my_tuple = ('abc', 234, 567, 'def')
min(my_tuple) # throws an error!

# The built-in method `.index()’ takes in a value as the argument to find its index in the tuple.
my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc') # returns 0
my_tuple.index(567) # returns 2

# The built-in method `.count()’ takes in a value as the argument to find the number of occurrences in the tuple.
my_tuple = ('abc', 'abc', 2, 3, 4)
my_tuple.count('abc') # returns 2
my_tuple.count(3) # returns 1
