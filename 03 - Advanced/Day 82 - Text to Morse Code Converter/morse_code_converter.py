# Dictionary mapping letters and numbers to Morse Code
MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"  # Use slash to represent spaces between words
}

def text_to_morse(text: str) -> str:
    """Convert plain text into Morse Code."""
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append("?")  # Unknown characters
    return " ".join(morse_code)


if __name__ == "__main__":
    print("Welcome to the Morse Code Converter!")
    print("Type a message and see it in Morse Code. Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter text: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        morse_output = text_to_morse(user_input)
        print(f"Morse Code: {morse_output}\n")
