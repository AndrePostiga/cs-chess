from PPlay.window import *
from scenes.menu import *

janela = Window(1080, 600)
janela.set_background_color((0, 0, 0))
janela.set_title("Xadrez")
mouse = janela.get_mouse()
keyboard = janela.get_keyboard()

dif = 0
actual_scene = 0

def change_scene(scene):
    global actual_scene,dif
    if scene == 1:
        actual_scene = Menu(janela, mouse, keyboard)
        actual_scene.start()
    else:
        quit()

def draw():
    actual_scene.draw()

def update():
    global dif
    janela.update()
    actual_scene.update()
    if actual_scene.change != 0:
        try:
            dif = actual_scene.setDif
        except:
            dif = dif
        change_scene(actual_scene.change)

def loop():
    while (True):
        draw()
        update()

change_scene(1)
loop()