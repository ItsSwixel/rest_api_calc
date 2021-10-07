def addition(val1, val2):
    return val1 + val2


def subtraction(val1, val2):
    return val1 - val2


def multiplication(val1, val2):
    return val1 * val2


def division(val1, val2):
    if val1 != 0 and val2 != 0:
        return val1 / val2
    else:
        return "Division by zero exception"
