# for Loop — Iterating Over a Sequence

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# The loop runs once for every item in fruits.
# Each iteration assigns the next item to fruit, then prints it.

# for Loop with range() — Looping a Specific Number of Times
for i in range(5):  # i goes from 0 to 4
    print(f"Iteration {i}")
# range(5) generates numbers 0,1,2,3,4.
# The loop runs 5 times, printing the iteration number each time.

# for Loop with enumerate() — Get Index and Value
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Color {index} is {color}")
# enumerate() returns pairs (index, item).
# This helps when you need the item’s position.

# while Loop — Repeat Until Condition False
count = 0

while count < 5:
    print(f"Count is {count}")
    count += 1  # Increment count to avoid infinite loop
# Loop continues as long as count is less than 5.
# The variable count is increased each time.
# When count reaches 5, the loop stops.

# break — Exit Loop Early
for num in range(10):
    if num == 5:
        print("Reached 5, stopping loop.")
        break  # Exit loop immediately
    print(num)
# The loop prints numbers until num equals 5, then breaks out.

# continue — Skip Current Iteration
for num in range(5):
    if num == 2:
        print("Skipping 2")
        continue  # Skip rest of loop body for num==2
    print(num)
# When num is 2, it prints a message and skips printing 2 itself.

# else Clause on Loops
for i in range(3):
    print(i)
else:
    print("Loop finished without break")

print("---")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Won't print this because loop broke early")

# The else after a loop runs only if no break occurred.
# In the first loop, no break happens, so the message prints.
# In the second, break occurs when i==3, so else is skipped.


# Nested Loops — Loop Inside a Loop
for i in range(1, 4):      # Outer loop
    for j in range(1, 3):  # Inner loop
        print(f"i={i}, j={j}")
# For each iteration of i, the inner loop runs completely over j.
# Outputs pairs of i and j values.

# Looping Over a Dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")
# .items() returns key-value pairs from the dictionary.
# Loop prints each pair.

# Infinite Loop Example (with while)
while True:
    response = input("Type 'exit' to stop: ")
    if response == 'exit':
        break
# while True loops forever until break is executed.
# Useful for interactive prompts or waiting for a specific event.