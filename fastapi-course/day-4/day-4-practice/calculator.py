
def add_cal(*args):
    return sum(args)


# -----------------------------------------------------

def sub_cal(*args):

    if not args:
        return 0

    total = args[0]

    for number in args[1:]:
        total -= number

    return total


# ---------------------------------------------------

def div_cal(num1, num2):
    return num1/num2




# ----------------------------------------------------

def multi_cal(num1, num2):
    return num1 * num2
