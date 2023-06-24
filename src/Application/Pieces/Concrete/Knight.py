from ..Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

KNT_IMG_PATH_W = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets",
                 "imgs", "testassets", "Chess_nlt60.png")

KNT_IMG_PATH_B = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets",
                 "imgs", "testassets", "Chess_ndt60.png")


def inbounds(attr, i) -> bool:
    if 7 >= attr + i >= 0:
        return True
    else:
        return False


class Knight(Piece):

    def __init__(self, radius, x=0, y=0, ptype=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, ptype, offSetX, offSetY)
        if self.type == 1  or self.type == 5:
            self.image = Image(KNT_IMG_PATH_W)
        else:
            self.image = Image(KNT_IMG_PATH_B)
        self.image.set_position(self.center[0], self.center[1])

    def movepossibilities(self, pieces: list[Piece]) -> list[list[int]]:
        mask = self.createmask()

        for i in [-2, +2]:
            if inbounds(self.x, i):
                for j in [-1, 1]:
                    if inbounds(self.y, j):
                        mask[self.x + i][self.y + j] = 1
            if inbounds(self.y, i):
                for j in [-1, 1]:
                    if inbounds(self.x, j):
                        mask[self.x + j][self.y + i] = 1

        for piece in pieces:
            if piece.type != self.type and (mask[piece.x][piece.y] == 1):
                mask[piece.x][piece.y] = 2
            else:
                mask[piece.x][piece.y] = -2

        mask[self.x][self.y] = 0
        return mask

