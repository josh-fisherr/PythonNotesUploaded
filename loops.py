# For loops
'''
In the example below, the for loop is iterating over the list nums. For each item in num, 
it is printing the output of num + 1.
'''
nums = [1, 2, 3, 4, 5]
 
for num in nums:
  print(num + 1)

# For loops with range
'''
The range() function can be used with the for loop to execute a block of code multiple times. 
The code below iterates between numbers 0 to 2 and prints each number.
'''
for i in range(3):
  print(i)

# Nested loops
'''
A for loop can have nested for loops. This is particularly useful if the items you are iterating over contain subitems. 
In the example below, 
we have a list of lists called teams and we can use a nested for loop to print each name in the lists.
'''
teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
  for name in team:
    print(name)

# While loops
'''
The while loop is used to execute code while its condition evaluates to be True. 
In the example below, the while loop will run and print i as long as the value of i is less than 6.
'''
i = 1
while i < 6:
  print(i)
  i += 1
