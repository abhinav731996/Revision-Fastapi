class Employee:
    def __init__(self, employee_id, name, age, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display_details(self):
        print("---------------------------------------")
        print("Employee ID = ", self.employee_id)
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Department = ", self.department)
        print("Salary = ", self.salary)
        print("---------------------------------------")

    def update_salary(self, new_salary):

        if self.salary <= 0:
            raise ValueError("salary can't be nagitive !!")

        self.salary = new_salary
        print("\n Salary update successfully !! \n")


class EmployeeManager:

    def __init__(self):
        self.employee = []

    def find_employee(self, employee_id):

        for employee in self.employee:
            if employee.employee_id == employee_id:
                return employee

        return None
    
        