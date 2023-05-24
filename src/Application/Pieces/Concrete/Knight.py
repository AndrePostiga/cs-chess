from ..Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR=os.path.dirname(os.path.abspath(__file__))

KNT_IMG_PATH = \
    os.path.join(PRJ_FLDR, "assets", "imgs", "testasset", "pawntest.jpg")

class Knight (Piece):
    def __init__(self, x_pos: int, y_pos: int):
        super().__init__(x_pos, y_pos)
        self.movementType = "jumper"
        self.nMovement = 1

    def move(self, table, i, j):
        pass

