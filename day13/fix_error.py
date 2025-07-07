from utils import colors

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))
if age >= 18:
    print(f"You can drive at age {age}.")


# Problematic Code
# def average(numbers):
#     return sum(numbers) / len(numbers)
# print(average([]))  # This causes ZeroDivisionError


def average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return colors.red + "Error: Cannot divide by zero. The list is empty." + colors.reset

print(average([]))          # Output: Error message
print(average([2, 4, 6]))   # Output: 4.0
