import pygame
from . import window

class Image():

    def __init__(self, image_file):
        
        self.image = pygame.image.load(image_file).convert_alpha()

        self.rect = self.image.get_rect()

        self.width = self.rect.width
        self.height = self.rect.height

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        window.Window.get_screen().blit(self.image, self.rect)

    def set_position(self, x, y):
        self.x = x
        self.y = y
