class Employee:

    def __init__(self, employee_id, name, age, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    
    def desplay_details(self):

        print("---------------------------------------")
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Detaprtment = ", self.department)
        print("Salary = ", self.salary)
        print("---------------------------------------")


    def update_salary(self, new_salary):

        if new_salary < 0:
            raise ValueError("salary cannot be -ve !!")

        self._salary = new_salary
        print("Salary update successfully !!!!")


class EmployeeManager:

    def __init__(self):

        self.employee = []

    def find_employee(self,employee_id):

        for employee in self.employee:
            if employee.employee_id == employee_id:
                return employee

        return None

    # def add_employee(self):

    #     try:
    #         employee_id = int(input("Please enter employee ID: "))

    #         if self.find_employee