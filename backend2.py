#Given a list of response times, calculate:
#average response time
#number of responses > 1 second
list_1=[1.8,0.8,0.9,0.3,1.3]
sum_1=sum(list_1)
avg_1=sum_1/len(list_1)
print(f"The average response time is {avg_1}")
count=0
for i in list_1:
    if i>1:
        count+=1
    
print(f"The number of responses greater than 1 is {count}")

#Iterate through user records and print only active users.

user={
    "user1":{
        "username":"user1@example.com",
        "active":True,
    },
    "user2":{
        "username":"user2@example.com",
        "active":False,
    },
    "user3":{
        "username":"user3@example.com",
        "active":True,
    }
}
for key,value in user.items():
    if value.get("active"):
        print(value.get("username"))

#Read all the the login attempts and stop processing once ("blocked") appears
login_attempt=[]
def insert_login_attempts(login_attempt):
    for i  in range(1,6):
        user_response=input("Enter your response:")
        login_attempt.append(user_response)
insert_login_attempts(login_attempt)
for attempts in login_attempt:
    if attempts=="blocked" or attempts=="Blocked":
        print("Processing blocked")
        break
    else:
        print("Succesfully processed")

#Loop through requests and skip those with status code 404.

requests=[200,201,404,400,300,250,404,106]

for status in requests:
    if status==404:
        continue
    else:
        print(status)

#Simulate retry logic: try an operation maximum 3 times, stop if successful

count=0
for i in range(1,6):
    role=input("Enter your role:")
    if role=="employee":
        count+=1
        if count==3:
            print("Cannot proceed")
            break
        print("Access cannot be granted!Please Retry")      
    else:
        print("Access Granted")





