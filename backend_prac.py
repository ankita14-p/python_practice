#A user sends a request with a role.
#Allow access only if the role is "admin" or "manager". Otherwise return "403 Forbidden".
role=input("Enter your role:")

def request(role):
    if role=="admin" or role=="manager":
        print("Access Granted")
    else:
        print("403 Forbidden")

request(role)

#Validate user age during signup.
#< 18 → reject
#18–60 → accept
#> 60 → mark as "senior_user"

age=int(input("Enter your age:"))
if age<18:
    print("You must be above 18!")
elif age>=18 and age<=60:
    print("Signed up Successfully!")
else:
    user_type="senior_user"
    print(f"Signed up as {user_type}")

#An receives a request method (GET, POST, PUT, DELETE).
#Print which operation is being performed or "Invalid method".
request=input("Enter the type of request:")

def validation(request):
    match request:
        case "GET":
            print("GET method is performed")
        case "POST":
            print("POST method is performed")
        case "PUT":
            print("PUT method is performed")
        case "DELETE":
            print("DELETE method is performed")
        case _:
            print("Invalid Method")

validation(request)

#Check password strength:
#length ≥ 8
#contains at least one digit
#Print "Strong" or "Weak".
pas=input("Enter your passowrd:")

if len(pas)>=8:
    for char in pas:
        if char.isdigit():
            print("Strong")
            break
    else:
        print("Weak")
else:
    print("Weak")

#A payment service receives an amount.
#amount ≤ 0 → invalid
#amount > 0 and ≤ balance → success
#else → insufficient balance

amount=int(input("Enter the amount:"))
balance=5000
if amount<=0:
    print("Invalid!")
elif amount==balance:
    print("Paymeent Successful")
else:
    print("Insufficient Balance")



