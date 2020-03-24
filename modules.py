# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager
#  (including Django) as well as custom modules

import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
import validator
from validator import validate_email

# today = datetime.date.today()   // data object in date time
today = date.today()
#timestamp = time.time()
timestamp = time()

c = CamelCase()
print(c.hump('hello, there world'))

print(timestamp)

email = 'test@testgmail.com'
if validate_email(email):
    print('Email is valid')

# There are examples of core module that are available bu default with python and python
# has a package manager pip

# For install something with pip we have to do pip install