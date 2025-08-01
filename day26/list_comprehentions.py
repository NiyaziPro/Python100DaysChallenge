numbers = [1, 2, 3, 4, 5]
new_list = [number + 1 for number in numbers]
print(new_list)

name = "Nikko"
letters = [letter for letter in name]
print(letters)

num = range(1, 5)
new_num = [n + n for n in num]
print(new_num)

range_list = [digit * 2 for digit in range(1, 6)]
print(range_list)

names = ["Alex", "Fati", "Caroline", "Jack", "Eleanor", "Alice"]

short_names = [name for name in names if len(name) < 5]
print(short_names)
