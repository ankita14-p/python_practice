class Student:
    college="XYZ" #class atributes
    def __init__(self,name,roll_no,age,dept):
        self.name=name #instance attributes
        self.roll_no=roll_no
        self.age=age
        self.dept=dept
    def get_roll_no(self): #Method
       print(f"Roll no is {self.roll_no}")
    def get_dept(self):
        return self.dept
s1=Student("Ankita",6,22,"CS")
s1.get_roll_no()
print(s1.get_dept())    

s1.college="yyy" #overidden
print(s1.college)

# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print(f"{self.name} woofs")

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()