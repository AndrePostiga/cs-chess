from ..Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

BSP_IMG_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets", "imgs",
                 "testasset", "bishoptest.jpg")


class Bishop(Piece):
    def __init__(self, radius, x=0, y=0, ptype=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, ptype, offSetX, offSetY)
        self.image = Image(BSP_IMG_PATH)
        self.image.set_position(self.center[0], self.center[1])

    def haspiece(self, x, y, pieces):
        for piece in pieces:
            if (piece.x == x) and (piece.y == y):
                if piece.type != self.type:
                    return 2
                else:
                    return -2
        return None

    def calculatediagon(self, dirx, diry, mask, pieces):
        i = 0 + dirx
        j = 0 + diry
        # loop1
        while True:
            if ((self.x + i) > 7) or ((self.y + j) > 7) \
                    or ((self.x + i) < 0) or ((self.y + j) < 0): break
            a = self.haspiece(self.x + i, self.y + j, pieces)
            if a is None:
                mask[self.x + i][self.y + j] = 1
                i = i + dirx
                j = j + diry
                continue
            else:
                mask[self.x + i][self.y + j] = a
                break

    def movepossibilities(self, pieces: list[Piece]) -> list[list[int]]:
        mask = self.createmask()

        # chato: caminhamento individual
        self.calculatediagon(1, 1, mask, pieces)
        self.calculatediagon(1, -1, mask, pieces)
        self.calculatediagon(-1, -1, mask, pieces)
        self.calculatediagon(-1, 1, mask, pieces)

        mask[self.x][self.y] = 0
        return mask
