from ..Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

PAWN_IMG_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "assets", "imgs", "testasset", "pawntest.jpg")


class Pawn(Piece):
    def __init__(self, radius, x=0, y=0, ptype=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, ptype, offSetX, offSetY)
        self.image = Image(PAWN_IMG_PATH)
        self.image.set_position(self.center[0], self.center[1])

    # mover conforme o prompt
    def move(self, x, y, pieces: list[Piece]) -> Piece:

        check = self.movepossibilities(pieces)

        if check[x][y] == 1:
            self.x = x
            self.y = y

            self.setCenter()
            self.image.set_position(self.center[0], self.center[1])
        elif check[x][y] == 2:
            self.x = x
            self.y = y

            #
            self.setCenter()
            self.image.set_position(self.center[0], self.center[1])
            removerpiece = None

            for piece in pieces:
                if piece.x == self.x and piece.y == self.y:
                    removerpiece = piece
            if removerpiece is not None:
                return removerpiece
            #

        return None

    def draw(self):
        self.setCenter()
        self.image.draw()

    # manda uma matriz de possibilidades de movimento, uma máscara, para aplicar sobre o tabuleiro, isto é,
    # para pintar quadrados de verde, vermelho, amarelo etc
    def movepossibilities(self, pieces: list[Piece]) -> list[list[int]]:
        maskmatrix = self.createmask()
        maskmatrix[self.x][self.y + (1 if self.type == 0 else -1)] = 1
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

    def setCenter(self):
        self.center = (self.offSetX + self.radius * (2 * self.x), self.offSetY + self.radius * (2 * self.y))
