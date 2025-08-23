# Task - Love Calculator

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.
#
# e.g.
# name1 = "John Doe" name2 = "Alice Bauer"
#
# T occurs 0 times
# R occurs 1 time
# U occurs 1 times
# E occurs 3 times
# Total = 5
#
# L occurs 1 time
# O occurs 2 times
# V occurs 0 times
# E occurs 3 times
# Total = 6
#
# Love Score = 56
#
# Example Input
# calculate_love_score("John Doe", "Alice Bauer")
#
# Example Output
# 42

def calculate_love_score(name1, name2):
    names_char_list = [c.upper() for c in name1 + name2]
    total1 = 0
    total2 = 0
    for letter in "TRUE":
        count = names_char_list.count(letter)
        print(f"{letter} occurs {count} times")
        total1 += count

    for letter in "LOVE":
        count = names_char_list.count(letter)
        print(f"{letter} occurs {count} times")
        total2 += count

    print(total1, total2, sep="")


calculate_love_score("John Doe", "Alice Bauer")