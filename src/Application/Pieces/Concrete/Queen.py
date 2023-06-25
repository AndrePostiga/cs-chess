from .King import King
from ..Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

QUE_IMG_PATH_W = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets",
                 "imgs", "testassets", "Chess_qlt60.png")

QUE_IMG_PATH_B = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets",
                 "imgs", "testassets", "Chess_qdt60.png")

class Queen(Piece):
    def __init__(self, radius, x=0, y=0, ptype=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, ptype, offSetX, offSetY)
        if self.type == 1  or self.type == 5:
            self.image = Image(QUE_IMG_PATH_W)
        else:
            self.image = Image(QUE_IMG_PATH_B)
        self.image.set_position(self.center[0], self.center[1])

    def haspiece(self, x, y, pieces):
        for piece in pieces:
            if (piece.x == x) and (piece.y == y):
                if piece.type != self.type:
                    if isinstance(piece, King):
                        return 4
                    else:
                        return 2
                else:
                    return -2
        return None

    def fillRest(self, matriz, posix, posiy, direcao: int):
        if (posix > 7 or posix < 0) or (posiy > 7 or posiy < 0):
            return
        if not (matriz[posix][posiy] == -2):
            matriz[posix][posiy] = -1

        if direcao % 2 == 0:
            dire = int(direcao / 2)

            self.fillRest(matriz, posix + dire, posiy, direcao)
        else:
            self.fillRest(matriz, posix, posiy + direcao, direcao)

    def calculatediagon(self, dirx, diry, mask, pieces):
        i = 0 + dirx
        j = 0 + diry
        # loop1
        while True:
            if ((self.x + i) > 7) or ((self.y + j) > 7) \
                    or ((self.x + i) < 0) or ((self.y + j) < 0):
                break
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

        # parte torre
        for piece in pieces:
            if (piece.x == self.x or piece.y == self.y) and self.type != piece.type:
                if isinstance(piece, King):
                    mask[piece.x][piece.y] = 4
                else:
                    mask[piece.x][piece.y] = 2
            else:
                mask[piece.x][piece.y] = -2

        for i in [-1, 1]:
            # Para x primeiro
            count = 1
            while True:
                if 0 <= self.x + i * count <= 7:
                    if (mask[self.x + i * count][self.y] == -2) \
                            or (mask[self.x + i * count][self.y] == 2)\
                            or (mask[self.x + i * count][self.y] == 4):
                        self.fillRest(mask, self.x + i * (count + 1), self.y, 2 * i)
                        break
                    mask[self.x + i * count][self.y] = 1
                    count = count + 1
                else:
                    break

            # Para y segundo
            count = 1
            while True:
                if 0 <= self.y + i * count <= 7:
                    if (mask[self.x][self.y + i * count] == -2) \
                            or (mask[self.x][self.y + i * count] == 2)\
                            or (mask[self.x + i * count][self.y] == 4):
                        self.fillRest(mask, self.x, self.y + i * (count + 1), i)
                        break
                    mask[self.x][self.y + i * count] = 1
                    count = count + 1
                else:
                    break

        # parte bispo

        self.calculatediagon(1, 1, mask, pieces)
        self.calculatediagon(1, -1, mask, pieces)
        self.calculatediagon(-1, -1, mask, pieces)
        self.calculatediagon(-1, 1, mask, pieces)

        mask[self.x][self.y] = 0
        return mask
