# Python does not have traditional block scope like some other languages (e.g., Java, C, or JavaScript).
# In many languages, variables declared inside blocks (like inside if, for, or while) are only accessible within that block. This is called block-level scope.

# But in Python, blocks like: if / for / while / try / with  -  do not create a new scope.

# Example (Python doesn't block scope):
if True:
    x = 10  # declared inside an if block

print(x)  # ✅ This will print 10

# In other languages like Java:
# if (true) {
#     int x = 10;
# }
# System.out.println(x);  // ❌ Error: x is not defined


# Python emphasizes readability and a flat structure.
# Since blocks are part of code readability but not scope isolation, Python doesn’t isolate their variables.

for i in range(3):
    pass

print(i)  # i is still accessible here
# So variables inside loops or conditionals will "leak" into the outer scope — unlike in many other languages.
