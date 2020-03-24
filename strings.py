# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Nitin'
age = 20

# Concetenate
# print ('Hello, my name is '+ name + 'and my age is ' + str(age))

# String Formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format(name = name, age = age))

# F-strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello, world'

#capitalize string
print(s.capitalize())   # capatialize the first variables

# Make all uppercase
print(s.upper())

# make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# start with
print(s.startswith('hello'))

# End With
print(s.endswith('world'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalpha())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
