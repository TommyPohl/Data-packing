import json

# Zo stringu
numbers = [23, 34, 45, 34]

data = "adam"       #{"name": "Adam", "age": 34}

json_string = json.dumps(data)

print(json_string)

#json_string = '{"name": "Alice", "age": 25}'
data2 = json.loads(json_string)

print(data2)