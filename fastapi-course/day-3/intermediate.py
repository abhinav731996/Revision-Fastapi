# # ------------------------ Tuples ---------------------------
# # tuple immutable hota hai
# employee = ("Abhinav", 25, "Developer")

# print(employee)
# print(employee[0])
# print(employee[1])



# # ------------------------ Sets -----------------------------
# # Set ek collection hai jo duplicate values allow nahi karta.
# department = {"it", "hr", "IT", "sales", "Hr","it", "hr"}

# print(department)

# department.add("Marketing")

# department.remove("hr")
# department.remove("it")

# print(department)
# print("IT" in department)



# # -------------------------- Nested Dictionary ------------------------

# company = {
#     "name": "Indixpert",
#     "location": "Gurugram",
#     "employees": {
#         "employee_1": {
#             "id": 101,
#             "name": "Abhinav",
#             "department": "IT"
#         },
#         "employee_2": {
#             "id": 102,
#             "name": "Rahul",
#             "department": "HR"
#         }
#     }
# }

# print(company)

# print(company["name"])

# print(company["employees"]["employee_1"]["name"])

# print(company["employees"]["employee_1"]["department"])




# # ---------------------------- Enumerate -----------------------------
# # Jab list ke elements ke saath unka index bhi chahiye, tab enumerate() use karte hain.

# employee = ["Kajal", "Abhinav", "Kumkum"]

# for i in range(len(employee)):
#     print(i, employee[i])

# # print('**************** by using enumerate *******************')

# for index, name in enumerate(employee):
#     print(index, name)

# # print('**************** by using enumerate & start with 1 *******************')

# for index, name in enumerate(employee, start=1):
#     print(index, name)

# # print('**************** by using enumerate & start with 1 *******************')
# for index, name in enumerate(employee, start=1):
#     print(index, ".)", name)

# # ------------------------------------ ZIP -------------------------------------
# # zip() ka use multiple lists ke corresponding elements ko ek saath access karne ke liye hota hai.

# name = ["Kajal", "Abhinav", "Kumkum"]
# departments = ["Doctor", "IT", "QA"]

# for name, departments in zip(name, departments):
#     print(name,"=", departments)



# # ------------------------------ List Comprehension ----------------------------
# # Ye Python mein list create karne ka short aur useful method hai.

# numbers = [1, 2, 3, 4, 5]
# squares = []
# even_num = []

# for i in numbers:
#     squares.append(i ** 2)

# print(squares)

# for i in numbers:
#     if(i %2 == 0):
#         even_num.append(i)

# print(even_num)



# # -------------------------------------------- Practice -------------------------------------------

# # ===== 1 (Ek tuple banao jisme 5 employee names hon. Loop use karke sabhi names print karo.)=======
# list = ("Abhinav", "Kaushik", "Sumit", "Dinesh", "Sahil")

# for i  in range(len(list)):
#     print(list[i])


# # ===== 2 (Ek list banao: ["IT", "HR", "IT", "Sales", "HR", "Marketing"]. Set ka use karke unique departments print karo.) =====

# departments = ["IT", "HR", "IT", "Sales", "HR", "Marketing"]

# set_depart = set()

# set_depart.update(departments)

# print(set_depart)


# ===== 3 (Ek company dictionary banao jisme company name, location aur 2 employees ki details (id, name, salary) hon. Dono employees ke names aur salaries print karo.) =====

# company = {
#     "name": "Indixpert",
#     "location": "Gurgaon",
#     "employees": {
#         "employee_1": {
#             "name": "Abhinav",
#             "salary": 50000
#         },
#         "employee_2": {
#             "name": "Sahil",
#             "salary": 40000
#         }
#     }
# }

# # print(company["employees"]["employee_1"]["name"])
# # print(company["employees"]["employee_1"]["salary"])

# # print(company["employees"]["employee_2"]["name"])
# # print(company["employees"]["employee_2"]["salary"])


# for key, value in company["employees"].items():
#     print( value["name"], value["salary"])



# # ===== 4 5 employee names ki list banao aur enumerate() se unke names ke saath numbering 1 se print karo. =====

# employees = ("Abhinav", "Kaushik", "Sumit", "Dinesh", "Sahil")

# for index, name in enumerate(employees, start=1):
#     print(index, name)


# # ===== 5 Do lists banao: employee names aur unke salaries. zip() se har employee ka name aur salary print karo. =====

# employee_name = ["Abhinav", "Dinesh", "Kaushik"]

# employee_salary = [50000, 45000, 40000]

# for employee_name, employee_salary in zip(employee_name, employee_salary):
#     print(employee_name, "=", employee_salary)



# # ===== 6 1 se 20 tak numbers ki list banao aur list comprehension se sirf even numbers ki new list banao. =====

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# even_list = []

# for i in list:
#     if(i%2 == 0):
#         even_list.append(i)

# print(even_list)



# # Day 3 practical challenge ===============================================
# 1. List comprehension use karni hai.
# 2. Salary ₹40,000 se zyada honi chahiye.
# 3. Sirf selected employees ka name aur salary print karna hai.

employees = [
    {"id": 101, "name": "Abhinav", "salary": 50000},
    {"id": 102, "name": "Sahil", "salary": 30000},
    {"id": 103, "name": "Kaushik", "salary": 45000},
    {"id": 104, "name": "Dinesh", "salary": 25000},
    {"id": 105, "name": "Sumit", "salary": 60000}
]

selected_emp = []

for emp in employees:
    if(emp["salary"] > 40000):
        selected_emp.append({
            "name": emp["name"],
            "salary":emp["salary"]
        })


print(selected_emp)