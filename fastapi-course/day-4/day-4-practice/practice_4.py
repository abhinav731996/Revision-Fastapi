# # Ek function banao calculate_total(*args). 5 numbers pass karo aur unka sum return karo.

# def calculate_total(*args):
#     return sum(args)

# result = calculate_total(4,7,8,7,5)

# print(result)



# # Ek function employee_details(**kwargs) banao. Name, age, department aur salary pass karo. Loop se saari key-value pairs print karo.

# def employee_details(**kwargs):
#     for keys, values in kwargs.items():
#         print(keys, ": ", values)


# employee_details(
#     name = "Abhinav",
#     age = 29,
#     department = "IT",
#     salary = 55000
# )



# # Do numbers input lo aur division perform karo. ValueError aur ZeroDivisionError ko separately handle karo. Successful calculation par else aur har situation mein finally execute hona chahiye.

# try:
#     num1 = int(input("Enter 1st number: "))
#     num2 = int(input("Enter 2nd number: "))

#     result = num1/num2
#     # print(result)

# except ValueError():
#     print('Please enter a valid number!!')

# except ZeroDivisionError():
#     print("A number can't be divisebl by 0!!")

# else:
#     print("Result =", result)

# finally:
#     print("calculated succesfully !!!")



# # Ek function create_profile(name, *skills, **details) banao. Name, 3 skills, age aur department pass karo. Saari details print karo.

# def create_profile(name, *skills, **details):

#     print("Name = ", name)

#     print("Skills :-")

#     for i in skills:
#         print(i)

#     print("Details :- ")

#     for keys, values in details.items():
#         print(keys, ":", values)

# create_profile(
#     "Abhinav",
#     "python", "fastAPI", "cloud",
#     age = 28,
#     department = "backend + cloud"
# )


# # calculator.py aur main.py naam ki do files banao. calculator.py mein add, subtract, multiply aur divide functions likho. main.py mein unhe import karke use karo. Dono files ka code submit karo.

