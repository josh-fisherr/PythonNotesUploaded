# In Python, dictionaries are defined with curly brackets {}.
# Dictionaries contain what’s called key-value pairs, which refer to pairs of a key and a value separated by a colon :. 
# The values can hold and be a mix of different data types, including lists or even nested dictionaries. 
# However, keys must be an immutable data type such as strings, numbers or tuples.

# The following dictionary has 4 key-value pairs. There are 4 key-value pairs separated by commas. 
# For example, the key 'fruits' has the value of the ['mangoes', 'bananas', 'kiwis']:
groceries = {'fruits': ['mangoes', 'bananas', 'kiwis'],
            'protein': ['beef', 'pork', 'salmon'],
            'carbs': ['rice', 'pasta', 'bread'],
            'veggies': ['lettuce', 'cabbage', 'onions']}

# Accessing and Writing Values
# In contrast to other data structures such as lists and tuples,
# there are no built-in ways to use indexing and slicing to access the values in a certain order in the dictionaries.
# A value within a dictionary can be accessed with its key.

party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}
 
party_planning['Location'] # returns 'Our Backyard'

# Likewise, values can be updated in the dictionary using its key:
party_planning['Location'] = 'At the park'
party_planning['Location'] # prints 'At the park'

#Similarly, a new key-value pair can be added to a dictionary:
party_planning['Dress Code'] = 'Casual'

# The length of a dictionary can be measured using the built-in function len().
# It takes the dictionary as an argument to count the number of key-value pairs in the dictionary.
party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}
 
len(party_planning) # returns 5

# The built-in method update() takes in a dictionary as an argument to update an existing dictionary.
# Any new key-value pairs will be added to the existing dictionary,
# but overlapping key-value pairs from the new dictionary will overwrite the key-value pairs in the existing dictionary.
shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}
 
shopping_list1.update(shopping_list2)
 
print(shopping_list1) # prints {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 350, 'shoes': 'sandals'}

# The built-in functions .keys() and .values() can be used to return the list of keys and values of a dictionary.
shopping_list = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
 
shopping_list.keys() # returns dict_keys(['jewelry', 'clothes', 'budget'])
shopping_list.values() # returns dict_values(['earrings', 'jeans', 200])