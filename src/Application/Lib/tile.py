import pygame
from . import window

class Tile():

    def __init__(self, width, height, x=0, y=0, color = pygame.Color('white')):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(window.Window.get_screen(), self.color, self.rect)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
