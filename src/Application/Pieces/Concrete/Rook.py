from src.Application.Pieces.Piece import Piece


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


