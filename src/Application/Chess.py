from Lib.window import Window
from Scenes.menu import Menu
class Chess:
    def __init__(self):
        self.window = Window(1080, 600)
        self.window.set_background_color((0, 0, 0))
        self.window.set_title("Xadrez")
        self.mouse = self.window.get_mouse()

    def change_scene(self,scene):
        if scene == 1:
            self.actual_scene = Menu(self.window, self.mouse)
            self.actual_scene.start()
        else:
            quit()

    def draw(self):
        self.actual_scene.draw()

    def update(self):
        self.window.update()
        self.actual_scene.update()
        if self.actual_scene.change != 0:
            self.change_scene(self.actual_scene.change)

    def loop(self):
        while (True):
            self.draw()
            self.update()

chess = Chess()
chess.change_scene(1)
chess.loop()