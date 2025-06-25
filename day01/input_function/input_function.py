#The input() function in Python is used to get user input from the console.
name = input("What is your name? ")
print("Hello", name)
#It always returns a string (str type).
#Whatever the user types becomes the value of the variable.

#Basic Behavior
data = input("Type something: ")
print(type(data)) # <class 'str'>

#Type Conversion (Converting input_function) - You must convert input if you want an integer or float:
age = int(input("Enter your age: ")) # int() for integers
height = float(input("Enter your height in meters: ")) #float() for decimal numbers
#⚠️ If the user types something invalid, it causes an error.


#Handling Invalid input_function (Try-Except) - Useful for preventing crashes.
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Oops! That's not a number.")


#Stripping Extra Spaces - Sometimes users type with spaces by accident. Use .strip():
username = input("Username: ").strip()
#strip() removes both leading and trailing spaces.
# You can also use:
# .lstrip() → removes only left spaces
# .rstrip() → removes only right spaces


#Check for Empty input_function
user_input = input("Enter something: ").strip()
if not user_input:
    print("You didn’t type anything!")

#Hidden input_function (Passwords) - Use getpass for hidden input, like passwords:
from getpass import getpass
password = getpass("Password: ") #It hides what the user types.

#Multiple Inputs in One Line - Use split() to handle several inputs:
x, y = input("Enter two values: ").split()
#Gives you two strings. To convert to numbers:
a, b = map(int, input("Enter two numbers: ").split())

#Get a List from input_function
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
#input_function: 5 10 15   Output: [5, 10, 15]


#Loop Until Valid input_function - Useful in games, quizzes, and interactive apps.
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid! Try again.")


#input_function with Default Values - If the user presses Enter without typing, it uses "John"
name = input("Enter your name [default: John]: ") or "John"

#Evaluate Math Expressions (Dangerous!) - ⚠️ Never use eval() with user input in real-world applications — it’s dangerous.
result = eval(input("Enter math expression: ")) #input_function: 5 + 2 * 3   Output: 11


#Unicode input_function (Multilingual) - Works well with Turkish, Arabic, Cyrillic, Japanese, etc.
isim = input("İsmin nedir? ")
print("Merhaba", isim)


#Choice Inputs - .lower() helps ignore case sensitivity (Y, y, YES...).
answer = input("Do you agree? (y/n): ").lower()
if answer == 'y':
    print("You agreed.")

#Reusable input_function Function - You can define your own smart input function:
def ask_int(prompt="Enter an integer: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not an integer.")

#Usage:
age = ask_int("How old are you? ")

