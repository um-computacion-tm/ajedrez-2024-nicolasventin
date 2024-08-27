import unittest
from game.king import King

class TestKing(unittest.TestCase):
    
    def setUp(self):
        self.white_king = King("White")
        self.black_king = King("Black")

    def test_king_valid_moves(self):
        self.assertTrue(self.white_king.king_move(4, 4, 5, 5))  # Diagonal
        self.assertTrue(self.white_king.king_move(4, 4, 4, 5))  # Derecha
        self.assertTrue(self.white_king.king_move(4, 4, 5, 4))  # Abajo
        self.assertTrue(self.white_king.king_move(4, 4, 3, 3))  # Diagonal inversa
        self.assertTrue(self.white_king.king_move(4, 4, 4, 3))  # Izquierda

    def test_king_invalid_moves(self):
        self.assertFalse(self.white_king.king_move(4, 4, 6, 6))  # Fuera de rango

if __name__ == '__main__':
    unittest.main()
