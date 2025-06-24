# The 3 Logical Operators in Python
# | Operator | Name | Meaning                                                |
# | -------- | ---- | ------------------------------------------------------ |
# | `and`    | AND  | True if **both** conditions are true                   |
# | `or`     | OR   | True if **at least one** is true                       |
# | `not`    | NOT  | **Inverts** the condition (True → False, False → True) |


# and Operator
# Returns True only if both conditions are true.
age = 25
has_id = True

if age >= 18 and has_id:
    print("Access granted.")
# Both age >= 18 and has_id must be true.
# If either is false, access is denied.


# or Operator
# Returns True if at least one condition is true.
is_admin = False
is_editor = True

if is_admin or is_editor:
    print("You can edit the content.")
# Only one role is enough to allow editing.

# not Operator
# Reverses the result of a condition.
logged_in = False

if not logged_in:
    print("Please log in.")
# not False becomes True, so the message is shown.

# Multiple logical operators together
age = 17
has_permission = True

if age >= 18 or has_permission:
    print("You may enter.")
# Even though the age condition is false, the permission is true — so the overall result is true.


#  Truth Table Summary
# | A     | B     | A and B | A or B |
# | ----- | ----- | ------- | ------ |
# | True  | True  | True    | True   |
# | True  | False | False   | True   |
# | False | True  | False   | True   |
# | False | False | False   | False  |