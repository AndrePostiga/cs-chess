from PPlay.sprite import *

class Scene(object):
    def __init__(self, janela, mouse, keyboard):
        self.window = janela
        self.mouse = mouse
        self.keyboard = keyboard

    def start(self):
        return 0

    def change_update(self):
        return 0

    def update(self):
        return 0

    def draw(self):
        return 0