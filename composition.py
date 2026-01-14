class assign_task_to_employee:
    def execute(self):
        return f"Assigns task to employee"
class assigns_task_to_deptartment:
    def execute(self):
        return f"Assigns task to department"
class performes_task:
    def execute(self):
        return f"Performs the assigned task"
class Employee:
    def __init__(self,emp_id,name,role):
        self.emp_id = emp_id
        self.name = name
        self.role = role
    def task_to_perform(self):
        print(f"Employee {self.name} with ID {self.emp_id} {self.role.execute()}.")
admin=assign_task_to_employee()
manager=assigns_task_to_deptartment()
emp=performes_task()
emp1=Employee(1,"John",manager)
emp1.task_to_perform()
emp2=Employee(2,"Alice",admin)
emp2.task_to_perform()
emp3=Employee(3,"Bob",emp)
emp3.task_to_perform()
emp1.role=assigns_task_to_deptartment()
emp1.task_to_perform()