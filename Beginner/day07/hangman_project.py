import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
    "apple",
    "banana",
    "orange",
    "guitar",
    "planet",
    "animal",
    "bridge",
    "window",
    "forest",
    "castle",
    "desert",
    "jungle",
    "pirate",
    "dragon",
    "rocket",
    "wizard",
    "island",
    "camera",
    "hunter",
    "monster",
    "diamond",
    "zombie",
    "phoenix",
    "python",
    "treasure",
    "galaxy",
    "volcano",
    "nightmare",
    "labyrinth",
    "avalanche",
    "sphinx",
    "mystery"
]
green = "\033[92m"
red = "\033[91m"
reset = "\033[0m"

lives = 6
random_word = random.choice(word_list)
print(random_word)
print(len(random_word))
placeholder = ""
game_over = False
correct_letters = []
length_word = len(random_word)

for i in range(length_word):
    placeholder += "_"
print(placeholder)

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in random_word:

        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    print(correct_letters)

    if guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(red + "You lose." + reset)

    if "_" not in display:
        game_over = True
        print(green + "You win." + reset)

    print(stages[lives])
