# Namespace is a container where names are mapped to objects (variables, functions, classes, etc.).
# It ensures that names are unique and don't conflict with one another.
# Think of it as a dictionary:
# { name (str): object (value/reference) }

# Types of Namespaces in Python
# Python manages several namespaces at different levels:

# | Namespace Type | When It Exists                 | Example Contents                |
# | -------------- | ------------------------------ | ------------------------------- |
# | **Built-in**   | Always available               | `len`, `print`, `int`, etc.     |
# | **Global**     | When a module/script is loaded | Top-level variables & functions |
# | **Enclosing**  | In nested functions            | Outer function’s local names    |
# | **Local**      | Inside a function/method       | Function parameters, local vars |


x = 10  # Global namespace

def outer():
    y = 20  # Enclosing namespace

    def inner():
        z = 30  # Local namespace
        print(x, y, z)

    inner()

outer()
# Behind the scenes, Python checks these namespaces in the LEGB order (Local → Enclosing → Global → Built-in).

# Accessing a Namespace
# Python provides built-in functions to inspect namespaces:

# globals() → Returns a dictionary of global names
# locals() → Returns a dictionary of local names
# dir() → Lists the names in the current namespace
print(globals())
print(locals())
print(dir())

# Why Are Namespaces Important?
# Avoid name collisions (e.g., sum as a variable vs the built-in sum())
# Improve modularity (you can have my_function() in multiple modules)
# Enable encapsulation (data hiding in classes/functions)


# Module & Class Namespaces
# Every module and class in Python has its own namespace.
import math
print(math.pi)  # Accessing name 'pi' from math module's namespace


# Common Issues
# Accidentally overriding built-in names:
list = [1, 2, 3]  # Now you can’t use list() as a function
# Variable shadowing between local/global/enclosing scopes