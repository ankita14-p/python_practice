def create_task(*args,title,assigned_to,assigned_by,due_date):
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
