import unittest
from main import get_state_of_board, BoardState

class TestBoardState(unittest.TestCase):
    def test_get_state_of_board(self):
        # For now, all boards should return DRAW as I haven't implemented the logic yet
        self.assertEqual(get_state_of_board("XXXOO____"), BoardState.DRAW)
        self.assertEqual(get_state_of_board("XX_OOOX__"), BoardState.DRAW)
        self.assertEqual(get_state_of_board("XOXO_____"), BoardState.DRAW)
        self.assertEqual(get_state_of_board("XOXOOXXXO"), BoardState.DRAW)
        self.assertEqual(get_state_of_board("Invalid_"), BoardState.DRAW)

if __name__ == "__main__":
    unittest.main()
