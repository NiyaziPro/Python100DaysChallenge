# Type Error
# Happens when you try to use incompatible data types together.
print("Age: " + 25)  # TypeError: can't concatenate str and int

# Type Checking - Checking the type of variable before using it.
x = 10
if isinstance(x, int):
    print("x is an integer")

print(type(x)) # <class 'int'>


# Type Conversion - Changing a value from one type to another (casting).
num_str = "100"
num_int = int(num_str)
print(num_int + 20)  # Output: 120

print(type(num_str)) # Output: <class 'str'>
print(type(num_int)) # Output: <class 'int'>