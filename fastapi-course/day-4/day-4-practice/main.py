from calculator import add_cal, sub_cal, div_cal, multi_cal;

try:

    addition = add_cal(5,7,8,2,6)

    subtraction = sub_cal(5,7,8,2,6)

    multiply = multi_cal(2,4)

    division = div_cal(8,2)

except ValueError:
    print("enter valid number ")

except ZeroDivisionError:
    print("can not be divisibale by 0")

else:
    print(addition)
    print(subtraction)
    print(multiply)
    print(division)

finally: 
    print("calculation successfully !!")