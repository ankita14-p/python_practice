a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)

#list using list constructor
d=list((10,20,80))
print(d)

#creating list with multple repeated elements
e=[8]*5
print(e)

#Accssing list elements
print(a[0]) # First element
print(a[-1]) #last eleent
print(b[1:3]) # Slicing (from index 1 to 2)

#Adding elements in a list
a.append(6) #append a single element at the end of the list
print(a)
b.extend(["mango","orange"]) #adds multiple elements at the end of the list
print(b)
c.insert(2,"world") #insert element at a specific position
print(c)
 #clear() --> clears the entire list
 #since lists are mutable we can update elements of lists unlike strings
a[0] = 10
print(a)

#Removing elemnts from list
a.remove(3) #remove specific element by value
print(a)
popped_element = b.pop() #remove and return last element
print(popped_element)
print(b)
del c[1] #remove element at specific index
print(c)