from Lib.image import *

class Scene(object):
    def __init__(self, janela, mouse):
        self.window = janela
        self.mouse = mouse

    def start(self):
        return 0

    def change_update(self):
        return 0

    def update(self):
        return 0

    def draw(self):
        return 0