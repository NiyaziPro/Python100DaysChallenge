# The modulo operator % returns the remainder when one number is divided by another.
# Syntax : remainder = a % b

print(10 % 3)   # 1  → 10 divided by 3 is 3 with a remainder of 1
print(20 % 5)   # 0  → 20 is evenly divisible by 5
print(7 % 4)    # 3

# Check if a number is even or odd
number = int(input("Enter number :\n"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Check divisibility
if number % 5 == 0:
    print("This number is divisible by 5")

# Looping patterns or wrapping around
# Used in games or graphics:
number = (number + 1) % 5  # Cycles between 0–4

# Rounding behavior with negatives
print(-7 % 3)  # Output: 2 → Python always returns a non-negative remainder


# Modulo vs Division
# | Operation      | Operator | Result for `10 ÷ 3` |
# | -------------- | -------- | ------------------- |
# | Division       | `/`      | `3.333...` (float)  |
# | Floor Division | `//`     | `3` (int)           |
# | Modulo         | `%`      | `1` (remainder)     |