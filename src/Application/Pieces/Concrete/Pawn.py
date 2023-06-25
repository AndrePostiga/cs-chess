from ..Piece import Piece

from Lib.image import Image
import os

PRJ_FLDR = os.path.dirname(os.path.abspath(__file__))

PAWN_IMG_PATH_W = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets",
                 "imgs", "testassets", "Chess_plt60.png")

PAWN_IMG_PATH_B = \
    os.path.join(PRJ_FLDR, "..", "..", "..", "assets",
                 "imgs", "testassets", "Chess_pdt60.png")


def check_pawn(x, y, type, pieces):
    for piece in pieces:
        if isinstance(piece, Pawn) and piece.enpassant \
                and piece.x == x and piece.y == y \
                and piece.type != type:
            return piece
    return None


def check_piece(x, y, pieces):
    for piece in pieces:
        if piece.x == x and piece.y == y:
            return piece
    else:
        return None
    pass


class Pawn(Piece):
    def __init__(self, radius, x=0, y=0, ptype=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, ptype, offSetX, offSetY)
        self.enpassant = False
        if self.type == 1:
            self.image = Image(PAWN_IMG_PATH_W)
        else:
            self.image = Image(PAWN_IMG_PATH_B)
        self.image.set_position(self.center[0], self.center[1])

    # manda uma matriz de possibilidades de movimento,
    # uma máscara, para aplicar sobre o tabuleiro, isto é,
    # para pintar quadrados de verde, vermelho, amarelo etc
    def movepossibilities(self, pieces):
        maskmatrix = self.createmask()
        maskmatrix[self.x][self.y + (1 if self.type == 0 else -1)] = 1
        if self.firstplay \
                and (check_piece(self.x, self.y + (1 if self.type == 0 else
        -1), pieces) is None) \
                and (check_piece(self.x, self.y + (1 if self.type == 0 else
        -1), pieces) is None):
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
        #####en passant
        self.check_enpassant(pieces, maskmatrix)

        maskmatrix[self.x][self.y] = 0
        return maskmatrix

    def move(self, x, y, pieces):
        fp = self.firstplay
        cord = [self.x, self.y]
        if self.movepossibilities(pieces)[x][y] == 3:
            # enpassant
            self.x = x
            self.y = y
            self.setCenter()
            self.image.set_position(self.center[0], self.center[1])
            self.firstplay = False

            kp = check_pawn(self.x, self.y +
                            (-1 if self.type == 0 else 1), self.type, pieces)
            mv = True



        else:
            kp, mv = super().move(x, y, pieces)
            # se for a primeira vez que moveu:

            if mv and fp and (cord[1] == self.y + 2 or cord[1] == self.y - 2):
                self.enpassant = True
            else:
                self.enpassant = False

        #

        return kp, mv

    def check_enpassant(self, pieces, maskmatrix):
        for i in [-1, 1]:
            pawn = check_pawn(self.x + i, self.y, self.type, pieces)
            if (pawn and
                    maskmatrix[self.x + i][self.y + (1 if self.type == 0
                    else -1)] == -1):
                maskmatrix[self.x + i][self.y + (1 if self.type == 0 else -1)] = 3
                # 3 = special movement
