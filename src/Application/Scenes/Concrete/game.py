from ..scene import Scene
from Lib.tile import Tile
from src.Application.Pieces.Piece import Piece
import pygame

from src.Application.Pieces.Concrete.Pawn import Pawn


class Game(Scene):
    def __init__(self, window, mouse):
        super(Game, self).__init__(window, mouse)
        self.change = 0
        self.wasPressed = True
        self.board = []
        self.pieces = []
        self.wasPressed = True

    def start(self):
        size = (min(self.window.width, self.window.height) - 200) / 8
        posx = (self.window.width - 8 * size) / 2
        posy = (self.window.height - 8 * size) / 2
        for i in range(8):
            self.board.append([])
            for j in range(8):
                color = pygame.Color('white')
                if (i + j) % 2 != 0:
                    color = pygame.Color('black')
                self.board[i].append(Tile(size, size, posx + size * i, posy + size * j, color))
                if j <= 1:
                    self.pieces.append(Pawn(size / 2, i, j, 0, posx, posy))
                if j >= 6:
                    self.pieces.append(Pawn(size / 2, i, j, 1, posx, posy))

    def draw(self):
        self.window.set_background_color(pygame.Color('tan'))
        for row in self.board:
            for tile in row:
                tile.draw()
        for piece in self.pieces:
            piece.draw()

    def update(self):
        if not self.wasPressed:
            for piece in self.pieces:
                if (self.mouse.is_over_object(self.board[piece.x][piece.y])
                        and self.mouse.is_button_pressed(1)):
                    piece.move(piece.x, (piece.y + 1 if piece.type == 0 else piece.y - 1), self.pieces)
        self.wasPressed = False
