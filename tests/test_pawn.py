import unittest
from game.pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_str(self):
        self.white_pawn = Pawn("White")
        self.black_pawn = Pawn("Black")
        
    def test_white_pawn_single_move(self):
        self.assertTrue(self.white_pawn.pawn_move(6, 4, 5, 4))

    def test_white_pawn_double_move(self):
        self.assertTrue(self.white_pawn.pawn_move(6, 4, 4, 4))
    
    def test_white_pawn_invalid_move(self):
        self.assertFalse(self.white_pawn.pawn_move(6, 4, 7, 4))
    
    def test_black_pawn_single_move(self):
        self.assertTrue(self.black_pawn.pawn_move(1, 4, 2, 4))
    
    def test_black_pawn_double_move(self):
        self.assertTrue(self.black_pawn.pawn_move(1, 4, 3, 4))

    def test_black_pawn_invalid_move(self):
        self.assertFalse(self.black_pawn.pawn_move(1, 4, 0, 4))
 
if __name__ == '__main__':
    unittest.main()