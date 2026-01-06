#for
users=["alice","john","marie"]
for user in users:
    print(user)
    # Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive','Alice': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():   #.copy() helps to avoid runtime error as if copy is not used then we are changing the size of dictionary while iterating
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():   #items implies the status of the users
    if status == 'active':
        active_users[user] = status


#range --> iterates for a sequence of numbers (start,stop,step)
for i in range(5):
    print(i) #0-->5

#to print between specific numbers
for i in range(2, 6):
    print(i) #2-->5

#to print with specific step
print(list(range(1, 10, 2))) #1,3,5,7,9

#to print indices with values
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(i, fruits[i])

#this can also be done using enumerate
seasons=['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons,start=2))) #start=2 means index starts from 2

#for-else --> after complete execution of for the else block is executed
for i in range(1,15):
    if i%2==0:
        print(f"{i} is even")
else:
    print("Loop is over")

for x in range(6):
  if x == 3: 
     print(x+1)
  print(x)
else:
  print("Finally finished!")
