#Create a User class with attributes id, name, and email.
#Create 3 user objects and print their details.
class User:
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email
    def __str__(self):
        return f"Id:{self.id},Name:{self.name} and Email:{self.email}"
u1=User(101,"Ankita","ankita@example")
u2=User(102,"John","john@example")
print(u1)
print(u2)
        