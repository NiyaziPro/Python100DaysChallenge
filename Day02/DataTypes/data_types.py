# Integer (int) - Whole numbers without decimals. Used for counting or indexing.
age = 25
print(type(age), age)  # Output: <class 'int'> 25

# Floating-point (float) - Numbers with decimal points. Used for precise measurements.
pi = 3.14
print(type(pi), pi)  # Output: <class 'float'> 3.14

# Complex (complex) - Numbers with real and imaginary parts. Used in advanced math.
z = 2 + 3j
print(type(z), z)  # Output: <class 'complex'> (2+3j)

# String (str) - Text data enclosed in quotes. Immutable.
name = "Alice"
print(type(name), name)  # Output: <class 'str'> Alice

# Boolean (bool) - True or False values. Used for conditions and logic.
is_adult = True
print(type(is_adult), is_adult)  # Output: <class 'bool'> True

# NoneType (None) - Represents absence of value or "nothing."
result = None
print(type(result), result)  # Output: <class 'NoneType'> None

# List (list) - Ordered, mutable collection of items (can be mixed types).
fruits = ["apple", "banana", "cherry"]
print(type(fruits), fruits)  # Output: <class 'list'> ['apple', 'banana', 'cherry']

# Tuple (tuple) - Ordered, immutable collection of items.
coordinates = (10, 20)
print(type(coordinates), coordinates)  # Output: <class 'tuple'> (10, 20)

# Set (set) - Unordered collection of unique items.
unique_numbers = {1, 2, 3, 3, 2}
print(type(unique_numbers), unique_numbers)  # Output: <class 'set'> {1, 2, 3}

#Dictionary (dict) - Collection of key-value pairs. Keys are unique.
person = {"name": "Bob", "age": 30}
print(type(person),person)  # Output: <class 'dict'> {'name': 'Bob', 'age': 30}
