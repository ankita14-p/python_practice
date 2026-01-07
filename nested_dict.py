employee={
    "employee1":{
        "name": "Alice",
        "age": 30,
    }
}
print(employee)

#Adding Elements to a nested dictionary
#Adding anew key_value pair to an existing inner dictionary
employee["employee1"]["department"]="IT"
print(employee)

#Adding a new inner dictionary
employee["employee2"]={
    "name":"Bob",
    "age":28,
    "department":"HR"
}
print(employee)

#Accessing elements in a nested dictionary
print(employee["employee1"]["name"])  #Accessing name of employee1
print(employee["employee2"]["name"])  #Accessing name of employee2

#deleting from nested array
del employee["employee1"]["age"]  #Deleting age of employee1
print(employee)

#Removing an entire inner dictionary
del employee["employee2"]  #Deleting employee2
print(employee)