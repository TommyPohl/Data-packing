import json


student = {"name": "adam", "age": 33, "grades": "1,2,3"}

with open("student.json", "w") as f:
    json.dump(student, f)


with open("student.json", "r") as f:
    data = json.load(f)


print(data)