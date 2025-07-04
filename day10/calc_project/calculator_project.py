from day10.calc_project import calc_art
from utils import colors


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        print(colors.red + "You can not divide by zero! Please select other number!" + colors.reset)
        return 0
    else:
        return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(calc_art.logo)
    should_accumulate = True
    first_number = float(input("What's the first number?\n"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
            should_accumulate = True
        else:
            should_accumulate = False
            print(colors.red + "Invalid Operator!" + colors.reset)
            calculator()
        next_number = float(input("What's the next number?\n"))

        answer = operations[operation](first_number, next_number)

        print(f"{first_number} {operation} {next_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_number = answer
        else:
            should_accumulate = False
            calculator()


calculator()
