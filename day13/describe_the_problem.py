from random import randint


def my_function():
    for i in range(1, 20):  # false -> should be range(1, 21)
        if i == 20:
            print("You got it")


# range - range(stop) -> range object range(start, stop[, step]) -> range object
# Return an object that produces a sequence of integers from start (inclusive)
# to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1.
# start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3.
# These are exactly the valid indices for a list of 4 elements.
# When step is given, it specifies the increment (or decrement).
my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?


# Reproduce the Bug

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)  # false -> should be randint(0, 5)
print(dice_images[dice_num])



year = int(input("What's your year of birth?\n"))

if 1980 < year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Generation Z.")
