# In Python, to show text on the screen, you use the printing() function.
print("Hello world!")
# The printing() function takes a value (or values) and prints them to the console.
# Text should be inside quotes: either "double" or 'single'.

# printing multiple things at once by separating them with commas:
print("My name is ", 'Alice')

# printing numbers directly (without quotes):
print(45)

# Some characters can't be typed directly into a string — like newlines or quotes. Use escape characters:
# | Escape | Meaning      | Example                      |
# | ------ | ------------ | ---------------------------- |
# | `\n`   | New line     | `printing("Hello\nWorld")`      |
# | `\t`   | Tab (indent) | `printing("Hello\tWorld")`      |
# | `\"`   | Double quote | `printing("She said: \"Hi!\"")` |
# | `\\`   | Backslash    | `printing("C:\\Users\\Name")`   |

print("Hello\nWorld")
print("Hello\tWorld")
print("She said: \"Hi!\"")
print("C:\\Users\\Name")

# The printing() function has special arguments:
# sep – separator between values
print("Python", "Java", "C++", sep=" | ")
# end – what to printing after the line
print("Loading", end="...")
print("Done!")

# printing variables too:
name = "Alice"
age = 25
print("Name:", name)
print("Age:", age)

# Formatted Strings (f-strings) - Modern Python allows f-strings for cleaner formatting:
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Printing Emojis & Unicode - Python supports Unicode, so you can printing emojis too:
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


# printing in Loops and Conditional Logic
for i in range(1, 6):
    print(f"{i} squared is {i ** 2}")

if True:
    print("Yes!")
else:
    print("No!")


#printing vs Return
#| `printing()`                     | `return`                         |
#| ----------------------------- | -------------------------------- |
#| Displays output to the screen | Sends value back from a function |
#| Doesn't affect program logic  | Controls program flow            |
def add(x, y):
    return x + y

result = add(2, 3)
print(result)  # Displays the returned value

