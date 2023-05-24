from abc import ABC, abstractmethod

from src.Application.Lib.window import Window

import pygame


class Piece(ABC):

    def __init__(self, radius, x=0, y=0, type=0, offSetX=0, offSetY=0):
        self.center = None
        self.x = x
        self.y = y
        self.offSetX = offSetX
        self.offSetY = offSetY
        self.type = type
        if type == 0:
            self.color = pygame.Color("gray72")
        else:
            self.color = pygame.Color("gray22")
        self.radius = radius
        self.setCenter()

    # def draw(self):
    #     pygame.draw.circle(Window.get_screen(), self.color, self.center, self.radius)

    @abstractmethod
    def draw(self):
        return NotImplemented

    # def move(self, x, y, pieces):
    #     if self.type == 0:
    #         self.y += 1
    #     else:
    #         self.y -= 1
    #     self.setCenter()

    @staticmethod
    def createmask():
        mask = []
        for i in range(8):
            mask.append([])
            for j in range(8):
                mask[i].append(-1)
        return mask

    def setCenter(self):
        self.center = (self.offSetX + self.radius * (2 * self.x), self.offSetY + self.radius * (2 * self.y))

    # def setCenter(self):
    #     self.center = (
    #         self.offSetX + self.radius * ((2 * self.x) + 1),
    #         self.offSetY + self.radius * ((2 * self.y) + 1)
    #     )

    def move(self, x, y, pieces):

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

    @abstractmethod
    def movepossibilities(self, pieces: list):
        return NotImplemented
