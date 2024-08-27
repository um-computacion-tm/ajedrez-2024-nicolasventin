from game.piece import Piece


class Rook(Piece):
    white_str = "♜"
    black_str = "♖"
        
    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            possibles.append((next_row, col))
        return possibles
            
    def rook_move(self, from_row, from_col, to_row, to_col):
        if from_row == to_row or from_col == to_col: # falta la logica de saber si hay un enemigo en la casilla o no para saber si es un movimiento legal
            return True
        return False