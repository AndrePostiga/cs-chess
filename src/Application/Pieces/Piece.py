
from src.Application.Lib.window import Window

import pygame



class Piece:

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

    def draw(self):
        pygame.draw.circle(Window.get_screen(), self.color, self.center, self.radius)

    def move(self, x, y, pieces):
        if self.type == 0:
            self.y += 1
        else:
            self.y -= 1
        self.setCenter()

    @staticmethod
    def createmask():
        mask = []
        for i in range(8):
            mask.append([])
            for j in range(8):
                mask[i].append(-1)
        return mask

    def setCenter(self):
        self.center = (
            self.offSetX + self.radius*((2*self.x)+1), 
            self.offSetY + self.radius*((2*self.y)+1)
        )

