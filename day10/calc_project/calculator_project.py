from day10.calc_project import calc_art
from utils import colors

print(calc_art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        print(colors.red + "You can not divide by zero! Please select other number!" + colors.reset)
        return None
    else:
        return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_number = float(input("What's the first number?\n"))
operation = input("+\n-\n*\n/\nPick an operation: ")
next_number = float(input("What's the next number?\n"))

print(operations.get("+")(first_number,next_number))
