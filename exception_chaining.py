
class TaskAssignmnetError(Exception):
    """Custom exception for task assignment errors."""
    pass
employee1={
    "name":"Jane Smith",
    "emp_id":102,
    "tasks":["Prepare Presentation","Client Meeting"],
    "worload_per_task":0
}
employee2={
    "name":"Mike Johnson",
    "emp_id":103,
    "tasks":["Data Analysis","Report Writing"],

}
def calculate_workload(emp_data,total_hours, num_tasks):
    """Calculate workload per task."""
    try:
        workload_per_task = total_hours / num_tasks
    except ZeroDivisionError as e:
        raise TaskAssignmnetError("Cannot assign tasks when there are zero tasks.") from e
    else:
        emp_data['worload_per_task'] = workload_per_task
        return f"Workload per task for {emp_data['name']}: {workload_per_task} hours"  
    
tasks_to_process=[
        (employee1, 40, 0),  # This will raise ZeroDivisionError
        (employee1, 50, 5),  # This should work fine
        (employee2, 30, 3)   # This will raise KeyError

    ] 
for emp_data, total_hours, num_tasks in tasks_to_process:
    try:
        result = calculate_workload(emp_data, total_hours, num_tasks)
    except TaskAssignmnetError as e:
        print(f"Error for employee {emp_data['name']}: {e}")
    else:
        print(result)



    