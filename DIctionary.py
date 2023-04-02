#get employee details using employee id
employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"}]

def get_employee(id):
    for employee in employee_list:
        if employee['id']==id:
            return employee


print(get_employee(12345))
