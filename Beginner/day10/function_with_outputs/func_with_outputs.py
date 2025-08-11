# Function Returning a Single Value
# This function takes two arguments and returns their sum.
# The result is stored in a variable and printed.
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8


# Returning a String
# The function returns a formatted greeting string
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Output: Hello, Alice!


# Returning Multiple Values
# This function returns multiple values as a tuple.
# You can unpack them into separate variables.
def get_name_and_age():
    return "John", 25

name, age = get_name_and_age()
print(name)  # Output: John
print(age)   # Output: 25

# Return Early
# The return statement can be used conditionally to exit early based on logic.
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Cannot divide by zero.


# Using Return in an Expression
#  Returned values can be used directly in expressions or as function arguments.
def square(n):
    return n * n

print(square(4) + square(3))  # Output: 25


# Function That Returns Nothing (None)
#  If no return is used, Python returns None by default.
def say_hi():
    print("Hi!")

result = say_hi()
print(result)  # Output: None


# The .title() method is a string method in Python that returns a new string where
# the first character of each word is capitalized (uppercase),
# and all other characters in each word are lowercase.

text = "hello world from python"
new_text = text.title()
print(new_text)  # Output: "Hello World From Python"

# Important Notes
# It lowercases all other characters, so it might not work as expected with acronyms or special casing.
print("welcome to NASA".title())  # Output: "Welcome To Nasa" (⚠️ "NASA" becomes "Nasa")

# Comparison
# | Method          | Effect                                                 |
# | --------------- | ------------------------------------------------------ |
# | `.upper()`      | All characters uppercase                               |
# | `.lower()`      | All characters lowercase                               |
# | `.capitalize()` | Only first character of the entire string is uppercase |
# | `.title()`      | First character of **each word** is uppercase          |