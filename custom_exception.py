#Custom exception
class WorkloadLimitError(Exception):
    """Raises error when workload on an employee exceeds limit"""
    pass
employee1={
    "name":"John Doe",
     "tasks":["Code Review","Write Documentation","Implement Feature X"]

}
def assign_task(employee,task):
    if len(employee["tasks"])>=5:
        raise WorkloadLimitError(f"Cannot assign task '{task}' to {employee['name']}: Workload limit exceeded.")
    employee["tasks"].append(task)
    return f"Task '{task}' assigned to {employee['name']}."

try:
    print(assign_task(employee1,"Design Database Schema"))
    print(assign_task(employee1,"Optimize Performance"))
    print(assign_task(employee1,"Fix Bugs"))
    print(assign_task(employee1,"Update Dependencies"))
    print(assign_task(employee1,"Conduct Testing"))
    print(assign_task(employee1,"Prepare Release Notes"))
except WorkloadLimitError as e:
    print("Error!:",e)

#Raising Exception
def check_deadline(deadline_days):
    if deadline_days < 3:
        raise ValueError("Deadline too short! Must be at least 3 days.")
    return "Deadline is acceptable."
try:
    print(check_deadline(2))
except ValueError as e:
    print("Error!:",e)



