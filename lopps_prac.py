#Print all numbers from 1 to 50.
for i in range(1,51):
    print(i)

#Print all even numbers from 1 to 50.
for i  in range(2,51,2):
    print(i)

#Calculate the sum of all numbers from 1 to n (where n is user input).
n=input("Enter a number: ")
print(sum(range(1,int(n)+1)))    #without int the n is a string and concatenation between string and 1 cannot happen

#Print the multiplication table of a given number.
num=int(input("Enter a number: "))
for i in range(1,13):
    print(f"{num} * {i} = {num*i}")

#Count how many numbers in a list are greater than 10.
#Example list: [3, 15, 7, 22, 9, 30]
list_1=[3, 15, 7, 22, 9, 30]
count=0
for i in list_1:
    if i>10:
        count+=1
print(f"Count of numbers greater than 10 is: {count}")

#Print each character of a string on a new line.
name="Ankita"
for i in name:
    print(i)
#Find the largest number in a list without using max().
list_2=[34, 67, 23, 89, 12, 90, 45]
largest=list_2[0]
for i in list_2:
    if i>largest:
        largest=i
print(f"The largest number in the list is: {largest}")
