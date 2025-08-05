import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [dictionary[letter] for letter in word]
    except KeyError as error_message:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
