from ..scene import Scene
from Lib.tile import Tile

import pygame
from src.Application.Pieces.Concrete.Pawn import Pawn
from src.Application.Pieces.Concrete.Bishop import Bishop
from src.Application.Pieces.Concrete.Rook import Rook
from src.Application.Pieces.Concrete.Queen import Queen
from src.Application.Pieces.Concrete.King import King
from src.Application.Pieces.Concrete.Knight import Knight


class Game(Scene):
    def __init__(self, window, mouse):
        super(Game, self).__init__(window, mouse)
        self.change = 0
        self.wasPressed = True
        self.board = []
        self.pieces = []
        self.wasPressed = True

        self.choice = None

    def start(self):
        self.turn = 0

        size = 60
        posx = (self.window.width - 8 * size) / 2
        posy = (self.window.height - 8 * size) / 2
        self.appendspecials(size, posx, posy, 0)
        self.appendspecials(size, posx, posy, 1)
        for i in range(8):
            self.board.append([])
            for j in range(8):
                color = pygame.Color('white')
                if (i + j) % 2 != 0:
                    color = pygame.Color('chocolate4')
                self.board[i].append(Tile(size, size, posx +
                                          size * i, posy + size * j, color))
                if j == 1:
                    self.pieces.append(Pawn(size / 2, i, j, 0, posx, posy))

                if j == 6:
                    self.pieces.append(Pawn(size / 2, i, j, 1, posx, posy))

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

                                    enemydefeat, hasmoved = self.choicepiece.move(self.board.index(lane),lane.index(block),self.pieces)
                                    if hasmoved:
                                        #TODO joga a peca fora aqui
                                        #
                                        self.turn = 1
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
                                and self.mouse.is_button_pressed(1)):
                            self.choicepiece = piece
                            self.choice = piece.movepossibilities(self.pieces)
                            self.wasPressed = True
                else:
                    if not self.mouse.is_button_pressed(1):
                        self.wasPressed = False
        else:
            self.turn = 0
            #TODO não meu turno


    def update(self):
        self.statemachine()
        self.maskboard(self.choice)
    def appendspecials(self, size, posx, posy, col):
        if col == 0:
            self.pieces.append(Rook(size / 2, 0, 0, 0, posx, posy))
            self.pieces.append(Knight(size / 2, 1, 0, 0, posx, posy))
            self.pieces.append(Bishop(size / 2, 2, 0, 0, posx, posy))
            self.pieces.append(Queen(size / 2, 3, 0, 0, posx, posy))
            self.pieces.append(King(size / 2, 4, 0, 0, posx, posy))
            self.pieces.append(Bishop(size / 2, 5, 0, 0, posx, posy))
            self.pieces.append(Knight(size / 2, 6, 0, 0, posx, posy))
            self.pieces.append(Rook(size / 2, 7, 0, 0, posx, posy))
        else:
            self.pieces.append(Rook(size / 2, 0, 7, 1, posx, posy))
            self.pieces.append(Knight(size / 2, 1, 7, 1, posx, posy))
            self.pieces.append(Bishop(size / 2, 2, 7, 1, posx, posy))
            self.pieces.append(Queen(size / 2, 3, 7, 1, posx, posy))
            self.pieces.append(King(size / 2, 4, 7, 1, posx, posy))
            self.pieces.append(Bishop(size / 2, 5, 7, 1, posx, posy))
            self.pieces.append(Knight(size / 2, 6, 7, 1, posx, posy))
            self.pieces.append(Rook(size / 2, 7, 7, 1, posx, posy))

    #implementar arroba/encapsular todos os mouses
    def mouseclickverifier(self, function):
        pass
    def maskboard(self, mask):
        #TODO: help here wanted
        # colorir a matriz aqui
        #
