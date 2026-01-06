#Print numbers from 10 to 1 using range().
for i in range(10,0,-1):
    print(i)

#Print all odd numbers between 1 and 50.
for i in range(1,51,2):
    print(i)

#Print multiples of 5 between 1 and 100.
for i in range(5,101,5):
    print(i)

#Print numbers from 100 to 0, decreasing by 10.
for i in range(100,-1,-10):
    print(i)

#Find the sum of all numbers divisible by 3 between 1 and 100.
sum=0
for i in range(1,101):
    if i%3==0:
       sum+=i
print(f"The sum of all numbers divisible by 3 between 1 and 100 is: {sum}")

#Print all numbers between 1 and 100 that are divisible by both 3 and 5.
for i in range (1,101):
    if i%3==0 and i%5==0:
        print(i)