# FOR STRING USE []
# FOR TUPLE  USE ()
# FOR SET    USE {}



# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Sinle value needs
fruits2 = ('Apples',)     # By ',' it became tuple from string

# print(fruits2, type(fruits2))

# Get value
print(fruits[1])

# Can't change value

# Delte tuples
del fruits2

# Get lengt
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {'Apples', 'Oranges', 'Mangos'}

# Check is in set
print('Apples' in fruits_set)

#Add to set
fruits_set.add('Grape')

# remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')       # will not give error but will not be added

# Clear set
fruits_set.clear()         # will gice a clear set


print(fruits_set)