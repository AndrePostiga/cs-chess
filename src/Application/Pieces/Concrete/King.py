from .Rook import Rook
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


def check_tower(x, y, pieces, color):
    for piece in pieces:
        if (isinstance(piece, Rook) and piece.firstplay
                and piece.x == x and piece.y == y and piece.type == color):
            return piece
    return None




class King(Piece):

    def checkcheck(self, pieces : list[Piece], xmove, ymove, piecemove: Piece):

        if piecemove is not None: #querem mover
            proxylist = pieces.copy()
            proxypiece = object.__new__(type(piecemove))
            proxypiece.__init__(0, xmove, ymove, piecemove.type, 0, 0)
            #trocar peça real com a proxy
            proxylist.remove(piecemove)
            proxylist.append(proxypiece)
        else: #estado atual
            proxylist = pieces

        #TODO: se for rei = 4, não a 2
        for piece in proxylist:
            possib = piece.movepossibilities(proxylist)
            if possib[self.x][self.y] == 4:
                return 1


        return 0





    def __init__(self, radius, x=0, y=0, type=0, offSetX=0, offSetY=0):
        super().__init__(radius, x, y, type, offSetX, offSetY)
        if self.type == 1  or self.type == 5:
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

        self.check_castling(mask, pieces)

        mask[self.x][self.y] = 0
        return mask

    def check_castling(self, mask, pieces):
        if self.firstplay:
            # kingside
            if (mask[self.x + 1][self.y] == 1 and
                    mask[self.x + 2][self.y] == -1):
                if check_tower(self.x + 3, self.y, pieces, self.type):
                    mask[self.x + 2][self.y] = 3

            # queenside
            if (mask[self.x - 1][self.y] == 1 and
                    mask[self.x - 2][self.y] == -1 and
                    mask[self.x - 3][self.y] == -1):
                if check_tower(self.x - 4, self.y, pieces, self.type):
                    mask[self.x - 2][self.y] = 3

    def move(self, x, y, pieces):
        check = self.movepossibilities(pieces)
        if check[x][y] == 3:
            if x > self.x:
                tower = check_tower( 7, self.y,pieces, self.type)
                tower.x = self.x+1
                tower.setCenter()
                tower.image.set_position(tower.center[0], tower.center[1])
            else:
                tower = check_tower( 0, self.y,pieces, self.type)
                tower.x = self.x - 1
                tower.setCenter()
                tower.image.set_position(tower.center[0], tower.center[1])


            self.x = x
            self.y = y
            self.setCenter()
            self.image.set_position(self.center[0], self.center[1])
            self.firstplay = False
            return None, True
        else:
            return super().move(x, y, pieces)
