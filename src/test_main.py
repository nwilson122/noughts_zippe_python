import unittest
from main import get_state_of_board, BoardState


class TestBoardState(unittest.TestCase):
    def test_get_state_of_board(self):
        # Test winning boards
        self.assertEqual(
            get_state_of_board("XXXOO____"), BoardState.CROSSES_WIN
        )
        self.assertEqual(
            get_state_of_board("XX_OOOX__"), BoardState.NOUGHTS_WIN
        )
        # Test unfinished board
        self.assertEqual(
            get_state_of_board("XOXO_____"), BoardState.UNFINISHED
        )
        # Test draw
        self.assertEqual(get_state_of_board("XOXOOXXXO"), BoardState.DRAW)
        # Test invalid board
        self.assertEqual(get_state_of_board("Invalid_"), BoardState.INVALID)


if __name__ == "__main__":
    unittest.main()
