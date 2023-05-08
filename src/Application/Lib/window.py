import sys
import pygame
from pygame.locals import *
from . import mouse

pygame.init()
    
class Window():
    screen = None
    
    def __init__(self, width, height):
        Window.mouse = mouse.Mouse()
        
        self.width = width
        self.height = height
        self.color = [0,0,0]
        self.title = "Title"
        self.curr_time = 0 
        self.last_time = 0
        self.total_time = 0

        Window.screen = pygame.display.set_mode([self.width, self.height])

        self.set_background_color(self.color)
        self.set_title(self.title)


        pygame.display.update()

    def update(self):
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==QUIT:
                self.close()
        self.last_time = self.curr_time 
        self.curr_time = pygame.time.get_ticks()
        self.total_time += (self.curr_time - self.last_time)

    def clear(self):
        self.set_background_color([255,255,255])
        self.update()

    def close(self):
        pygame.quit()
        sys.exit()
        
    def set_background_color(self, RGB):
        self.color = RGB
        Window.screen.fill(self.color)

    def get_background_color(self):
        return self.color

    def set_title(self, title):
        self.title = title
        pygame.display.set_caption(title)

    def get_title(self):
        return self.title
    
    @classmethod
    def get_screen(cls):
        return cls.screen

    @classmethod
    def get_mouse(cls):
        return cls.mouse