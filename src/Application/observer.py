from Lib.window import *
from Scenes.menu import *

window = Window(1080, 600)
window.set_background_color((0, 0, 0))
window.set_title("Xadrez")
mouse = window.get_mouse()

dif = 0
actual_scene = 0

def change_scene(scene):
    global actual_scene,dif
    if scene == 1:
        actual_scene = Menu(window, mouse)
        actual_scene.start()
    else:
        quit()

def draw():
    actual_scene.draw()

def update():
    global dif
    window.update()
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