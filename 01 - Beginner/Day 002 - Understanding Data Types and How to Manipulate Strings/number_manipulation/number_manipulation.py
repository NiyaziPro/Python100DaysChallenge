import math

# Absolute Value - Removes the sign of a number.
x = -42
print(abs(x))  # Output: 42

# Rounding Numbers - round to the nearest whole number or a set number of decimal places.
print(round(3.14159))       # 3
print(round(3.14159, 2))    # 3.14

# Floor and Ceiling
# math.floor() rounds down
# math.ceil() rounds up
print(math.floor(4.7))  # 4
print(math.ceil(4.1))   # 5

# Square Root, Power, and Logarithm
print(math.sqrt(16))       # 4.0
print(math.pow(2, 3))      # 8.0
print(math.log(100, 10))   # 2.0

# Modulo and Divmod
# Modulo gives the remainder
# divmod() gives both quotient and remainder
print(10 % 3)          # 1
print(divmod(10, 3))   # (3, 1)

# Type Conversion - Convert between int, float, and str types:
x = 5.9
print(int(x))      # 5
print(float(3))    # 3.0
print(str(123))    # '123'

# Negative to Positive (and vice versa)
n = -10
print(abs(n))     # 10
p = 7
print(-p)         # -7

# Truncation (remove decimal part)
print(math.trunc(4.999))  # 4

# Clamp a value between limits (manual) - Keep a number in a range:
value = 150
min_val = 0
max_val = 100

clamped = max(min_val, min(value, max_val))
print(clamped)  # 100

# Formatting Numbers
# Format for user-friendly output:
n = 12345.6789

print(f"{n:.2f}")         # 12345.68
print(f"{n:,.2f}")        # 12,345.68
print(f"{n:08.2f}")       # 012345.68


