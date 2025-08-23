# Docstrings (short for documentation strings) are multi-line string literals
# used to document Python modules, classes, functions, or methods.
# They explain what a block of code does, making your code easier to understand
# for others — and for your future self.

# A docstring is placed immediately after the definition of a function, class, or module, using triple quotes:
def greet(name):
    """Return a friendly greeting with the given name."""
    return f"Hello, {name}!"

print(greet("Nik"))
# Unlike regular comments (#), docstrings are stored as metadata and can be accessed with help() or .__doc__.


def multiply(x, y):
    """
    Multiply two numbers and return the result.

    Args:
        x (int or float): First number.
        y (int or float): Second number.

    Returns:
        int or float: Product of x and y.
    """
    return x * y

print(multiply.__doc__)

# Or interactively
help(multiply)

# Docstring vs Comment
# | Feature      | Docstring             | Comment                    |
# | ------------ | --------------------- | -------------------------- |
# | Syntax       | Triple quotes (`"""`) | Hash symbol (`#`)          |
# | Stored?      | Yes (`.__doc__`)      | No                         |
# | Purpose      | Document code blocks  | Explain code logic briefly |
# | Used By IDEs | Yes                   | Sometimes                  |