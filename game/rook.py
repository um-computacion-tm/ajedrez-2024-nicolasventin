from piece import Piece


class Rook(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"
        
    def rook_move(self, from_row, from_col, to_row, to_col):
        if from_row == to_row or from_col == to_col: # falta la logica de saber si hay un enemigo en la casilla o no para saber si es un movimiento legal
            return True
        return False