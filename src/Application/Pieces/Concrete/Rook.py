from Pieces.Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

ROK_IMG_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets", "imgs", "testasset", "rooktest.jpg")


class Rook(Piece):
    def __init__(self, radius, x=0, y=0, ptype=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, ptype, offSetX, offSetY)
        self.image = Image(ROK_IMG_PATH)
        self.image.set_position(self.center[0], self.center[1])

    def inbounds(self, name, i) -> bool:
        if 7 > getattr(self, name) + i > 0:
            return False
        else:
            return True


    def movepossibilities(self, pieces: list[Piece]) -> list[list[int]]:
        mask = self.createmask()

       #for i in [-2, +2]:
       #    if self.inbounds("x", i):
       #        for j in [-1, 1]:
       #            if self.inbounds("y", j):
       #                mask[self.x + i][self.y + j] = 1
       #    if self.inbounds("y", i):
       #        for j in [-1, 1]:
       #            if self.inbounds("x", j):
       #                mask[self.x + i][self.y + j] = 1

        for piece in pieces:
            if (piece.x == self.x or piece.y == self.y) and self.type != piece.type:
                mask[piece.x][piece.y] = 2
            else:
                mask[piece.x][piece.y] = -2
        
        for i in [-1, 1]:
            # Para x primeiro
            count = 1
            while True:
                if(0 <= self.x + i * count <= 7):
                    if(mask[self.x + i * count][self.y] == -2) or (mask[self.x + i * count][self.y] == 2):
                        self.fillRest(mask, (self.x + i * count + 1, self.y), 2 * i)
                        break

            # Para y segundo
            count = 1
            while True:
                if(0 <= self.y + i * count <= 7):
                    if(mask[self.x][self.y + i * count] == -2) or (mask[self.x][self.y + i * count] == 2):
                        self.fillRest(mask, (self.x, self.y + i * count + 1), i)


        mask[self.x][self.y] = 0
        return mask

    def draw(self):
        self.image.draw()

    def fillRest(self, matriz, posicao: tuple, direcao):
        if(posicao[0] > 7 or posicao[0] < 0) or (posicao[1] > 7 or posicao[1] < 0):
            return
        if(not(matriz[posicao[0]][posicao[1]] == -2)):
            matriz[posicao[0]][posicao[1]] = -1
        
        if(direcao % 2 == 0):
            self.fillRest(matriz, (posicao[0] + direcao / 2, posicao[1]), direcao)
        else:
            self.fillRest(matriz, (posicao[0], posicao[1] + direcao), direcao)
        
