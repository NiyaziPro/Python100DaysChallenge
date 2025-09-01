# A dictionary is a collection of key-value pairs. It’s like a real-world dictionary
# where you look up a word (key) and get its meaning (value). In Python:
# Keys must be unique and immutable (strings, numbers, tuples).
# Values can be any data type (including other dictionaries).

# Creating a Dictionary
student = {
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "Physics"],
}

# Accessing Values
# Use keys to get values:
print(student["name"])  # Alice
print(student["age"])  # 22
# Or use .get() which returns None or a default if key not found:
print(student.get("name"))  # Alice
print(student.get("grade", "N/A"))  # N/A (default)

# Adding or Updating Items
student["grade"] = "A"  # Add new key-value
student["age"] = 23  # Update existing key


# Removing Items
student.pop("age")  # removes 'age' key
# student.popitem() # removes last inserted key-value pair
del student["grade"]  # deletes key-value pair

# Looping Through Dictionaries
# Loop keys:
for key in student:
    print(key)

# Loop values:
for value in student.values():
    print(value)

# Loop key-value pairs:
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary Methods
# | Method          | Description                                                               |
# | --------------- | ------------------------------------------------------------------------- |
# | `dict.clear()`  | Removes all items                                                         |
# | `dict.copy()`   | Returns a shallow copy                                                    |
# | `dict.keys()`   | Returns all keys                                                          |
# | `dict.values()` | Returns all values                                                        |
# | `dict.items()`  | Returns all key-value pairs                                               |
# | `dict.update()` | Updates dictionary with another dictionary or iterable of key-value pairs |

# Nesting dictionaries - Dictionaries can contain other dictionaries:
students = {
    "s1": {"name": "Ali", "age": 25},
    "s2": {"name": "Veli", "age": 30}
}

print(students["s1"]["name"])  # Ali

# Immutability of Keys - Keys must be immutable:
students = {
    "s1": {"name": "Ali", "age": 25},
    "s2": {"name": "Veli", "age": 30}
}

print(students["s1"]["name"])  # Ali

# Dictionary Comprehension - Create dictionaries using comprehension:
squares = {x: x * x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
