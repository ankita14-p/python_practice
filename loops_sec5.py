#Given a list of user dictionaries:
#Count how many users are active

users = [
    {"id": 1, "active": True},
    {"id": 2, "active": False},
    {"id": 3, "active": True}
]
active_count=0
for user in users:
    if user.get("active"):  #get() is used to acces items in dictionary
        active_count+=1
print(f"Number of active users: {active_count}")

#From a list of emails, print only valid emails (must contain @ and .).
emails=["ank@user.example","invalidemail.com","user@domain"]
for email in emails:
    if "@" in email and "." in email:
        print(f"Valid email: {email}")
    else:
        print(f"Invalid email: {email}")

#Given request logs as status codes.Count how many requests failed (status code ≥ 400).
logs = [200, 201, 400, 401, 500, 200]
failed_count=0
for status in logs:
    if status>=400:
        failed_count+=1
print(f"Number of failed requests: {failed_count}")

#Given a list of keys, check whether a provided key is valid.
#If found → "Access Granted"
#Else → "Invalid Key"

keys = ["key1", "key2", "key3"]
provided_key = "key2"
for key in keys:
    if provided_key in keys:
        print("Access Granted")
        break
else:
    print("Invalid Key")
#Check if a user ID exists before processing a request.
#Use for-else
#Print "User Found" or "User Not Found"
user_ids = [101, 102, 103, 104]
search_id = 105
for uid in user_ids:
    if uid==search_id:
        print("User Found")
        print("Request processed")
        break
else:
    print("User Not Found")


