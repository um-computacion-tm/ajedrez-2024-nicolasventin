from piece import Piece


class Rook(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"
        
def rook_move(self, from_row, from_col, to_row, to_col):
        pass
