# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample json
userJSON = '{"firstName:" : "John", "lastName":"bhasneria"}'

# Parse to dict
user = json.loads(userJSON)        # gives in py format

print(user['firstName:'])
print(user)

car = {'nake': 'Ford', 'Model':'Mustang', 'year': 1971}

carJSON = json.dumps(car)   # gives in json format

print(carJSON)    