#Set is used to store a collection of items 
#duplicates are not allowed
s={1,2,3,1}
print(s)
#Unordered. Cannot be accesed with indexes like in lists
#Efficient as compared to lists for search,insert and delete operations as it uses hashing internally
#can add or delete elemnts but cannot update elements
#s[1]=5    #Error 

#creating a set
s={10,20,30}
print(s)

#typecasting list to set
s=set([1,2,3])
print(s)

#adding element to the set
s.add(4)
print(s)

#Heterogeneous Set
s={1,"Ankita",False,True,67.9} #True doesn't appear as True evaluates to 1 and that means duplication
print(s)

#adding elements in set
set_1={1,2,3}
set_1.add(5)
print(set_1)

#adding elements using iterator
for i in range(4,9):
    set_1.add(i)
print(set_1)


people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union() function
population = people.union(vampires)

print("Union using union() function")
print(population)

# Union using "|" operator
population = people|dracula
print("\nUnion using '|' operator")
print(population)

set1 = set() # Cannot initialize set=() it gives error
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

# Intersection using intersection() function
set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)

# Intersection using "&" operator
set3 = set1 & set2
print("\nIntersection using '&' operator")
print(set3)

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

# Difference of two sets using difference() function
set3 = set1.difference(set2)
print(" Difference of two sets using difference() function")
print(set3)

# Difference of two sets using '-' operator
set3 = set1 - set2
print("\nDifference of two sets using '-' operator")
print(set3)