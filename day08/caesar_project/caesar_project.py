alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(string):
    result = ""
    for ch in string:
        if ch in alphabet:
            i = alphabet.index(ch)
            result += list_2[i]
        else:
            result += ch
    return result



def decrypt(word_encrypt):
    result = ""
    for ch in word_encrypt:
        if ch in list_2:
            i = list_2.index(ch)
            result += alphabet[i]
        else:
            result += ch
    return result



again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    list_2 = alphabet[shift:] + alphabet[:shift]
    if direction == "encode":
        print("Here's the encoded result : " + encrypt(text))
        answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
        if answer == "yes":
            continue
        elif answer == "no":
            print("Goodbye")
            break
        else:
            print("Error!")
            continue
    elif direction == "decode":
        print("Here's the decoded result : " + decrypt(text))
        answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
        if answer == "yes":
            continue
        elif answer == "no":
            print("Goodbye")
            break
        else:
            print("Error!")
            continue
    else:
        print("Error! Please type 'encode' to encrypt, type 'decode' to decrypt:")
        continue