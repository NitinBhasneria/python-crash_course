# If/ Else conditions are used to decide to do something based on something being true or false

x = 3
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values


# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y :
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is grater than {x}')

# Logical operators (and, or, not) - Used to combine conditional statements




# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5]

# in
if x in numbers:
    print(x in numbers)

# not in
if x not in numbers:
    print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)