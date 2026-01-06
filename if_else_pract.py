#Even number or odd number
num=int(input("Enter an integer number: "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
#greatest of three numbers
a=9
b=8
c=10
if a>b and a>c:
    print(f"{a} is the greatest number")
elif b>a and b>c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")
#grading system
marks=int(input("Enter your marks: "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=75 and marks<=89:
    print("Grade B")
elif marks>=60 and marks<=74:
    print("Grade C")
elif marks>=40 and marks<=59:
    print("Grade D")
else:
    print("Grade F")    
