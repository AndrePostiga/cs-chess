from ..scene import Scene
from Lib.tile import Tile
from Lib.timer import Timer

import pygame
from src.Application.Pieces.Concrete.Pawn import Pawn
from src.Application.Pieces.Concrete.Bishop import Bishop
from src.Application.Pieces.Concrete.Rook import Rook
from src.Application.Pieces.Concrete.Queen import Queen
from src.Application.Pieces.Concrete.King import King
from src.Application.Pieces.Concrete.Knight import Knight
from src.Application.Players.AI.AIModel import AIModel


class Game(Scene):

    def __init__(self, window, mouse):

        super(Game, self).__init__(window, mouse)
        self.size = 60

        self.change = 0
        self.wasPressed = True
        self.board = []
        self.pieces = []
        self.wasPressed = True

        self.choice = None

        self.timer = Timer(window)

        self.aiSystem: AIModel

    def start(self):
        self.turn = 0

        posx = (self.window.width - 8 * self.size) / 2
        posy = (self.window.height - 8 * self.size) / 2
        self.appendspecials(posx, posy, 0)
        self.appendspecials(posx, posy, 1)
        for i in range(8):
            self.board.append([])
            for j in range(8):
                color = pygame.Color('white')
                if (i + j) % 2 != 0:
                    color = pygame.Color('chocolate4')
                self.board[i].append(Tile(self.size, self.size, posx +
                                          self.size * i, posy + self.size * j, color))
                if j == 1:
                    self.pieces.append(Pawn(self.size / 2, i, j, 0, posx, posy))

                if j == 6:
                    self.pieces.append(Pawn(self.size / 2, i, j, 1, posx, posy))

        self.aiSystem = AIModel.intanceAI(0, [1, 2, 3, 4, 5, 6])

    def draw(self):

        self.window.set_background_color(pygame.Color('tan'))
        for row in self.board:
            for tile in row:
                tile.draw()
        for piece in self.pieces:
            piece.draw()

    def statemachine(self):
        if not self.turn:
            self.turn = 0

        ##hora dos estados
        if self.turn == 0:
            self.timer.timeP1()
            if (self.choice is not None) and (self.choicepiece is not None):
                # minha vez e e eu escolhi a peça
                if self.mouse.is_button_pressed(3):
                    self.choice = None
                    self.choicepiece = None
                else:
                    if not self.wasPressed:
                        for lane in self.board:
                            for block in lane:
                                if (self.mouse.is_over_object(block)
                                        and self.mouse.is_button_pressed(1)):

                                    enemydefeat, hasmoved = self.choicepiece.move(
                                        self.board.index(lane),
                                        lane.index(block), self.pieces)
                                    if hasmoved:
                                        if enemydefeat is not None:
                                            self.pieces.remove(enemydefeat)
                                        self.turn = 1
                                        self.check_promot(self.choicepiece)
                                        self.choice = None
                                        self.choicepiece = None

                                self.wasPressed = True
                    else:
                        if not self.mouse.is_button_pressed(1):
                            self.wasPressed = False


            else:
                # minha vez, mas n escolhi nada

                if not self.wasPressed:
                    for piece in self.pieces:
                        if (self.mouse.is_over_object(self.board[piece.x][piece.y])
                                and self.mouse.is_button_pressed(1)
                                and piece.type != self.turn):
                            self.choicepiece = piece
                            self.choice = piece.movepossibilities(self.pieces)
                            self.wasPressed = True
                else:
                    if not self.mouse.is_button_pressed(1):
                        self.wasPressed = False
        else:
            # Fixme: trash code
            a = 0
            aiplay = None
            removedpiece = None
            while a < 50:
                aiplay = self.aiSystem.handlePlay(self.pieces)
                print(aiplay)
                if aiplay is None:
                    raise
                removedpiece = aiplay[0].move(aiplay[1], aiplay[2], self.pieces)
                print(removedpiece)
                if removedpiece[1]:
                    break
                a = a + 1

            if removedpiece[0] is not None:
                self.pieces.remove(removedpiece[0])
            self.check_promot(aiplay[0])
            self.turn = 0
            # TODO não meu turno

    def update(self):
        self.statemachine()
        self.maskboard()
    def appendspecials(self, posx, posy, col):
        if col == 0:
            self.pieces.append(Rook(self.size / 2, 0, 0, 0, posx, posy))
            self.pieces.append(Knight(self.size / 2, 1, 0, 0, posx, posy))
            self.pieces.append(Bishop(self.size / 2, 2, 0, 0, posx, posy))
            self.pieces.append(Queen(self.size / 2, 3, 0, 0, posx, posy))
            self.pieces.append(King(self.size / 2, 4, 0, 0, posx, posy))
            self.pieces.append(Bishop(self.size / 2, 5, 0, 0, posx, posy))
            self.pieces.append(Knight(self.size / 2, 6, 0, 0, posx, posy))
            self.pieces.append(Rook(self.size / 2, 7, 0, 0, posx, posy))
        else:
            self.pieces.append(Rook(self.size / 2, 0, 7, 1, posx, posy))
            self.pieces.append(Knight(self.size / 2, 1, 7, 1, posx, posy))
            self.pieces.append(Bishop(self.size / 2, 2, 7, 1, posx, posy))
            self.pieces.append(Queen(self.size / 2, 3, 7, 1, posx, posy))
            self.pieces.append(King(self.size / 2, 4, 7, 1, posx, posy))
            self.pieces.append(Bishop(self.size / 2, 5, 7, 1, posx, posy))
            self.pieces.append(Knight(self.size / 2, 6, 7, 1, posx, posy))
            self.pieces.append(Rook(self.size / 2, 7, 7, 1, posx, posy))

    # implementar arroba/encapsular todos os mouses
    def mouseclickverifier(self, function):
        pass

    def maskboard(self):

        if self.choice is not None:
            # mascara
            i = 0
            while i < len(self.choice):
                j = 0
                while j < len(self.choice[i]):
                    match self.choice[i][j]:
                        case 1:
                            self.board[i][j].set_color('green')
                        case 2:
                            self.board[i][j].set_color('blue')
                        case 3:
                            self.board[i][j].set_color('purple')
                        ################
                        case -1:
                            pass
                            # self.board[i][j].set_color('red')
                        case -2:
                            pass
                            # self.board[i][j].set_color('gray')
                        case 0:
                            self.board[i][j].set_color('yellow')

                    j = j + 1
                i = i + 1



        else:
            for i in range(8):
                self.board.append([])
                for j in range(8):
                    self.board[i][j].set_color('white')
                    if (i + j) % 2 != 0:
                        self.board[i][j].set_color('chocolate4')

    def check_promot(self, elem):
        if isinstance(elem, Pawn):
            posx = (self.window.width - 8 * self.size) / 2
            posy = (self.window.height - 8 * self.size) / 2
            if elem.type == 0 and elem.y == 7:
                self.pieces.append(Queen(elem.radius, elem.x,
                                         elem.y, elem.type, posx, posy))
                self.pieces.remove(elem)
            if elem.type == 1 and elem.y == 0:
                # TODO: abrir caixa de dialogo pokemon estilo red
                #self.pieces.append(Queen(elem.radius, elem.x,
                #                         elem.y, elem.type, posx, posy))

                #Adicionar as opcoes e criar variaveizinhas
                # legaizinhas pra facilitar a remocao depois da escolha
                self.pieces.append(Queen(elem.radius, elem.x, elem.y, 5, posx - elem.radius * 2, posy - elem.radius *2))
                queenR = self.pieces[len(self.pieces)-1]
                self.pieces.append(
                    Rook(elem.radius, elem.x, elem.y, 5, posx, posy - elem.radius * 2))
                rookR = self.pieces[len(self.pieces)-1]
                self.pieces.append(
                    Bishop(elem.radius, elem.x, elem.y, 5, posx + elem.radius * 2, posy - elem.radius * 2))
                bishopR = self.pieces[len(self.pieces)-1]
                self.pieces.append(
                    Knight(elem.radius, elem.x, elem.y, 5, posx + elem.radius * 4, posy - elem.radius * 2))
                bishopR = self.pieces[len(self.pieces) -1]



                #self.pieces.remove(elem)
