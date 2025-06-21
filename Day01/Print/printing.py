# In Python, to show text on the screen, you use the print() function.
print("Hello world!")
# The print() function takes a value (or values) and prints them to the console.
# Text should be inside quotes: either "double" or 'single'.

# print multiple things at once by separating them with commas:
print("My name is ", 'Alice')

# print numbers directly (without quotes):
print(45)

# Some characters can't be typed directly into a string — like newlines or quotes. Use escape characters:
# | Escape | Meaning      | Example                      |
# | ------ | ------------ | ---------------------------- |
# | `\n`   | New line     | `print("Hello\nWorld")`      |
# | `\t`   | Tab (indent) | `print("Hello\tWorld")`      |
# | `\"`   | Double quote | `print("She said: \"Hi!\"")` |
# | `\\`   | Backslash    | `print("C:\\Users\\Name")`   |

print("Hello\nWorld")
print("Hello\tWorld")
print("She said: \"Hi!\"")
print("C:\\Users\\Name")

# The print() function has special arguments:
# sep – separator between values
print("Python", "Java", "C++", sep=" | ")
# end – what to print after the line
print("Loading", end="...")
print("Done!")

# print variables too:
name = "Alice"
age = 25
print("Name:", name)
print("Age:", age)

# Formatted Strings (f-strings) - Modern Python allows f-strings for cleaner formatting:
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Printing Emojis & Unicode - Python supports Unicode, so you can print emojis too:
print("I love Python ❤️")
print("\U0001F600")  # 😀
print("Heart: \u2764")  # ❤️

# file parameter - This lets you write to files instead of the screen:
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)

# flush Parameter - Used to force writing to a file or console without buffering:
import time

print("Loading", end="", flush=True)
time.sleep(2)
print("...Done!")
# Without flush=True, some systems might delay showing output.


# Print in Loops and Conditional Logic
for i in range(1, 6):
    print(f"{i} squared is {i ** 2}")

if True:
    print("Yes!")
else:
    print("No!")


#Print vs Return
#| `print()`                     | `return`                         |
#| ----------------------------- | -------------------------------- |
#| Displays output to the screen | Sends value back from a function |
#| Doesn't affect program logic  | Controls program flow            |
def add(x, y):
    return x + y

result = add(2, 3)
print(result)  # Displays the returned value

