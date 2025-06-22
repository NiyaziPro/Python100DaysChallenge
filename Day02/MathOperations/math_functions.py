# Advanced math functions

# Function	    Use	                            Example
# abs(x)	    Absolute value	                abs(-10) → 10
# round(x)	    Round to nearest integer	    round(3.6) → 4
# pow(x, y)	    Power (x^y)	                    pow(2, 3) → 8
# divmod(x,y)	Returns (quotient, remainder)	divmod(9, 4) → (2, 1)

import math

print(math.sqrt(16))       # Square root: 4.0
print(math.floor(3.7))     # Floor (down): 3
print(math.ceil(3.1))      # Ceil (up): 4
print(math.pi)             # 3.141592...
print(math.factorial(5))   # 120
print(math.log(100, 10))   # 2.0 (log base 10)


# Type Conversions in Math - Mathematical operations between int and float will automatically promote to float.
x = 3
y = 2.0
print(x + y)  # 5.0 (float)

# Best Practices
# Use parentheses for clarity in complex expressions.
# Prefer math.pow() or ** for powers.
# Be mindful of / vs // when you want integer vs float.
# Use round() with 2nd argument to control decimal places:
print(round(3.14159, 2))  # 3.14
