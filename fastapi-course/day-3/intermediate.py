# # ------------------------ Tuples ---------------------------
# employee = ("Abhinav", 25, "Developer")

# print(employee)
# print(employee[0])
# print(employee[1])



# # ------------------------ Sets -----------------------------

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

# print(company["name"])

# print(company["employees"]["employee_1"]["name"])

# print(company["employees"]["employee_1"]["department"])




# # ---------------------------- Enumerate -----------------------------
# # Jab list ke elements ke saath unka index bhi chahiye, tab enumerate() use karte hain.

# employee = ["Kajal", "Abhinav", "Kumkum"]

# for i in range(len(employee)):
#     print(i, employee[i])

# print('**************** by using enumerate *******************')

# for index, name in enumerate(employee):
#     print(index, name)

# print('**************** by using enumerate & start with 1 *******************')

# for index, name in enumerate(employee, start=1):
#     print(index, name)



# # ------------------------------------ ZIP -------------------------------------
# # zip() ka use multiple lists ke corresponding elements ko ek saath access karne ke liye hota hai.

# name = ["Kajal", "Abhinav", "Kumkum"]
# departments = ["Doctor", "IT", "QA"]

# for name, departments in zip(name, departments):
#     print(name,"=", departments)



# ------------------------------ List Comprehension ----------------------------
# Ye Python mein list create karne ka short aur useful method hai.

numbers = [1, 2, 3, 4, 5]
squares = []

for i in numbers:
    squares.append(i ** 2)

print(squares)

