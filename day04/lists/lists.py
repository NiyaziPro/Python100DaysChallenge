# List - https://docs.python.org/3.13/tutorial/datastructures.html

# Creating a List
fruits = ["apple", "banana", "cherry"]
print(fruits)
# This creates a list of strings. The items are ordered and indexed:
# fruits[0] → "apple"
# fruits[1] → "banana"

# Accessing Items -  We can use both positive and negative indexing.
print(fruits[1])      # Output: banana
print(fruits[-1])     # Output: cherry (last item)

# Modifying an Item - Lists are mutable, so items can be changed directly by index.
fruits[0] = "mango"
print(fruits)         # ['mango', 'banana', 'cherry']

# Adding Items:
# append() – Add to end
fruits.append("orange")
print(fruits)         # ['mango', 'banana', 'cherry', 'orange']

# insert() – Add at specific position
fruits.insert(1, "kiwi")
print(fruits)         # ['mango', 'kiwi', 'banana', 'cherry', 'orange']

# extend() – Add another list
more_fruits = ["grape", "pineapple"]
fruits.extend(more_fruits)
print(fruits)

# Removing Items
#  remove() – Remove by value
fruits.remove("banana")
print(fruits)

# pop() – Remove by index or last
last_item = fruits.pop()
print("Removed:", last_item)

# del – Delete by index
del fruits[0]

# clear() – Empty the list
fruits.clear()

# Checking if an Item Exists
if "apple" in fruits:
    print("Apple is in the list")
else:
    print("Apple is not in the list")

# Iterating Over a List
for fruit in fruits:
    print(fruit)

# Sorting and Reversing
numbers = [5, 2, 9, 1]
numbers.sort()           # Ascending
print(numbers)           # [1, 2, 5, 9]

numbers.sort(reverse=True)  # Descending
print(numbers)              # [9, 5, 2, 1]

numbers.reverse()        # Reverse order (not sorting!)


# Getting Length
print(len(fruits))   # Number of items in the list

# Slicing a List
print(fruits[1:3])    # Items from index 1 to 2
print(fruits[:2])     # First two items
print(fruits[-2:])    # Last two items

# Nested Lists - Lists can contain other lists — helpful in matrices or complex structures.
nested = [["apple", "banana"], [1, 2, 3]]
print(nested[0][1])    # banana
print(nested[1][2])    # 3

# Copying Lists
# Wrong way (creates link):
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]

# Right way (creates copy):
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # [1, 2, 3]


# Summary of Key List Methods
# | Method         | Description                         |
# | -------------- | ----------------------------------- |
# | `append(x)`    | Adds `x` to the end of the list     |
# | `insert(i, x)` | Inserts `x` at index `i`            |
# | `extend(lst)`  | Adds all items from another list    |
# | `remove(x)`    | Removes first occurrence of `x`     |
# | `pop(i)`       | Removes item at index `i` (or last) |
# | `clear()`      | Removes all items                   |
# | `sort()`       | Sorts the list                      |
# | `reverse()`    | Reverses the list                   |
# | `copy()`       | Creates a shallow copy              |