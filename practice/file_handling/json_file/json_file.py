import json

student = {
    "name" : "Rahul",
    "age" : 17,
    "City" : "Jaipur"
}

with open("student.json", "w") as file:
    
    json.dump(student, file, indent = 4) # we can adjust data using the indent parameter of dump, intent is optional

json_std = json.dumps(student) # converts python dictionary to JSON string
print(json_std)
print(type(json_std))

with open("student.json", "r") as file:
    data = json.load(file) # loads data from file to the program
    print(data)

std = '{"name" : "Rahul", "age" : 17}'
upd_std = json.loads(std) # converts the JSON string to python dictionary
print(upd_std)
print(type(upd_std))