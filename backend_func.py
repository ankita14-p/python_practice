def create_task(*args,title,assigned_to,assigned_by,due_date):
    if title is " ":
        return "Error: Title cannot be empty"
    task={
        "title":title,
        "assigned_to":assigned_to,
        "assigned_by":assigned_by,
        "due_date":due_date,
        "tags":args
    }
    return task
def display_task(task):
    print("Title:",task["title"])
    print("Assigned To:",task["assigned_to"])
    print("Assigned By:",task["assigned_by"])
    print("Due Date:",task["due_date"])
    print("Tags:"," ".join(task["tags"]))

task1=create_task("urgent","remote","frontend",title="Complete Report",assigned_to="John",assigned_by="Alice",due_date="2026-02-15")
display_task(task1)

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
     
        


