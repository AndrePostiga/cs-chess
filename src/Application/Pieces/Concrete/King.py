from ..Piece import Piece
from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))
KNG_IMG_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets", "imgs", "testasset", "kingtest.jpg")


class King(Piece):
    def draw(self):
        self.image.draw()

    def movepossibilities(self, pieces: list["Piece"]) -> list[list[int]]:
        mask = self.createmask()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                pieces[self.x+i][self.y+i] = 1

        for piece in pieces:
            if self.type == piece.type:
                mask[piece.x][piece.y] = -2
            else:
                mask[piece.x][piece.y] = 2

        mask[self.x][self.y] = 0
        return mask

    def __init__(self, radius, x=0, y=0, type=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, type, offSetX, offSetY)
        self.image = Image(KNG_IMG_PATH)
        self.image.set_position(self.center[0], self.center[1])
