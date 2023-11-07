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

    def __init__(self, word_list=None, num_lives=5) -> None:
        '''
        Creates an instance of the game.

        Hangman takes two optional arguments:
        - word_list, from which a word is chosen at random,
        - num_lives, which defaults to 5.

        Words in a word list may contain non alphabetical characters, such as
        a space or a hyphen, but may not contain any underscores. This condition
        is not enforced but will render a positive outcome impossible.
        Non alphabetical characters will be displayed as is and not be part of
        the guessing.
        '''
        self._word_list = word_list
        self.full_num_lives = num_lives


    def _chose_word(self):
        '''
        Choses a random word to be guessed from the list provided.
        Initialises game variables.
        '''
        if self._word_list is None:
            raise ValueError("Word list is empty, provide a word list to start a game")
        else:
            self.num_lives = self.full_num_lives
            self.list_of_guesses = []
            self.word_to_be_guessed = random.choice(self._word_list).lower()
            
            # The user is not expected to guess non alphabetical characters, so:
            # 1/ display them, and 2/ remove them from the count.
            self.word_guessed = ['_' if letter.isalpha() else letter for letter in self.word_to_be_guessed]
            self.num_letters_remaining = len(set(list(self.word_to_be_guessed)) - set(self.word_guessed))

    def _check_guess(self, letter):
        '''
        Given the user hazarded a guess of a letter,
        check whether the guessed letter is in the word to be guessed,
        either way, do the relevant computations & display adequate messages.
        '''
        if letter in self.word_to_be_guessed:
            print(f"Good guess! {letter} is in the word.")

            for idx, letter_in_word in enumerate(self.word_to_be_guessed):
                if letter_in_word == letter:
                    self.word_guessed[idx] = letter

            self.num_letters_remaining -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")


    def _ask_for_input(self):
        '''
        Get the user to input their guesses, a single letter at a time.
        When a valid letter has been selected, update the relevant game variables,
        and return to the caller.
        '''
        while True:
            # Print game status
            print("\nGuess the word: " + "".join(self.word_guessed))
            print("Letters already tried: " + (", ".join(self.list_of_guesses) if self.list_of_guesses else "None"))

            # Get user input
            letter_guess = input("Please guess a letter: ").lower()

            # Check input validity: 1 letter not already tried
            if not (len(letter_guess) == 1 and letter_guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Input is valid, register the try and check whether it is a good guess
                self.list_of_guesses.append(letter_guess)
                self._check_guess(letter_guess)
                break


    def play(self, word_list=None):
        '''
        Manages a whole game.

        Optional parameter: word_list.
        If no word list was passed to the class constructor, then there must be one here.
        '''
        if word_list:
            self._word_list = word_list

        # Initialise the game
        self._chose_word()

        # Play until the game is won (good guesses) or lost (no lives left)
        while self.num_lives > 0 and self.num_letters_remaining > 0:
            self._ask_for_input()

        # Show the result of the game
        if self.num_lives == 0:
            print("\nYou lost!")
        elif self.num_letters_remaining == 0:
            print("\nYou won!")


if __name__ == "__main__":
    # Initialise a game of hangman, play two
    hangman = Hangman(word_lists.word_lists["fruits"])
    hangman.play()
    hangman.play()

    # Play another one with a different list
    hangman.play(word_lists.word_lists["animals"])

    # Check that if no word list is provided, it bails in error
    try:
        hangman = Hangman()
        hangman.play()
    except ValueError as e:
        print(f"Error [{e}] is expected, testing edge cases")