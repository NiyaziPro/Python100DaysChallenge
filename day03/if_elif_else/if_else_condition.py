# if Statement
# Executes a block only if the condition is true.
age = 18
if age >= 18:
    print("You are an adult.")
# Note: The condition uses a comparison (>=) and ends with a colon :. The indented part is the block that runs if true.

# if-else Statement
# If the condition is true, do the first block. Otherwise, do the second.
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else (Multiple Conditions)
# Use elif (short for else if) to check multiple conditions in order.
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")
#Python checks each if/elif in order and stops at the first match.


# Comparison Operators
# Used to create conditions:
# | Operator | Meaning          | Example  |
# | -------- | ---------------- | -------- |
# | `==`     | Equal to         | `a == b` |
# | `!=`     | Not equal to     | `a != b` |
# | `>`      | Greater than     | `a > b`  |
# | `<`      | Less than        | `a < b`  |
# | `>=`     | Greater or equal | `a >= b` |
# | `<=`     | Less or equal    | `a <= b` |


# Logical Operators
# You can combine multiple conditions with:
# and: both conditions must be true
# or: at least one must be true
# not: inverts the condition
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted.")


#  Nesting Conditionals
# You can put if statements inside other if blocks.
age = 20
if age >= 18:
    if age >= 65:
        print("Senior")
    else:
        print("Adult")


# Short if Expression (Ternary Operator)
# A one-line conditional assignment:
is_logged_in = True
status = "Welcome!" if is_logged_in else "Please log in"
print(status)
