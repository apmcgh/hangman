# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Lessons learnt
Discovered the assignement expression `:=`.

The project instructions did not lead to a complete hangman gameplay, so
I tookthe liberty to add a few essential features.

In a commercial environment, any lack of clarity would have to be resolved with the relevant stakeholders
so as to make sure that the product responds to actual requirements and expectations.

# Installation instructions
Pre-requisites:
- Python, conda, git must be installed, configured and working.
- I assume you have basic knowledge of the above.

Installation:
- Clone this repo.

# Usage instructions
You may try a few sample games with:

    python hangman/milestone_5.py

Or `from milestone_5 import Hangman` in your own python file, in the `hangman` directory and use the following options to play a game:

    <your variable> = Hangman(<optional word list>, <optional number of lives>)
    <your variable>.play(<optional word list>)
    # Note that a word list is necessary in one of the first two calls,otherwise play will raise an exception.

# File structure of the project

The `word_lists` module provides different possible word lists in the form of a dictionary indexed by categories.   
The `milestone_5` module provides some samples of full game play if invoked directly, it can be called as a library.

# License
Copyleft