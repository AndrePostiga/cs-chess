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
        #TODO: castling interagindo mal com xeque
        #TODO: xeque inválido para o rei fixed?

        if piecemove is not None: #querem mover
            proxylist = pieces.copy()
            proxypiece = type(piecemove).__new__(type(piecemove))
            proxypiece.__init__(0, piecemove.x, piecemove.y, piecemove.type, 0, 0)
            proxylist.remove(piecemove)
            proxylist.append(proxypiece)
            proxypiece.move(xmove, ymove, proxylist)
            if piecemove == self:#rei move
                for piece in proxylist:
                    possib = piece.movepossibilities(proxylist)
                    if possib[proxypiece.x][proxypiece.y] == 4:
                        return 1
            else:
                #trocar peça real com a proxy
                for piece in proxylist:
                    possib = piece.movepossibilities(proxylist)
                    if possib[self.x][self.y] == 4:
                        return 1
        else: #estado atual
            proxylist = pieces
            for piece in proxylist:
                possib = piece.movepossibilities(proxylist)
                if possib[self.x][self.y] == 4:
                    if self.ismate(pieces):
                        return 2
                    return 1

        #se for rei = 4, não a 2
        return 0

    def ismate (self, pieces : list[Piece]) -> bool:
        return False





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
                if type(piece).__name__ == "King":
                    mask[piece.x][piece.y] = 4
                else:
                    mask[piece.x][piece.y] = 2
            else:
                mask[piece.x][piece.y] = -2
        if self.firstplay:
            self.check_castling(mask, pieces)

        mask[self.x][self.y] = 0
        return mask

    def check_castling(self, mask, pieces):

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
            #TODO: castling interagindo mal com xeque
            #checar antes de mover qualquer coisa, importante


            #


            if x > self.x:
                tower = check_tower(7, self.y,pieces, self.type)
                #
                # self.castle_check_check(tower, pieces)
                #
                tower.x = self.x+1
                tower.setCenter()
                tower.image.set_position(tower.center[0], tower.center[1])
            else:
                tower = check_tower(0, self.y,pieces, self.type)
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


    # def castle_check_check(self):
    #     proxylist = pieces.copy()
    #     proxypiece = type(Towee).__new__(type(piecemove))
    #     proxypiece.__init__(0, piecemove.x, piecemove.y, piecemove.type, 0, 0)
    #     proxylist.remove(piecemove)
    #     proxylist.append(proxypiece)
    #     proxypiece.move(xmove, ymove, proxylist)
