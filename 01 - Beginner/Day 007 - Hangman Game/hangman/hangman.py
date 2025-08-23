import random
import hangman_worlds
import hangman_art
from utils import colors

print(colors.green + hangman_art.logo, "\n", colors.reset)
lives = 6
random_word = random.choice(hangman_worlds.word_list)
placeholder = ""
word_length = len(random_word)

for position in range(word_length):
    placeholder += "_"
print(colors.blue + "Word to guess: " + placeholder + colors.reset)

game_over = False
correct_letters = []

while not game_over:
    display = ""
    print(f"{colors.yellow}****************************{lives}/6 LIVES LEFT****************************{colors.reset}")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(colors.blue + "Word to guess: " + display + colors.reset)

    if guess not in random_word:
        lives -= 1
        print(f"{colors.magenta}You guessed {guess}, that's not in the word. You lose a life!{colors.reset}")

        if lives == 0:
            game_over = True

            print(
                f"{colors.red}***********************IT WAS {random_word}! YOU LOSE**********************{colors.reset}")

        if "_" not in display:
            game_over = True

            print(colors.green + "****************************YOU WIN****************************" + colors.reset)

        print(hangman_art.stages[lives])
