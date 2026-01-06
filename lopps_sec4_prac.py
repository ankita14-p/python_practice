#Search for a number in a list.
#If found, print "Found"
#Else, print "Not Found"

numbers = [12, 45, 23, 67, 34, 89, 90]
search_num = int(input("Enter a number to search: "))
for index,value in enumerate(numbers):
    if value==search_num:
        print("Found")
        break
else:
    print("Not Found")

#Check whether a given number is prime using for-else.
num = int(input("Enter a number: "))
if num==1:
    print("1 is neither prime nor composite.")
else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")

#Check if a username already exists in a list of usernames.
usernames=["user1","user2","user3","admin"]
new_user="user4"
for username in usernames:
    if username==new_user:
        print("Username already exists")
        break
else:
    usernames.append(new_user)
    print("Username added successfully")

#Check whether a list contains any negative number.
numbers = [12, -45, 23, 67, -34, 89, 90]
for num in numbers:
    if num<0:
        print("List contains negative number")
        break
else:
    print("List does not contain any negative number")


