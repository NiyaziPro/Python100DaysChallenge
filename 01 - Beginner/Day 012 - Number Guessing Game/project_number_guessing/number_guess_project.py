import random

random_number = random.randint(0, 101)
print(random_number)
lives = 1

def number_guessing(lives):
    while lives > 0:
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            break
        elif guess > random_number:
            lives -= 1
            print(f"Too high.\nGuess again.\nYou have {lives} attempts remaining to guess the number.")
        elif guess < random_number:
            lives -= 1
            print(f"Too low.\nGuess again.\nYou have {lives} attempts remaining to guess the number.")
        else:
            print("Error")
        if lives == 0:
            print("You've run out of guesses, you lose.")


print("Welcome to the Number Guessing Game :)")
print("I'm thinking of a number between 1 and 100.")

choose = input("Choose a difficulty.Type 'easy' or 'hard' : ").lower()

if choose == "easy":
    lives = 10
    number_guessing(lives)

elif choose == "hard":
    lives = 5
    number_guessing(lives)