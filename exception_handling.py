#try--> test the expected error to occur
#except--> handle the error
#else--> if no error occurs
#finally--> always execute this block
def calculate_workload(total_hours,deadline):
    try:
        hours_per_day=total_hours/deadline
    except ZeroDivisionError:
        return "You have no time left!"
    except TypeError:
        return "Invalid input!Please enter numerical values"
    else:
        return f"You need to work {hours_per_day} hours per day to meet the deadline."
    finally:
        print("Workload calculation attempted.")
print(calculate_workload(40,0))
print(calculate_workload(40,"five"))
print(calculate_workload(40,5))

#Built-in Exceptions

#ArithmeticError--> errors related to mathematical operations
def divide_numbers(num1,num2):
    try:
        result=num1/num2
    except ArithmeticError as e:
        print(e)
    else:
        return f"The result is {result}"
divide_numbers(10,0)
#OverflowError--> when a calculation exceeds the maximum limit
import math
try:
    result = math.exp(1000)  # Exponential function with a large argument
except OverflowError as e:
    print(e)
else:
    print(f"The result is {result}")
#AssertionError--> when an assert statement fails
try:
    assert 1 == 2, "Assertion failed"
except AssertionError as e:
    print(e)

#AttributeError--> when an attribute reference or assignment fails
class MyClass:
    pass

obj = MyClass()

try:
    obj.some_attribute
except AttributeError as e:
    print(e)
#IndexError--> when a sequence subscript is out of range
list_1=[1,2,3,4]
try:
    element=list_1[10]
except IndexError as e:
    print(e)
else:
    print(f"Element is {element}")
#KeyError--> when a dictionary key is not found
my_dict={"a":1,"b":2}
try:
    value=my_dict["c"]
except KeyError as e:
    print(e)
else:
    print(f"Value is {value}")
#MemoryError--> when an operation runs out of memory
try:
    li = [1] * (10**10)
except MemoryError as e:
    print(e)
#ValueError--> when a function receives an argument of the right type but inappropriate value
try:
    number=int("abc")
except ValueError as e:
    print(e)
#TypeError--> when an operation or function is applied to an object of inappropriate type
try:
    result="2"+2
except TypeError as e:
    print(e)

    