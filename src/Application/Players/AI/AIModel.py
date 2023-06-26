from Pieces.Piece import Piece
import random


class AIModel:
    ai_instance = None

    @staticmethod
    def intanceAI(color, valuematrix):
        if AIModel.ai_instance is None:
            AIModel.ai_instance = AIModel(color, valuematrix)
        return AIModel.ai_instance

    def __init__(self, color, valuematrix):
        self.piececount = None
        self.color = color

        self.valueMatrix = valuematrix
        # [pwn, bsp, rok, hrs, que, kng]

    def handlePlay(self, pieces) -> (Piece, int, int):

        mypieces = []
        for i in pieces:
            if i.type == self.color:
                mypieces.append(i)
        self.piececount = len(mypieces)

        play = None #= bestPlay(pieces)
        if play is not None:
            return play
        play = self.randomPlay(mypieces)
        return play




    #FIXME Trashy fallback, retorna jogada errada as vezes, loopa infinito
    def randomPlay (self, pieces: list[Piece]) -> (Piece, int, int):
        a = True
        selectedpiece = None
        possibleplays = None

        # escolhe peça VALIDA
        while a:
            if self.piececount < 0:
                return None
            selectedpiece = pieces[random.randint(0, self.piececount - 1)]
            possibleplays = selectedpiece.movepossibilities(pieces)
            for lane in possibleplays:
                if True in (ele > 0 for ele in lane):
                    a = False

        # escolhe movimento VALIDO
        while True:
            x, y = random.randint(0, 7), random.randint(0, 7)
            if possibleplays[x][y] == 1 or possibleplays[x][y] == 2 \
                    or possibleplays[x][y] == 3 or possibleplays[x][y] == 4:
                return selectedpiece, x, y


    def bestPlay(self, pieces, table) ->  (Piece, int, int):


        pass
