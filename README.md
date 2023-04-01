# Hangman game
This code is a simple implementation of the classic game of Hangman in Python. The game randomly selects a word from a list of predefined words and the player has to guess the word by suggesting letters, one at a time. The player has 10 attempts to guess the word before the game ends.

# How to Play
1. The game will randomly select a word from a list of words.

2. The player will be prompted to enter a letter.

3. The game will check if the letter is in the word or not.

4. If the letter is in the word, the game will show the letter in its correct position(s).

5. If the letter is not in the word, the game will display a part of the hangman.

6. The player has to guess the word before the hangman is fully displayed.

7. If the player guesses the word correctly within 10 attempts, they win the game. If not, they lose.

# Code
The code is written in Python and uses the random library for handling events. It defines a function hangman() which contains the game logic. It selects a random word from a list of words, and then uses a loop to prompt the player for input and check if the input is in the word or not. It also displays the hangman figure based on the number of incorrect attempts.

To start the game, simply run the code and follow the prompts. Good luck!


