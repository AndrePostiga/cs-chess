from src.Application.Pieces.Piece import Piece


class King (Piece):
    def __init__(self, Xpos: int, Ypos: int):
        super().__init__(Xpos, Ypos)
        self.movementType = "square"
        self.nMovement = 1

    def move(self, table, i, j):
        pass

