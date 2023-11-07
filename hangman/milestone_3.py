import random

fruits = [
    "apple", "apricot", "avocado", "banana", "blackberry", "blueberry", "boysenberry", "breadfruit",
    "cantaloupe", "carambola", "cherimoya", "cherry", "cloudberry", "coconut", "cranberry", "date",
    "dragonfruit", "durian", "elderberry", "feijoa", "fig", "goji berry", "gooseberry", "grape",
    "grapefruit", "guava", "honeydew", "huckleberry", "jabuticaba", "jackfruit", "jambul", "jujube",
    "kiwi", "kumquat", "lemon", "lime", "longan", "loquat", "lychee", "mango", "mangosteen",
    "marionberry", "melon", "mulberry", "nectarine", "orange", "papaya", "passion fruit", "peach",
    "pear", "persimmon", "pineapple", "pitaya", "plantain", "plum", "pomegranate", "pomelo",
    "prickly pear", "quince", "raspberry", "red currant", "rambutan", "sapodilla", "sapote",
    "soursop", "star apple", "star fruit", "strawberry", "tamarillo", "tamarind", "tangerine",
    "ugli fruit", "watermelon", "white currant", "white sapote", "xigua", "yellow watermelon",
    "yuzu", "zucchini", "kaki",
]

word_list = fruits
word_to_be_guessed = random.choice(word_list).lower()


def check_guess(letter, word):
    if letter_is_in_word := (letter in word):
        print(f"Good guess! {letter} is in the word.")
    else:
        print(f"Sorry, {letter} is not in the word. Try again.")

    return letter_is_in_word


def ask_for_input(word_to_be_guessed):
    while True:
        letter_guess = input("Please guess a letter: ").lower()

        if len(letter_guess) == 1 and letter_guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    return letter_guess, check_guess(letter_guess, word_to_be_guessed)


letter_guess, is_guess_in_word = ask_for_input(word_to_be_guessed)
print(f"Guess: {letter_guess}, " + ("is" if is_guess_in_word else "is not") + " in the word to be guessed.")