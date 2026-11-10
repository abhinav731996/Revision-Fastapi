# --------------- for loop -----------------

# # for numbers

# for i in range (1,6):
#     print(i)


# # for lists
# employees = ["Rahul", "Priya", "Amit", "Neha"]

# for i in employees:
#     print(i)




# ----------------- while loop ---------------

# count = 1

# while count <= 5:
#     print(count)
#     count+=1




# ---------------- functions -------------

# def greet():
#     print("Welcome to the revision!!!!!")

# greet()


# ----------------- parameters with functions ----------------

# def greet(name):
#     print("Welcome to the world", name)

# greet("Abhinav")
# greet("Sahil")



# ----------------- return statements ---------------

# def add(a,b):
#     return a + b

# result = add(3,2)

# print(result)




# ------------------ 

# def get_employee():
#     return{
#         "name" : "Abhinav",
#         "age" : 29 
#     }

# employee = get_employee()

# print(employee["name"])
# print(employee["age"])






# ============================ Practice =============================

# --------------------- 1 ------------------------
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# if age >= 18:
#     print(name, "your are eligible for registration!!")

# else:
#     print(name, "your are not eligible for registration!!!!!!")


# ----------------------- 2 --------------------------
# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)


# ------------------------ 3 -------------------------
# salary = int(input("Enter your salary: "))
# bonus = int(input("Enter ypur bonus: "))

# def calculate_salary(a,b):
#     return a + b

# total_salary = calculate_salary(salary,bonus)

# print("Total salary = ", total_salary)


# ----------------------- 4 ---------------------------

num = int(input("Enter number: "))

def check_num(a):
    if a > 0:
        return print("Positive!!")

    elif a < 0:
        return print("Negative!!")

    else:
        return print("Zero!!!!!")

result = check_num(num)

print(result)