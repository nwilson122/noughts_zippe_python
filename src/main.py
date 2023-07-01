from enum import Enum

class BoardState(Enum):
    NOUGHTS_WIN = 'NOUGHTS_WIN'
    CROSSES_WIN = 'CROSSES_WIN'
    DRAW = 'DRAW'

# Initial function for getting the state of a board, to be completed later
def get_state_of_board(board):
    return BoardState.DRAW