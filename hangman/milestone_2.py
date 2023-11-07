import random

word_list = [
    "fig",
    "mango",
    "sapote",
    "pitaaya",
    "kahki",
]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please guess a letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
