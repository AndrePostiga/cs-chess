from ..Piece import Piece
from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

KNG_IMG_PATH_W = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets",
                 "imgs", "testassets", "Chess_klt60.png")

KNG_IMG_PATH_B = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets",
                 "imgs", "testassets", "Chess_kdt60.png")


class King(Piece):

    def __init__(self, radius, x=0, y=0, type=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, type, offSetX, offSetY)
        if self.type == 1:
            self.image = Image(KNG_IMG_PATH_W)
        else:
            self.image = Image(KNG_IMG_PATH_B)
        self.image.set_position(self.center[0], self.center[1])

    def movepossibilities(self, pieces: list["Piece"]) -> list[list[int]]:
        mask = self.createmask()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (0 <= self.x + i <= 7) and (0 <= self.y + j <= 7):
                    mask[self.x + i][self.y + j] = 1

        for piece in pieces:
            if piece.type != self.type and (mask[piece.x][piece.y] == 1):
                mask[piece.x][piece.y] = 2
            else:
                mask[piece.x][piece.y] = -2

        mask[self.x][self.y] = 0
        return mask