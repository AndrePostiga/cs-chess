from ..scene import Scene
from Lib.image import Image

import os

PRJ_FLDR=os.path.dirname(os.path.abspath(__file__))
print(PRJ_FLDR)
BUTTON_PLAY_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "assets", "imgs", "buttons", "jogar.png")
BUTTON_CREDITOS_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "assets", "imgs", "buttons", "creditos.png")
BUTTON_SAIR_PATH = \
    os.path.join(PRJ_FLDR, "..", "..", "assets", "imgs", "buttons", "sair.png")


class Menu(Scene):
    def __init__(self, janela, mouse):
        super(Menu, self).__init__(janela, mouse)

        self.button_play = Image(BUTTON_PLAY_PATH)
        self.button_creditos = Image(BUTTON_CREDITOS_PATH)
        self.button_sair = Image(BUTTON_SAIR_PATH)

        self.change = 0
        self.wasPressed = True

    def start(self):
        posx = self.window.width/2 - self.button_play.width/2
        posy = self.window.height/8
        self.button_play.set_position(posx, posy*3)
        self.button_creditos.set_position(posx, posy*4)
        self.button_sair.set_position(posx, posy*5)

    def change_update(self):
        if not(self.wasPressed):
            if (self.mouse.is_over_object(self.button_play) 
                and self.mouse.is_button_pressed(1)):
                return 2
            if (self.mouse.is_over_object(self.button_creditos) 
                and self.mouse.is_button_pressed(1)):
                return 42
            if (self.mouse.is_over_object(self.button_sair) 
                and self.mouse.is_button_pressed(1)):
                return -1
        self.wasPressed = self.mouse.is_button_pressed(1)
        return 0

    def update(self):
        self.change = self.change_update()

    def draw(self):
        self.window.set_background_color((0, 0, 0))
        self.button_play.draw()
        self.button_creditos.draw()
        self.button_sair.draw()