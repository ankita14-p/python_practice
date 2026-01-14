from dataclasses import dataclass
@dataclass
class Task:
    total_tasks=0
    title: str
    description: str
    status: str
    priority: str
    due_date: str
    __duration: int
    def __post_init__(self):
        Task.total_tasks += 1
    @staticmethod
    def is_valid_title(title:str)->bool:
       return len(title)>3
    def create_task(title,description,status,priority,due_date,duration):
        if Task.is_valid_title(title):
            return Task(title,description,status,priority,due_date,duration)
    def __str__(self):
        return f"Task: {self.title}, Description: {self.description}, Status: {self.status}, Priority: {self.priority}, Due Date: {self.due_date}"
    @property
    def get_duration(self):
        return self.__duration
    @get_duration.setter
    def set_duration(self,duration):
        if duration<0:
            raise ValueError("Duration cannot be negative")
        self.__duration=duration
    @classmethod
    def get_system_stats(cls):
        return f"Total tasks in the system: {cls.total_tasks}"
class Employee:
    def __init__(self,emp_id,emp_name,role,task:Task=None):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.role = role
        self.task = []
    def assign_task(self,task):
        self.task.append(task)
    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.emp_name}, Role: {self.role} and Tasks: {[str(t) for t in self.task]}"
emp1=Employee(1,"John","developer")
emp2=Employee(2,"Alice","manager")

task1=Task.create_task("Fix Bug","Fix the login bug","In Progress","High","2024-07-01",5)
task2=Task.create_task("Develop Feature","Develop the payment feature","Not Started","Medium","2024-08-01",10)
emp1.assign_task(task1)
emp2.assign_task(task2)
print(emp1)
print(emp2)
print(Task.get_system_stats())
try:
    task1.set_duration=-5
except ValueError as e:
    print(e)


