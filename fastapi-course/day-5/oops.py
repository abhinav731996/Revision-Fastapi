# # Class ---------------------------------------------------

# class Employee:
#     pass

# emp1 = Employee()
# emp2 = Employee()

# print(emp1)
# print(emp2)




# # __init__() Constructor ----------------------------------------
# # Maan lijiye hume employee object create karte time hi uska ID, name aur salary set karni hai.

class Employee():

    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary


emp1 = Employee(101, "Abhinav", 55000)

print(emp1.employee_id)
print(emp1.name)
print(emp1.salary)
        



# # Attributes and Methods ------------------------------------------
# # Class ke andar variables ko attributes aur functions ko methods kehte hain.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary =  salary

    def display_details(self):
        print("name : ", self.name)
        print("salary : ", self.salary)

    def update_salary(self, new_salary):
        self.salary = new_salary
        print("salary updated successfully !!")


emp1 = Employee("abhinav", 55000)

emp1.display_details()

emp1.update_salary(60000)

emp1.display_details()



        