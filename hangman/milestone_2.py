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
print(word_list)

word_to_be_guessed = random.choice(word_list)
print(word_to_be_guessed)

letter_guess = input("Please guess a letter: ")

if len(letter_guess) == 1 and letter_guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
