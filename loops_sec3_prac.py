#Print each item of a list along with its index.
fruits = ["apple", "banana", "cherry", "date"]
print(list(enumerate(fruits)))

#From a list of names, print the index of the name "Admin".
names = ["User1", "User2", "Admin", "User3"]
for index,name in enumerate(names):  #without enumerate it would be for name in names and idex,names won't run
    if name=="Admin":
        print(f"The index of 'Admin' is: {index}")

#Replace all values greater than 50 in a list with 0 using enumerate().
numbers = [10, 55, 23, 67, 45, 89, 12]
for index, value in enumerate(numbers):
    if value > 50:
        numbers[index] = 0

print(f"Modified list: {numbers}")

#Given a list of marks, print:
#index
#marks
#"Pass" if marks ≥ 40 else "Fail"

marks=[23, 67, 45, 89, 12, 38, 50]
for index,mark in enumerate(marks):
    if mark>40:
        result="Pass"
        print(f"Index: {index}, Marks: {mark}, Result: {result}")
    else:
        result="Fail"
        print(f"Index: {index}, Marks: {mark}, Result: {result}")

#Count how many times the value 0 appears in a list using enumerate().
numbers = [0, 5, 0, 3, 0, 7, 0, 2]
count = 0
for index, value in enumerate(numbers):
    if value == 0:
        count += 1
print(f"The value 0 appears {count} times in the list.")