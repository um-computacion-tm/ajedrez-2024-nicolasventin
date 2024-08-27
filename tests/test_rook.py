import unittest
from game.rook import Rook
import game.board as Board

class TestRook(unittest.TestCase):
    def test_str(self):
        rook = Rook("WHITE")
        self.assertEqual(str(rook), "♜")
        
    def test_rook_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.rook.possible.positions(4,0)
        self.assertEqual(possibles, [(5,0), (6,0), (7,0)])

    def test_rook_move_vertical_asc(self):              
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.rook.possible.positions(4,0)
        self.assertEqual(possibles, [(3,0), (2,0), (1,0), (0,0)])
        rook.possible
        
if __name__ == '__main__':
    unittest.main()