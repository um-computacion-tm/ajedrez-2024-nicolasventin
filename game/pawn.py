from piece import Piece


class Pawn(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♟"
        else:
            return "♙"

def pawn_move(self, from_row, from_col, to_row, to_col):
    if self.__color__ == "White":
         if from_col == to_col and (from_row - to_row == 1 or (from_row == 6 and from_row - to_row == 2)):
            return True
         else:
            if from_col == to_col and (to_row - from_row == 1 or (from_row == 1 and to_row - from_row == 2)):
                return True
    return False


# falta agregar la logica de comer las piezas en diagonal