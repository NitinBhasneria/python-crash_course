# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create a dict
person = {
    'first': 'Nitin',
    'last' : 'Bhasneria',
    'age'  : 20
}

# Use constructor
#person2 = dict(first_name = 'Nitin', last_name = 'Bhasneria')

# Get value
print(person['first'])
print(person.get('last'))


# Add key/value
person['phone'] = '888-888-888'

# Get dict keys
print(person.keys())

# Get items
print(person.items())

# Copy a dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove an item
del(person['age'])
person.pop('phone')

# Clear
person.clear()        # will get an empty dict

# Get length
print(len(person2))

# List of dict
peoples = [
    {'name' : 'Martha', 'age' : 30},
    {'name' : 'Kevin', 'age' : 25},
]

print(peoples[0]['name'])