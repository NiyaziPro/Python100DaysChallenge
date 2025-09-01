import random

#  random.random() - Returns a random float between 0.0 and 1.0.
# Usage: Simulations, probability experiments, or scaling to any range (e.g. value * 100 gives a float from 0 to 100).
value = random.random()
print("Random float between 0.0 and 1.0:", value)

# random.randint(a, b)
# Returns a random integer from a to b, inclusive.
# Usage: Simulates a dice roll or any bounded integer generation.
number = random.randint(1, 6)
print("Rolling a die... You got:", number)

# random.randrange(start, stop, step)
# Returns a randomly selected element from the given range.
# Usage: When you need a number from a specific range with a step (e.g., only even or only multiples of 5).
even_number = random.randrange(0, 100, 2)
print("Random even number under 100:", even_number)

# random.choice(sequence)
# Picks one random item from a list, tuple, or string.
# Usage: Random selections like choosing a random card, winner, or direction.
colors = ["red", "green", "blue", "yellow"]
selected = random.choice(colors)
print("Random color:", selected)

# random.choices(population, k=number)
# Returns k random elements with replacement.
# Usage: Useful when duplicates are acceptable (e.g., rolling multiple dice).
lottery_numbers = random.choices(range(1, 50), k=6)
print("Lottery numbers (with possible repeats):", lottery_numbers)

# random.sample(population, k=number)
# Returns k unique random elements without replacement.
# Usage: Drawing unique winners, selecting a team, generating a quiz with no repeated questions.
unique_draw = random.sample(range(1, 50), 6)
print("Lottery numbers (no repeats):", unique_draw)

# random.shuffle(list)
# Shuffles the items of a list in place.
# Usage: Useful for games or mixing datasets randomly.
deck = ["A", "K", "Q", "J", "10", "9"]
random.shuffle(deck)
print("Shuffled deck:", deck)

# random.uniform(a, b)
# Returns a random float number between a and b.
# Usage: Simulate prices, measurements, or values with decimal precision.
price = random.uniform(10.5, 75.5)
print("Random price:", round(price, 2))

# random.seed(value)
# Fixes the sequence of random numbers (for reproducibility).
# Usage: Useful in testing or tutorials where predictable "random" results are needed.
random.seed(42)
print(random.randint(1, 100))  # Will always return same number when seeded


# Combined Example:
random.seed(123)  # Consistent results

names = ["Alice", "Bob", "Charlie", "Diana"]
winner = random.choice(names)
scores = random.sample(range(50, 100), 3)

print("Winner:", winner)
print("Top 3 scores:", scores)

