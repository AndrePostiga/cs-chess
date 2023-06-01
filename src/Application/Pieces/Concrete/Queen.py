from ..Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

BSP_IMG_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets", "imgs",
                 "testasset", "bishoptest.jpg")


class Queen(Piece):
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

    def fillRest(self, matriz, posicao: tuple, direcao: int):
        if (posicao[0] > 7 or posicao[0] < 0) or (posicao[1] > 7 or posicao[1] < 0):
            return
        if not (matriz[posicao[0]][posicao[1]] == -2):
            matriz[posicao[0]][posicao[1]] = -1

        if direcao % 2 == 0:
            self.fillRest(matriz, (posicao[0] + direcao / 2, posicao[1]), direcao)
        else:
            self.fillRest(matriz, (posicao[0], posicao[1] + direcao), direcao)

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
                mask[piece.x][piece.y] = 2
            else:
                mask[piece.x][piece.y] = -2

        for i in [-1, 1]:
            # Para x primeiro
            count = 1
            while True:
                if 0 <= self.x + i * count <= 7:
                    if (mask[self.x + i * count][self.y] == -2) \
                            or (mask[self.x + i * count][self.y] == 2):
                        self.fillRest(mask, (self.x + i * count + 1, self.y), 2 * i)
                        break

            # Para y segundo
            count = 1
            while True:
                if 0 <= self.y + i * count <= 7:
                    if (mask[self.x][self.y + i * count] == -2) \
                            or (mask[self.x][self.y + i * count] == 2):
                        self.fillRest(mask, (self.x, self.y + i * count + 1), i)
                        break

        # parte bispo

        self.calculatediagon(1, 1, mask, pieces)
        self.calculatediagon(1, -1, mask, pieces)
        self.calculatediagon(-1, -1, mask, pieces)
        self.calculatediagon(-1, 1, mask, pieces)

        mask[self.x][self.y] = 0
        return mask

        pass
