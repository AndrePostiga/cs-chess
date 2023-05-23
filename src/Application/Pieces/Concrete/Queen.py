from src.Application.Pieces.Piece import Piece


class Queen (Piece):
    def __init__(self, x_pos: int, y_pos: int):
        super().__init__(x_pos, y_pos)
        self.movementType = "square"
        self.nMovement = 2

    def move(self, table, i, j):
        pass

