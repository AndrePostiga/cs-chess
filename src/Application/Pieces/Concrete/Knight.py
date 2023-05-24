from ..Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

KNT_IMG_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets", "imgs", "testasset", "pawntest.jpg")


class Knight(Piece):
    def __init__(self, radius, x=0, y=0, ptype=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, ptype, offSetX, offSetY)
        self.image = Image(KNT_IMG_PATH)
        self.image.set_position(self.center[0], self.center[1])

    def inbounds(self, name, i) -> bool:
        # TODO: alguém testa isso pra mim?
        if 7 > getattr(self, f"self.{name}") + i > 0:
            return False
        else:
            return True

    def movepossibilities(self, pieces: list[Piece]) -> list[list[int]]:
        mask = self.createmask()

        for i in [-2, +2]:
            if self.inbounds("x", i):
                for j in [-1, 1]:
                    if self.inbounds("y", j):
                        mask[self.x + i][self.y + j] = 1
            if self.inbounds("y", i):
                for j in [-1, 1]:
                    if self.inbounds("x", j):
                        mask[self.x + i][self.y + j] = 1

        for piece in pieces:
            if piece.type != self.type and (mask[piece.x][piece.y] == 1):
                mask[piece.x][piece.y] = 2
            else:
                mask[piece.x][piece.y] = -2

        mask[self.x][self.y] = 0
        return mask

    def draw(self):
        self.image.draw()
