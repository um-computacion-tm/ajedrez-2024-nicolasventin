from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True

    def move(self, from_row, from_col, to_row, to_col):

        piece = self.__board__.get_piece(from_row, from_col)

        if not piece:
            raise ValueError("No hay ninguna pieza en la posición inicial")
        
        if piece.color != self.__turn__:
            raise ValueError(f"Es el turno de {self.__turn__})")

        # verifica si el rey puede realizar ese movimiento
        if not piece.king_move(from_row, from_col, to_row, to_col):
            raise ValueError("Movimiento inválido para la pieza")

        self.__board__.move_piece(from_row, from_col, to_row, to_col)

        self.change_turn()

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"


