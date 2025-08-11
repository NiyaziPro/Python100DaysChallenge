import random

from Beginner.day14.art import logo, vs
from Beginner.day14.game_data import data


def format_account(account):
    """Formats account data into a printable string."""
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks if the user's guess is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# ----- GAME LOOP -----
def play_game():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"\nCompare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"✅ Correct! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"❌ Wrong! Final score: {score}.")

# ----- RUN -----
if __name__ == "__main__":
    print("👋 Welcome to the Higher-Lower Game: European Edition!")
    play_game()