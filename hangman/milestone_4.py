# Standard libraries
import random

# Local project libraries
import word_lists


class Hangman:
    '''
    Hangman is a classic game in which a player thinks of a word and the other
    player tries to guess that word within a certain amount of attempts.

    This is an implementation of the Hangman game, where the computer thinks of
    a word and the user tries to guess it. 
    '''

    def __init__(self, word_list, num_lives=5) -> None:
        '''
        Creates an instance of the game.
        Choses a random word to be guessed from the list provided.
        Initialises game variables.
        '''
        self.word_list = word_list
        self.num_lives = num_lives

        self.word_to_be_guessed = random.choice(self.word_list).lower()
        self.word_guessed = ['_' for letter in self.word_to_be_guessed]

        self.list_of_guesses = []
        self.num_letters_remaining = self._compute_num_letters_remaining()


    def _compute_num_letters_remaining(self):
        '''
        Computes the number of unique letters yet to be guessed.
        '''
        return len(
            set(list(self.word_to_be_guessed))
            - set(self.list_of_guesses)
        )


    def check_guess(self, letter):
        if letter_is_in_word := (letter in self.word_to_be_guessed):
            print(f"Good guess! {letter} is in the word.")

            for idx, letter_in_word in enumerate(self.word_to_be_guessed):
                if letter_in_word == letter:
                    self.word_guessed[idx] = letter
        else:
            print(f"Sorry, {letter} is not in the word. Try again.")

        return letter_is_in_word


    def ask_for_input(self):
        while True:
            letter_guess = input("Please guess a letter: ").lower()

            if not (len(letter_guess) == 1 and letter_guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(letter_guess)
                self.check_guess(letter_guess):
                #if self.check_guess(letter_guess):
                #    break


    def play(self):
        self.ask_for_input()


hangman = Hangman(word_lists.word_lists["fruits"])
hangman.play()