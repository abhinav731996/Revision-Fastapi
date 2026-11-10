# # 1. 5 employee names ki list banaiye. Ek naya employee add kijiye aur sabhi names loop se print kijiye.

# employee = ["abhinav", "dinesh", "kaushik", "sakhir", "taif"]

# employee.append("sayeed")

# for i in employee:
#     print(i)




# # 2. Ek employee dictionary banaiye jisme id, name, age, department aur salary ho. Salary update kijiye aur email add kijiye.

# employee = {
#         "id":101,
#         "name":"abhinav",
#         "age":25,
#         "salary":120000,
#         "department": "Management"
#     }

# employee["salary"] = 150000

# employee["email"] = "abhinav@gmail.com"

# print(employee)



# # 3. List of dictionaries mein employee ID ke through employee search karne ka function banaiye.

# employee =[ 
#     {
#         "id":101,
#         "name":"abhinav",
#         "age":25,
#         "salary":120000,
#         "department": "Management"
#     },
#     {
#         "id":102,
#         "name":"Sahil",
#         "age":22,
#         "salary":20000,
#         "department": "Management"
#     },
# ]


# def search_id():

#     emp_id = int(input("Please enter your search ID: "))

#     for i in employee:
#         if i["id"] == emp_id:
#             print(i)

#             return

#     print("employe not found!!!!")


# search_id()



# # 4. Employee ID input lekar us employee ki salary update karne ka function banaiye.

# employee =[ 
#     {
#         "id":101,
#         "name":"abhinav",
#         "age":25,
#         "salary":120000,
#         "department": "Management"
#     },
#     {
#         "id":102,
#         "name":"Sahil",
#         "age":22,
#         "salary":20000,
#         "department": "Management"
#     },
# ]

# print(employee)
# def update_salary():

#     emp_id = int(input("Please enter ID: "))

#     for i in employee:

#         if i["id"] == emp_id:
#             print("Employe found !!!!")

#             new_salary = int(input("Please enter new salary: "))

#             i["salary"] = new_salary

#             print("salary updated successfully")

#             print(i)


# update_salary()