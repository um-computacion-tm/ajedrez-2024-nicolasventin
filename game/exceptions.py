class InvalidMove():
    pass
class InvalidMoveNoPiece(InvalidMove):
    pass

class InvalidMoveRookMove(InvalidMove):
    pass

class InvalidMove(Exception):
    pass