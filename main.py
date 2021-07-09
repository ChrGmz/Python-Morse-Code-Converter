from re import sub
from dictionary import MORSE_DICTIONARY


def translate_msg(msg: str):
    """Accepts a string, strips all punctuation and returns the string as a dictionary of words and corresponding Morse
    code characters."""

    # Use regex to strip message of all punctuation and non-alphanumeric characters and splits words into a list
    stripped_words = sub(r'[^a-zA-Z\d\s:]', "", msg).upper().split()
    return {word: translate_word(word) for word in stripped_words}


def translate_word(word):
    """Returns a string of newline-separated morse code characters corresponding to each alphanumeric character in the
    word"""
    morse_chars = [MORSE_DICTIONARY[char] for char in word]
    return "\n".join(morse_chars)


print("Welcome to my Python Morse Code Generator!")

is_on = True

while is_on:
    user_input = input("Please enter the message you would like translated into morse code. Please bear in mind all "
                       "non-alphanumeric characters will be ignored:\n")

    morse_translation = translate_msg(user_input)
    print("Here is your message converted into Morse code:")
    for term, translation in morse_translation.items():
        print(f"Morse code for {term}:")
        print(translation)

    to_continue = input("Would you like to translate another message? Type y/n: ").lower()

    while to_continue != "y" and to_continue != "n":
        print("Invalid Response: 'y' and 'n' are the only valid responses.")
        to_continue = input("Would you like to translate another message? Type y/n: ").lower()

    if to_continue == "n":
        is_on = False

print("Thank you for using my Python Morse Code Generator!")
