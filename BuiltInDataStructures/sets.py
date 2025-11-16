# A set is an immutable, unordered collection of unique elements that can consist of integers, 
# floats, strings and tuples. However, sets cannot hold mutable elements such as lists, sets or dictionaries.
# In Python, a set is created with curly braces {} with items inside the braces separated by commas. See an example here:

set1 = {'Jenny', 26, 'Parker', 10.5}
print(set1) # prints {10.5, 26, 'Jenny', 'Parker'}

# The built-in function set() can be used with a list argument to create a set from that list.
# Note that this will drop any duplicate elements in the list, as sets can only contain unique, non-duplicated elements. 
# Here we can see lst being used with the set() function to create a set set2:
lst = ['Jenny', 26, 'Parker', 'Parker', 10.5]
set2 = set(lst)
print(set2) # prints {10.5, 26, 'Jenny', 'Parker'}

# Accessing and Writing Values
# Sets do not have indexes or keys. We can use in to check to see if the element exists in the set:
students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
print('Chau' in students) # returns True

# Because sets are immutable, existing elements within the sets cannot be changed. 
# However, new elements can be added using the built-in method add() which takes in an element to add to a set:
students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
 
students.add('George')
print('George' in students) # returns True

# The built-in method .update() takes in any iterable object, such as tuples, lists, dictionaries or sets, and adds the object
# to an existing set. Any duplicated elements will not be added.
students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
 
students1.update(students2)

# Similarly, the built-in method .union() takes an iterable object and joins the new object with the existing object:
students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
 
students3 = students1.union(students2)

# The built-in method .remove() takes in an element and removes it from the set. See an example below:
students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students.remove('Bridgette')

# Because sets are iterable, we can utilize a for loop to iterate through a set. 
count_down = set([9, 8, 7, 6, 5, 4, 3, 2, 1])
for num in count_down:
   print(num, 'seconds left!')


