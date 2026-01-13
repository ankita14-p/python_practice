import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
employee_list=[
    {"name": "Alice Brown", "age": 30, "position": "Data Analyst", "salary": 65000, "tasks": ["Data Cleaning", "Data Visualization", "Reporting"], "current_hours": 38,"department":"IT"},
    {"name": "Emily Johnson", "age": 35, "position": "Project Manager", "salary": 80000, "tasks": ["Planning", "Coordinating", "Monitoring"], "current_hours": 50,"department":"Management"},
    {"name": "Michael Smith", "age": 28, "position": "Software Engineer", "salary": 72000, "tasks": ["Coding", "Code Review", "Testing"], "current_hours": 45,"department":"Development"},
    {"name": "Sarah Davis", "age": 32, "position": "UX Designer", "salary": 68000, "tasks": ["User Research", "Wireframing", "Prototyping"], "current_hours": 40},

]
def change_dept(employee,new_department):
    """Change the department of employees"""
    if 'department' not in employee:
        logging.warning(f"Employee {employee['name']} does not have a department field.")
        raise KeyError(f"Department field missing for employee {employee['name']}")
    employee['department'] = new_department
    return employee
departments_to_update = [
    (employee_list[0], "Business Intelligence"),  # This should work fine
    (employee_list[1], "Operations"),             # This should work fine
    (employee_list[3], "Quality Assurance"),      # This will raise KeyError
]
try:
    for emp,new_dept in departments_to_update:
         change_dept(emp,new_dept)
         print(f"Updated employee: {emp['name']}, New Department: {emp['department']}")
except KeyError as e:
    logging.error(e)
finally:
    logging.info("Department update process completed.")

    

    
    

