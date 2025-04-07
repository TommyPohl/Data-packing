import json


#raw_data = [1, 2, 3]
raw_data = {"name": "adam", "age": 33, "Grades": []}

with open("student.json", "w") as f:
    json.dump(raw_data, f)


with open("student.json", "r") as f:
    data = json.load(f)


print(data)