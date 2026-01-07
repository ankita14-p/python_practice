#list comprehension is a consice way of creating a list using a single line of code
#syntax: [expression for item in iterable if condition]
cubes=[x**3 for x in range(1,11)]
print(cubes)  #prints cubes of numbers from 1 to 10

#In python, list doesn't store actual values instead it stores references to objects in memory meaning that list elements are present in multiple locations in the memory and list only take references to that locations