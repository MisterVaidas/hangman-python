# Hangman 1.0

Hangman 1.0 is a simple, console-based word guessing game implemented in Python. The game selects a word at random from a predefined list, and the player tries to guess it one letter at a time.

## Features

- Random word selection from a large word list.
- ASCII art representations for the hangman.
- Tracking of guessed letters to avoid repetition.
- Interactive console-based user interface.

## How to Play

1. Run the game in a Python environment.
2. The game will display a series of underscores representing the letters of a randomly chosen word.
3. Enter one letter at a time to guess the word.
4. If the guessed letter is in the word, it will be revealed in its correct position(s).
5. If the guessed letter is not in the word, part of the hangman will be drawn.
6. The game continues until the word is completely guessed or the hangman is fully drawn.

## Requirements

- Python 3.x
- Two additional Python files: `hangman_words.py` and `hangman_art.py` containing the word list and ASCII art, respectively.

## Installation

No additional installation is required. Ensure you have Python 3.x installed on your system.

## Usage

Run the script in your Python environment:

```bash
python hangman.py
```

## Contributing

Feel free to fork the project, make improvements, and open a pull request with your changes.

## Acknowledgments

- ASCII art and words list inspired by various open-source resources.
- Created as a part of a Python learning project.

***
Enjoy playing Hangman 1.0!