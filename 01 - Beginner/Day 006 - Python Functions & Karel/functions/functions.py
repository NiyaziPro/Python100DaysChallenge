# Basic functions
def greet():
    print("Hello, welcome to Python!")


greet()


# Function with Parameter
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# Function with Return Value
def square(number):
    return number * number


result = square(5)
print(result)  # Output: 25


# Multiple Parameters
def add(a, b):
    return a + b


print(add(3, 4))  # Output: 7


# Default Parameters
def greet(name="Stranger"):
    print(f"Hello, {name}!")


greet()  # Output: Hello, Stranger!
greet("Emma")  # Output: Hello, Emma!


# Keyword Arguments
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")


describe_pet(name="Buddy", animal="dog")


# Arbitrary Positional Arguments – *args
def add_numbers(*numbers):
    total = sum(numbers)
    print(f"Total: {total}")


add_numbers(1, 2, 3, 4)  # Output: Total: 10


# Returning Multiple Values
def min_max(numbers):
    return min(numbers), max(numbers)


lowest, highest = min_max([4, 2, 9, 1])
print(lowest, highest)  # Output: 1 9

# Lambda Function
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12


# Function Inside Function ( Nested )
def outer():
    def inner():
        print("This is the inner function.")

    inner()


outer()

# Variable Scope
x = 10  # global


def show():
    x = 5  # local
    print("Inside x = ", x)


show()  # Inside: 5
print("Outside x = ", x)  # Outside: 10


# Mutable Default Argument ( Avoid This )
def add_item(item, item_list=[]):  # BAD PRACTICE
    item_list.append(item)
    return item_list


print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b'] — reuses the same list!


# Correct way:
def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list


# Docstring Example
def square(n):
    """Returns the square of a number."""
    return n ** 2


print(square.__doc__)
print(square(5))


# First-Class Function
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def speak(func):
    return func("Hello")


print(speak(shout))  # HELLO
print(speak(whisper))  # hello
