task_list=[]
def create_task(*args,dept_name,title,assigned_to,assigned_by,due_date):
    if title==" ":
        return "Error: Title cannot be empty"
    task={
        "title":title,
        "assigned_to":assigned_to,
        "assigned_by":assigned_by,
        "department":dept_name,
        "due_date":due_date,
        "tags":args
    }
    task_list.append(task)
def display_task():
      for task in task_list:
            print(f"{task}")

create_task("urgent","remote","frontend",dept_name="it",title="Complete Report",assigned_to="John",assigned_by="Alice",due_date="2026-02-15")
create_task("urgent","remote","frontend",dept_name="hr",title="Complete Report",assigned_to="John",assigned_by="Alice",due_date="2026-02-15")
create_task("urgent","remote","frontend",dept_name="it",title="Complete Report",assigned_to="John",assigned_by="Alice",due_date="2026-02-15")
display_task()

def update_task_status(task:int,*,status:str):
     """Update the status of a task."""
     statuses=["Pending","In Progress","Completed","On Hold"]
     if status not in statuses:
            return "Error: Invalid status"
     task_status={
          "task_id":task,
          "status":status
     }
     return task_status
task_status1=update_task_status(201,status="In Progress")
def display_task_staus(task_status):
        print("Task ID:",task_status["task_id"])
        print("Status:",task_status["status"])
display_task_staus(task_status1)

def get_tasks_by_department(task_list,/,dept_name="General"):
        """Retrieve tasks by department."""
        filtered_tasks=[task for task in task_list if task["department"]==dept_name]
        return filtered_tasks
it_tasks=get_tasks_by_department(task_list,dept_name="it")
print(it_tasks)
active_subscribers=[]
def add_subscriber(email:str,current_list=None):
    """Add a subscriber to the mailing list."""
    if current_list is None:
          current_list=[]
    current_list.append(email)
    return 
add_subscriber("ankita@example.com") #not added in active_subscribers
add_subscriber("john@example.com",active_subscribers)
add_subscriber("alice@example.com",active_subscribers)
print(active_subscribers)
active_employees=[101,104,109,108,110,111]
def log_action(*,employee_id:int,action:str,**kwargs) -> str | dict:
      """Log an action performed by an employee"""
      if employee_id not in active_employees:
            return "Error: Unauthorized employee"
      action_log={
            "employee_id":employee_id,
            "action":action,
            "details":kwargs
        }
      return action_log

action=log_action(employee_id=104,action="Updated Task",browser="Chrome",timetsamp="2024-10-01 10:00:00")
print(action)
     



     
        


