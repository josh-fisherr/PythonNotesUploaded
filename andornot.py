'''
and	If both statements are true, returns True	x > 2 and y > 1
or	If one of the statements are true, returns True	x > 3 or y > 5
not	If used, returns the reverse of the actual result	not(x > 10 and y > 5)
'''

x = 4
y = 3
 
x > 2 and y > 1      # returns True
x > 5 or y <= 3      # returns True
not(x > 2 and y > 1) # returns False
