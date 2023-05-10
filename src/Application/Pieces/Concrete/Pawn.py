from src.Application.Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, x_pos: int, y_pos: int):
        super().__init__(x_pos, y_pos)
        self.movementType = "frontal"
        self.nMovement = 1

    def move(self, table, i, j):
        pass

