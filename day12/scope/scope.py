# Scope refers to the region of a program where a variable is defined and can be accessed.
# It determines the visibility and lifetime of variables in your Python code.
# Python determines the scope of a variable using the LEGB rule —
# which defines the hierarchy in which Python looks for variables:

# Local — inside the current function
#
# Enclosing — inside enclosing (outer) functions
#
# Global — top-level of the script or module
#
# Built-in — Python’s built-in names (e.g., len, sum, etc.)


# Local Scope
# Variables defined inside a function — only accessible within that function.
def greet():
    name = "Alice"  # Local scope
    print(name)

greet()
# print(name)  ❌ Error: name is not defined outside


#  Enclosing Scope
# Variables in the outer function of a nested function.
def outer():
    x = "outer"

    def inner():
        print(x)  # Can access enclosing scope

    inner()

# Global Scope
# Defined at the top level of a script/module. Accessible from any function unless shadowed.
language = "Python"  # Global scope

def speak():
    print(language)  # Access global variable

speak()


# Built-in Scope
# Python’s built-in functions and constants are always available.
print(len("hello"))  # len is built-in


# Scope Modifiers
# global
# Used to modify a global variable inside a function.
counter = 0

def increment():
    global counter
    counter += 1

# nonlocal
# Used inside nested functions to modify variables in the enclosing scope (not global).
def outer():
    x = 0

    def inner():
        nonlocal x
        x += 1


# Trying to modify a global variable inside a function without global — leads to UnboundLocalError.
# Using the same variable name in different scopes — can lead to confusion.

