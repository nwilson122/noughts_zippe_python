## Noughts and Crosses Game
This project implements the Noughts and Crosses (also known as Tic-Tac-Toe) game using Python. The game is played by two players on a 3x3 board, with one player as Noughts (O) and the other as Crosses (X). The objective is to get three symbols in a row horizontally, vertically, or diagonally.

### Project Structure
The project consists of the following files and directories:
src/main.py: The main Python script that contains the game logic and the implementation of the Noughts and Crosses game.
src/tests.py: Unit tests for the game logic.
.pre-commit-config.yaml: Configuration file for pre-commit hooks to enforce code quality and formatting.
pyproject.toml: Configuration file for Black code formatter.

### Packages Used
The project relies on the following packages:

unittest: Python's built-in unit testing framework used for testing the game logic.
enum: A module that provides a way to define enumerations in Python, used for representing the game board state.
pre-commit: A framework for managing and maintaining multi-language pre-commit hooks, used for enforcing code quality and formatting.
black: A code formatter that follows a strict style guide, used to automatically format the code according to consistent standards.
flake8: A linting tool for checking code quality and adherence to style guidelines, used to identify and report any code issues.

### Approach to the Problem
The Noughts and Crosses game is implemented using an object-oriented approach. The main logic is encapsulated in the get_state_of_board function, which takes a board string as input and determines the state of the game. The board is represented as a string of length 9, with 'X' for Crosses, 'O' for Noughts, and '_' for empty slots.

Problem approach
The function first validates the board to ensure it is a valid configuration. It then checks for winning combinations for both Crosses and Noughts. If a winning combination is found, the corresponding player wins. If there are no empty slots and no winning combinations, the game is a draw. The function returns the corresponding BoardState enumeration value representing the game state.

Unit tests are included in the tests.py file to verify the correctness of the game logic. These tests cover various scenarios, including winning boards, unfinished boards, draw boards, and invalid boards.

Pre-commit hooks are configured to automatically run code formatting and linting checks before each commit. This ensures that the code adheres to a consistent style and quality standards, maintaining readability and reducing potential issues.

Note: The project is configured with Sphinx, to create documentation in case it's ever expanded. As of now, it's just a setup/skeleton for a possible app.
