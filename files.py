# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myFile.txt', 'w')  # w for mode writing

# Get some info
print('Name: ', myFile.name)
print('IsClosed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# wrie to the file
myFile.write('I hate python')
myFile.write(' and JS')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write(', but I love C++')
myFile.close()

# Read from the file
myFile = open('myFile.txt', 'r+')
rext = myFile.read(100)      # 100 characters
print(rext)