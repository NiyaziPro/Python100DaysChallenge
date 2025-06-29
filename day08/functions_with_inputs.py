# In Python, functions can receive data from the caller using parameters (or inputs).
# These values are used inside the function to perform operations.

# Basic Syntax
def function_name(parameter1, parameter2):
    print(parameter1, parameter2)  # for example


# when you call the function, you pass actual values called arguments:
function_name("Alice", 30)


# Simple function with one input
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")  # Output: Hello, Alice!


# Function with multiple inputs
def add(x, y):
    print(x + y)


add(9, 6)  # Output: 15

# Key Concepts
# 1. Parameters -> Placeholders inside function definition
# 2. Arguments  -> Actual values passed when calling the function

# Positional vs Keyword arguments
# Positional (order matters)
def describe(name,age):
    print(f"{name} is {age} years old.")
describe("Ali",33) # Output: Ali is 33 years old.
#Keyword (order doesn't matter)
describe(age=35,name="Alex") # Output: Alex is 35 years old.

# Default parameters
def greet(name="Guest"):
    print(f"Hi, {name} :)")
greet()             # Output: Hi, Guest :)
greet("Stanley")    # Output: Hi, Stanley :)
