
class Employee:

    def __init__(self, employee_id, name, age, department, salary):

        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.department = department
        self._salary = salary

    def display_details(self):

        print("-------------------------")
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", self._salary)
        print("-------------------------")

    def update_salary(self, new_salary):

        if new_salary < 0:
            raise ValueError("Salary cannot be negative")

        self._salary = new_salary
        print("Salary updated successfully!")


class EmployeeManager:

    def __init__(self):

        self.employees = []

    def find_employee(self, employee_id):

        for employee in self.employees:

            if employee.employee_id == employee_id:
                return employee

        return None

    def add_employee(self):

        try:
            employee_id = int(input("Enter employee ID: "))

            if self.find_employee(employee_id):
                print("Employee ID already exists!")
                return

            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))

            if age < 18:
                print("Employee must be at least 18!")
                return

            if salary < 0:
                print("Salary cannot be negative!")
                return

            employee = Employee(
                employee_id,
                name,
                age,
                department,
                salary
            )

            self.employees.append(employee)

            print("Employee added successfully!")

        except ValueError:
            print("Please enter valid numeric values!")

    def view_employees(self):

        if not self.employees:
            print("No employees found!")
            return

        for employee in self.employees:
            employee.display_details()

    def search_employee(self):

        try:
            employee_id = int(input("Enter employee ID: "))

            employee = self.find_employee(employee_id)

            if employee:
                employee.display_details()
            else:
                print("Employee not found!")

        except ValueError:
            print("Please enter a valid employee ID!")

    def update_employee(self):

        try:
            employee_id = int(input("Enter employee ID: "))

            employee = self.find_employee(employee_id)

            if employee:

                new_salary = float(
                    input("Enter new salary: ")
                )

                employee.update_salary(new_salary)

            else:
                print("Employee not found!")

        except ValueError as error:
            print("Invalid input:", error)

    def delete_employee(self):

        try:
            employee_id = int(input("Enter employee ID: "))

            employee = self.find_employee(employee_id)

            if employee:

                self.employees.remove(employee)

                print("Employee deleted successfully!")

            else:
                print("Employee not found!")

        except ValueError:
            print("Please enter a valid employee ID!")


manager = EmployeeManager()

while True:

    print("\n====== EMPLOYEE MANAGEMENT SYSTEM ======")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_employee()

    elif choice == "2":
        manager.view_employees()

    elif choice == "3":
        manager.search_employee()

    elif choice == "4":
        manager.update_employee()

    elif choice == "5":
        manager.delete_employee()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Please select a valid option!")
