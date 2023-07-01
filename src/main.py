import sys
import unittest
from enum import Enum

# Characters used in the board string
CROSS = "X"
NOUGHT = "O"
EMPTY = "_"


class BoardState(Enum):
    NOUGHTS_WIN = "NOUGHTS_WIN"
    CROSSES_WIN = "CROSSES_WIN"
    DRAW = "DRAW"
    UNFINISHED = "UNFINISHED"
    INVALID = "INVALID"


def validate_board(board: str) -> bool:
    """Checks that the board string is valid,
    i.e., 9 characters consisting only of 'X', 'O', or '_'."""
    return len(board) == 9 and set(board).issubset({CROSS, NOUGHT, EMPTY})


def is_winning(board: str, player: str) -> bool:
    """Check if the player has any winning combination."""
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(
        board[i] == board[j] == board[k] == player
        for i, j, k in winning_combinations
    )


def get_state_of_board(board: str) -> BoardState:
    """Determine the state of a game board."""
    if not validate_board(board):
        return BoardState.INVALID
    elif is_winning(board, CROSS):
        return BoardState.CROSSES_WIN
    elif is_winning(board, NOUGHT):
        return BoardState.NOUGHTS_WIN
    elif EMPTY in board:
        return BoardState.UNFINISHED
    else:
        return BoardState.DRAW


def print_board_states(boards):
    """Prints the state of each board in the given list."""
    for board in boards:
        state = get_state_of_board(board)
        if state == BoardState.INVALID:
            print(f"Invalid board: {board}", file=sys.stderr)
        else:
            print(state.value)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] != "-v":
        print_board_states(sys.argv[1:])
    else:
        unittest.main()
