#tuple is an immutable ordered collection of elements
#Can hold elements of different datatypes

#Creating a tuple
tup=()
print(tup)

#using string
tup=('Ank','is')
print(tup)

#using list
li=[1,2,3,4]
print(tuple(li))

#using built-in function
tup=tuple("ank") #only one object and that is string ---> 'a','n','k'
print(tup)

#Creating a tuple with mixed datatype
tup=(5,"ank",True,9.0)
print(tup)

#Creating tuple with nested tuples
tup1=(1,1)
tup2=("Ank","bar")
tup3=(tup1,tup2)
print(tup3)

#creating a tuple with repetition
tup=("Ank")*3
print(tup)

#Accessing ekements with indexing
tup1=(1,2,3)
print(tup1[0])

#Slicing
tup2=tuple("Ankita")
print(tup2[1:4])
print(tup2[:3])

