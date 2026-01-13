import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
employee_profile={
    "employee_1":{
        "id":101,
        'name': 'Alice Brown',
        'age': 30,
        'position': 'Data Analyst',
        'salary': 65000,
    },
    "employee_2":{
        "id":102,
        'name': 'Michael Smith',
        'age': 28,
        'position': 'Software Engineer',
        'salary': 72000,
    },
    "employee_3":{
        "id":103,
        'name': 'Sarah Davis',
        'age': 32,
        'position': 'UX Designer',
        'salary': 68000,
    },
    "employee_4":{
        "id":104,
        'name': 'David Wilson',
        'age': 40,
        'position': 'DevOps Engineer',
        'salary': 75000,
    },
    "employee_5":{
        "id":105,
        'name': 'Linda Martinez',
        'age': 29,
        'position': 'Product Manager',
        'salary': 80000,
    }
    
}
id_to_find=int(input("Enter Employee ID to search: "))
def get_employee_name(id_to_find):
    try:
        for emp in employee_profile.values():
            if emp['id']==id_to_find:
                return emp['name']
        raise Exception("Employee ID not found.")
    except Exception as e:
        print(e)
        logging.error(f"Error occurred! {id_to_find} not found.")
    finally:
        logging.info("Search operation completed.")
employee_name=get_employee_name(id_to_find)
if employee_name:
    print(f"Employee Name: {employee_name}")
    
    
