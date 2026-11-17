# # Class ---------------------------------------------------

# class Employee:
#     pass

# emp1 = Employee()
# emp2 = Employee()

# print(emp1)
# print(emp2)




# # __init__() Constructor ----------------------------------------
# # Maan lijiye hume employee object create karte time hi uska ID, name aur salary set karni hai.

# class Employee():

#     def __init__(self, employee_id, name, salary):
#         self.employee_id = employee_id
#         self.name = name
#         self.salary = salary


# emp1 = Employee(101, "Abhinav", 55000)

# print(emp1.employee_id)
# print(emp1.name)
# print(emp1.salary)
        



# # Attributes and Methods ------------------------------------------
# # Class ke andar variables ko attributes aur functions ko methods kehte hain.

# class Employee:

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary =  salary

#     def display_details(self):
#         print("name : ", self.name)
#         print("salary : ", self.salary)

#     def update_salary(self, new_salary):
#         self.salary = new_salary
#         print("salary updated successfully !!")


# emp1 = Employee("abhinav", 55000)

# emp1.display_details()

# emp1.update_salary(60000)

# emp1.display_details()





# # Inheritance -------------------------------------------
# # Inheritance ka meaning hai ek class doosri class ke properties aur methods ko inherit kar sakti hai.

# class Employee:

#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary

#     def desplay_details(self):
#         print("id = ", self.id)
#         print("name = ", self.name)
#         print("salary = ", self.salary)

# class Developer(Employee):

#     def __init__(self, id, name, salary, skill):
#         super().__init__(id, name, salary)
#         self.skill = skill

#     def display_skills(self):
#         print("id = ", self.id)
#         print("name = ", self.name)
#         print("salary = ", self.salary)
#         print("skill = ", self.skill)

    

# dev1 = Developer(101, "Abhinav", 55000, "python")

# # dev1.desplay_details()
# dev1.display_skills()



# # Encapsulation ----------------------------------------------
# # Encapsulation ka meaning hai data aur usse related methods ko ek class mein organise karna, aur data access ko controlled rakhna.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary
    
#     def get_salary(self):
#         return self._salary

#     def update_salary(self, new_salary):

#         if new_salary > 0:
#             self._salary = new_salary
#             print("salary updated !!")

#         else:
#             print("invald salary !!")

# emp1 = Employee("abhinav", 55000)

# print(emp1.get_salary())

# emp1.update_salary(60000)

# print(emp1.get_salary())




# #  Polymorphism ---------------------------------------------------------
# # Polymorphism ka meaning hai same method name, different classes mein different behaviour de sakta hai.

class Employee:

    def work(self):
        print("Employee is working")


class Developer(Employee):

    def work(self):
        print("Developer is writing the code")

class Manager(Employee):

    def work(self):
        print("Manager is managing the team")

emp1 = Employee()
dev1 = Developer()
manag1 = Manager()

emp1.work()
dev1.work()
manag1.work()