from abc import ABC, abstractmethod

from src.Application.Lib.window import Window

import pygame


class Piece(ABC):

    def __init__(self, radius, x:int, y:int, type=0, offSetX=0, offSetY=0):
        self.center = None
        self.x = x
        self.y = y
        self.image = None
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

    def draw(self):
        self.image.draw()

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
            return None
        elif check[x][y] == 2:
            removingpiece = None
            for piece in pieces:
                if piece.x == x and piece.y == y:
                    removingpiece = piece

            self.x = x
            self.y = y

            #
            self.setCenter()
            self.image.set_position(self.center[0], self.center[1])
            return removingpiece
            #

    @abstractmethod
    def movepossibilities(self, pieces: list["Piece"]) -> list[list[int]]:
        return NotImplemented
