from src.Application.Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, Xpos: int, Ypos: int):
        super().__init__(Xpos, Ypos)
        self.movementType = "cross"
        self.nMovement = 2

    def move(self, table, i, j):
        pass
