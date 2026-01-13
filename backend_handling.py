import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

emp_profile = {
    "employee_1":{
        'name': 'John Doe',
        'age': 30,
        'position': 'Software Engineer',
        'salary': 70000,
        'task':['Developing','Testing','Code Review'],
        'current_hours':45
    },
    "employee_2":{
        'name': 'Jane Smith',
        'age': 28,
        'position': 'Data Analyst',
        'salary': 65000,
        'task':['Data Cleaning','Data Visualization','Reporting'],
        'current_hours':38
    },
    "employee_3":{
        'name': 'Emily Johnson',
        'age': 35,
        'position': 'Project Manager',
        'salary': 80000,
        'task':['Planning','Coordinating','Monitoring'],
        'current_hours':50
    }

}

def update_emp_salary(emp_profile,new_slary):
    """Updating the salary of the employees"""
    try:
        emp_profile['salary'] = new_slary
    except TypeError as e:
        print(e)
    else:
        logging.success(f"Salary updated to {new_slary} for employee {emp_profile.get('name', 'Unknown')}")
    finally:
        logging.info("Database connection closed.")
        return emp_profile
update_emp_salary(emp_profile['employee_1'],75000)

class OverWorkLoadError(Exception):
    """Custom exception for overwork situations."""
    pass
def add_working_hours(emp_profile,additional_hours):
    """Adding new working hours to the current hours of the employee"""
    new_hours= emp_profile['current_hours'] + additional_hours
    if new_hours>50:
        raise OverWorkLoadError(f"can't assign task to {emp_profile['name']} as it exceeds maximum working hours.")
    emp_profile['current_hours']=new_hours
    logging.info(f"Updated working hours for {emp_profile['name']}: {emp_profile['current_hours']} hours")
    return emp_profile
working_hours_to_add = [
    (emp_profile['employee_1'], 5),   # This should work fine
    (emp_profile['employee_2'], 15),  # This will raise OverWorkLoadError
    (emp_profile['employee_3'], 3)    # This will raise OverWorkLoadError
]

for emp_data, additional_hours in working_hours_to_add:
    try:
        updated_profile = add_working_hours(emp_data, additional_hours)
    except OverWorkLoadError as e:
        logging.error(e)
    else:
        logging.info(f"Successfully added hours for {emp_data['name']}. New hours: {updated_profile['current_hours']}")



    

    
    
