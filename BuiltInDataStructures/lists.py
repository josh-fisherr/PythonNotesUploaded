# A list can be created with brackets [] with items separated by commas ,.
# As noted above, a list can hold different data types, including strings, integers, float values and more.

# Built in Functions

# The length of a list can be measured using the built-in function len(). 
# It takes the list as an argument to count the items in the list.

lst1 = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst2 = [0, 1, 2, 3, 4]
lst3 = ['I love sushi so much!', 'I also love curry!']
 
print(len(lst1)) # prints 6
print(len(lst2)) # prints 5
print(len(lst3)) # prints 2

# The built-in method .append() takes an item as an argument to add the item to the end of a list.
lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.append(99) # appends 99 at the end of the list

# The built-in method .remove() removes an item that’s passed as the argument.
lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.remove(62) # removes 62 from the list

# The built-in method `.pop()’ takes an index and removes an item at that given index and returns that item. 
# If no index is provided, it takes the last item from the list.
lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.pop() # removes ['g', 'h', 'i']
lst.pop(0) # removes 'abc'


