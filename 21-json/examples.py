# Convert from json to python
# If you have a JSON string, you can parse it by using the json.loads() method
import json
# some JSON:
cars_json = '{"brand": "Mercedes", "model": "E 220", "year": 2022}'


# parse cars:
cars_dict = json.loads(cars_json)

# the result is a Python dictionary
print(cars_dict)
print(cars_dict["brand"])

# Convert from python to json
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


cars_dictionary = {"brand": "Mercedes", "model": "E 220", "year": 2022}

# convert into JSON:
cars_json_from_dict = json.dumps(cars_dictionary)

print(cars_json_from_dict)