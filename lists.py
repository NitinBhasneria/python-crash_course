# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1, 2, 3, 4, 5, 6]
fruits = ['Apples', 'Oranges', 'Grapes']

# Use a constructor
# number2 = list((1, 2, 3, 4, 5, 6))

# print(numbers, number2)

# Get a value
print(fruits[1])

# Get length
print (len(fruits))

# Append
fruits.append('Mangos')

# Change values
fruits[0] = 'Pears'

# Remove
fruits.remove('Grapes')

# Insert into positions
fruits.insert(2, 'Stawberries')

# Remove by position
fruits.pop(2)

#Reserve list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)
print(fruits)
