m=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(m)
# Accessing elements in a nested list
print(m[0][1])  # Output: 2
print(m[2][0])  # Output: 7

#using row-by-row loop
for row in m:
    print(row) #each row as a list in new line

#using index based nested loops
for i in range(len(m)): #iterating through rows
    for j in range(len(m[i])): #iterating through columns
        print(m[i][j], end=' ') #printing each element in the row
    print() #new line after each row

#Methods in multidimensional lists
# Adding a new row
m.append([10, 11, 12])
print(m)

#extend a row by adding multiple elements
m[1].extend([13,14])
print(m)

#reverses the order of elements in a list
m[0].reverse()
print(m)
m.reverse()
print(m)

#write element
m[2][2] = 99
print(m)