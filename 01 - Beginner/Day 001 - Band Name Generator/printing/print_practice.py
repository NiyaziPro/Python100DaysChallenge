# Task - printing your name, age, and hobby using f-string.
name = "Nikko"
age = 25
hobby = "Fishing"
print(f"My name is {name} and I'm {age} years old. My hobby is {hobby}.")



#Task - Write a loop that prints a loading bar:
#Loading: [#####     ] 50%

import time

for i in range(0, 101, 10):  # From 0 to 100 in steps of 10
    hashes = "#" * (i // 10)             # Filled part
    spaces = " " * ((100 - i) // 10)     # Unfilled part
    print(f"\rLoading: [{hashes}{spaces}] {i}%", end="", flush=True)
    time.sleep(0.3)  # Delay for animation effect

print("\nDone!")
