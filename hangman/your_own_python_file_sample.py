# Standard libraries
import random

# Local project libraries
from milestone_5 import Hangman
import word_lists

hangman = Hangman(num_lives=6)

while True:
    list_name = random.choice(list(word_lists.word_lists.keys()))
    print(f"\n\nPlaying a game from {list_name}:")
    hangman.play(word_lists.word_lists[list_name])
