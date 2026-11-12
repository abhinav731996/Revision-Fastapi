# Python Day 4 – Functions, Exception Handling, Modules & Packages

# # 1. *args – Multiple positional arguments ==============================================

# def calculate_salary(salary1, salary2, salary3):
#     total_salary = salary1 + salary2 + salary3
#     return total_salary

# result = calculate_salary(20000,45000,55000)

# print(result)

# # Lekin maan lijiye company mein 10 employees hain. Kya hum function mein 10 parameters banayenge?

# def calculate_salary(*args):

#     total = 0

#     for salary in args:
#         total += salary

#     return total

# result = calculate_salary(52000, 45000, 56000, 57000)

# print("total salary = ", result)


# # **kwargs – Multiple keyword arguments ==========================

# def employee_details(**kwargs):
#     print("name: ", kwargs["name"])
#     print("salary: ", kwargs["salary"])
#     print("age: ", kwargs["age"])
#     print("department: ", kwargs["department"])


# employee_details(
#     name = "Abhinav",
#     salary = 55000,
#     age = 30,
#     department = "IT"
# )

# employee_details(
#     name = "Sahil",
#     salary = 35000,
#     age = 30,
#     department = "IT"
# )


# # *args aur **kwargs ek saath ====================================

# def emp_details(name, *skills, **details):

#     print("employee name: ", name)

#     print("skills: ")

#     for i in skills:
#         print(i)

#     print("other details")

#     for key, values in details.items():
#         print(key, ":", values)


# emp_details(
#     "abhinav",
#     "python",
#     "fastAPI",
#     age = 29,
#     salary = 55000,
#     department = "backend + cloud"
# )



# # Exception Handling – try, except, else, finally ======================

# num1 = int(input("enter 1st number: "))
# num2 = int(input("enter 2nd number: "))

# result = num1/num2

# print(result)

# # Is code mein do problems ho sakti hain:
# # 1. User number ki jagah "hello" enter kar de.
# # 2. User second number 0 enter kar de.


try:
    num1 = int(input("enter 1st number: "))
    num2 = int(input("enter 2nd number: "))

    result = num1/num2

    print(result)

except ValueError:
    print("Please enter a valid number !!!")

except ZeroDivisionError:
    print("Number should not be zero !!!")

# else:
#     print("result: ", result)
#     print("Calculated successfully!!")

# finally:
#     print("progrem execute successfully !!")



# try:
#     # Risky code

# except ValueError:
#     # Handle ValueError

# except ZeroDivisionError:
#     # Handle ZeroDivisionError

# else:
#     # Execute when no error occurs

# finally:
#     # Cleanup code