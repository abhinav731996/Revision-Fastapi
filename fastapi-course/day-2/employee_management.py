# # -------------------------------- Lists -------------------------------------

# employees = ["Rahul", "Priya", "Amit", "Neha"]

# print(employees)
# print(employees[2])

# employees.append("Abhinav")
# print(employees)

# employees.remove("Amit")
# print(employees)

# print(len(employees))




# # ----------------------------------- Dictionaries -------------------------------

# employee = {
#     "id" : 101,
#     "name" : "Abhinav",
#     "age" : 25,
#     "department": "IT",
#     "salary" : 35000
# }

# print(employee)

# print(employee["name"])
# print(employee["salary"])

# employee["emial"] = "abhinav@gmail.com"

# print(employee)

# employee["salary"] = 40000
# print(employee)

# del employee["age"]
# print(employee)

# print(employee.get("age"))                  # none
# print(employee.get("age", 28))              # default value




# # ----------------------- List of dictionary --------------------------

# employees = [

#     {
#         "id": 101,
#         "name": "Rahul",
#         "department": "IT",
#         "salary": 35000
#     },

#     {
#         "id": 102,
#         "name": "Priya",
#         "department": "HR",
#         "salary": 30000
#     },

#     {
#         "id": 103,
#         "name": "Amit",
#         "department": "Finance",
#         "salary": 40000
#     }

# ]

# # print(employees)

# print(employees[2]["name"])


# for i in employees:
#     print(i["id"])


# employee["salary"] = 40000

# print(employee["salary"])

# ----------------------------- Practice ------------------------------
# 5. Employee Management System mein Add, View, Search, Update, Delete aur Exit sabhi features implement kijiye.

employees = [

    {
        "id": 101,
        "name": "Rahul",
        "age": 25,
        "department": "IT",
        "salary": 35000
    },

    {
        "id": 102,
        "name": "Priya",
        "age": 27,
        "department": "HR",
        "salary": 30000
    }

]

# ======== to view all data =========
def view_employee():
    for i in employees:

            print("------------------------")

            print("Employee ID: ", i["id"])
            print("Name: ", i["name"])
            print("Age: ", i["age"])
            print("Salary: ", i["salary"])

# view_employee()


# ======== to add data ==========
# print("\n********************** to add *************************************")
def add_employee():

    emp_id = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter department: ")
    salary = int(input("Enter salary: "))

    add = {
        "id":emp_id,
        "name":name,
        "age":age,
        "department":department,
        "salary":salary
    }

    employees.append(add)

    print("Employee add successfully!!")


# add_employee()

# view_employee()



# ============= to search employees ============

# print("\n****************** to search *****************************************")
def search_employee():

    emp_id = int(input("Enter your id: "))

    for search in employees:

        if search["id"] == emp_id:
            print("\nEmployee found !!!\n")

            print("Employee ID: ", search["id"])
            print("Employee Name: ", search["name"])
            print("Employee Age: ", search["age"])
            print("Employee Department: ", search["department"])
            print("Employe Salary: ", search["salary"])


            # print(search)

            return

    print("employee not found!!!!!")


# search_employee()

# view_employee()




# ================= to update employees =====================
def update_employee():
    emp_id = int(input("Enter employee ID: "))

    for i in employees:
        if i["id"]==emp_id:
            print("Employee found!!")

            new_salary = int(input("please enter new salary: "))

            i["salary"] = new_salary

            print("salary updated successfully!!!")

            print(i)




# ================== to delete employees =================

# print("\n******************** to delete **************************************")
def delete_employee():

    emp_id = int(input("Enter employee ID: "))

    for delete in employees:
        if delete["id"] == emp_id:
            employees.remove(delete)

            print("Employee deleted successfully!!")

            return

        print("employee not found!!!!!!")

# delete_employee()

# view_employee()

# print("\n***********************************************************")



while True:

    print("\n =========== Employee management system ===========")

    print("Press 1 to add employee: ")
    print("Press 2 to delete employee: ")
    print("Press 3 to search employee: ")
    print("Press 4 to view all employee: ")
    print("Press 5 to exit: ")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        delete_employee()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        view_employee()

    elif choice == 5:
        print("Thank you!!")
        break

    else:
        print("Please select a valid choice!!!!!!")