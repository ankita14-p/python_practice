#dict: stores value in key:value pairs
#values can be of any data type and can contain duplicates
#keys rae immutable and cannot be repeated
#keys are case sensitive
#dict are ordered as of python version 3.7

#Creating a dictionary
dict_1={
    "name":"Ankita",
    "age":22,
    "city":"Pune",
    "is_student":True,
    "hobbies":["reading","traveling","coding"], #list as value
    "education":{      #nested dictionary
        "undergraduate":"B.Tech",
        "postgraduate":"M.Tech"
    }

}
print(dict_1)

#Another way to create a dictionary
dict_2=dict(name="Rohan",age=25,city="Mumbai")
print(dict_2)

#Accesing dictionary items
print(dict_1["name"])  #using key
print(dict_1.get("age"))  #using get() method

#Adding and updating dictionary items
dict_1["profession"]="Engineer"  #adding new key-value pair
dict_1["age"]=23  #updating existing key-value pair
print(dict_1)

#removing dictionary items
#del removes an item by key
del dict_1["is_student"]
print(dict_1)

#pop() removes an item by key and returns its value
value=dict_2.pop("age")
print(value)
print(dict_2)

#popitem() removes the last inserted item
last_item=dict_1.popitem()
print(last_item)
print(dict_1)

#clear all items from the dictionary
dict_2.clear()
print(dict_2)

#Iterating through dictionary
d={1:"a",2:"b",3:"c"}

#Iterate through keys
for key in d:   #each key in new line
    print(key)

#Iterate through values
for value in d.values(): #each value in new line
    print(value)

#Iterate through key-value pairs
for key,value in d.items(): #each key-value pair in new line
    print(key,value)
