#unpacking of tuples
tup=("Hello","World","Bye")
a,b,c=tup #stores the values of tuples that was present in different in dexes into separate variables
print(a)
print(b)
print(c)

#Tuple unpacking with asterick
tup=(1,2,3,4,5,6)
a, b, *c=tup
print(a)
print(b)
print(c)

#concatenation of tuples
tup1=(1,2,3)
tup2=("Ankita","hello")
tup3=tup1+tup2
print(tup3)

#Reversing the tuple
tup=tuple("Ankita")
print(tup[::-1])

#deleting a tuple
del tup
print(tup)  #ERROR--> 'tup' is not defined