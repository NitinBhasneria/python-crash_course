# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1      # no int and no semicolon
# y = 2.3         #float        
# name = 'Nitin'  #str
# is_cool = True  # capital T of F

# Multiple Assignment
x, y, name, is_cool = (1, 2.5, 'Nitin', True)

# Basic maths
a = x + y

print('Hello',x ,y ,name, is_cool)

# Casting 
x = str(x)
y = int(y)

# checking type
print(type(x), x)
print(type(y), y)
