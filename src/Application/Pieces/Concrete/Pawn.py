from ..Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

PAWN_IMG_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets",
                 "imgs", "testassets", "pawntest.jpg")


class Pawn(Piece):
    def __init__(self, radius, x=0, y=0, ptype=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, ptype, offSetX, offSetY)
        self.image = Image(PAWN_IMG_PATH)
        self.image.set_position(self.center[0], self.center[1])
        self.firstplay = True

    # manda uma matriz de possibilidades de movimento,
    # uma máscara, para aplicar sobre o tabuleiro, isto é,
    # para pintar quadrados de verde, vermelho, amarelo etc
    def movepossibilities(self, pieces):
        maskmatrix = self.createmask()
        maskmatrix[self.x][self.y + (1 if self.type == 0 else -1)] = 1
        if self.firstplay:
            maskmatrix[self.x][self.y + 2 * (1 if self.type == 0 else -1)] = 1

        # vê outras peças no campo; lento
        for piece in pieces:
            if piece.type != self.type:
                # pode comer a peça?
                if (piece.y == self.y + (1 if self.type == 0 else -1)) and (
                        (piece.x == self.x + 1) or (piece.x == self.x - 1)):
                    maskmatrix[piece.x][piece.y] = 2

                else:
                    maskmatrix[piece.x][piece.y] = -2
            else:
                maskmatrix[piece.x][piece.y] = -2
        maskmatrix[self.x][self.y] = 0
        return maskmatrix

    def move(self, x, y, pieces):
        o = super().move(x, y, pieces)
        if self.firstplay:
            self.firstplay = False

        return o
