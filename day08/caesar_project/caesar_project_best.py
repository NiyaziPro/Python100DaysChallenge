import string
from day08.caesar_project import caesar_art

alphabet = list(string.ascii_lowercase)

def encrypt(text, cipher_table):
    return "".join(cipher_table[alphabet.index(c)] if c in alphabet else c for c in text)

def decrypt(text, cipher_table):
    return "".join(alphabet[cipher_table.index(c)] if c in cipher_table else c for c in text)

def ask_continue():
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if answer == 'yes':
        return True
    elif answer == 'no':
        print("Goodbye")
        return False
    else:
        print("Invalid input. Try again.")
        return True

print(caesar_art.logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()

    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Please enter a valid number.")
        continue

    cipher_table = alphabet[shift:] + alphabet[:shift]

    if direction == "encode":
        print("Here's the encoded result: " + encrypt(text, cipher_table))
    elif direction == "decode":
        print("Here's the decoded result: " + decrypt(text, cipher_table))
    else:
        print("Invalid operation. Try again.")
        continue

    if not ask_continue():
        break
