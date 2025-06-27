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
print(result) # Output: 25