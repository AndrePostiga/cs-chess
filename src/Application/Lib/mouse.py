import pygame

class Mouse():
    def __init__(self):
        self.BUTTON_LEFT = 1
        self.BUTTON_MIDDLE = 2
        self.BUTTON_RIGHT = 3
        self.WHEEL_UP = 4
        self.WHEEL_DOWN = 5
        
        self.visibility = True


    def get_position(self):
        return pygame.mouse.get_pos()


    def set_position(self, x, y):
        pygame.mouse.set_pos([x,y])


    def hide(self):
        pygame.mouse.set_visible(False)
        self.visibility = False


    def unhide(self):
        pygame.mouse.set_visible(True)
        self.visibility = True

    def is_visible(self):
        return self.visibility


    def is_button_pressed(self, button):
        pressed_buttons = pygame.mouse.get_pressed()
        if(pressed_buttons[button-1] == 1):
            return True
        else:
            return False            
    def is_over_area(self, start_point, end_point):
        mouse_pos = self.get_position()
        
        if((mouse_pos[0] < start_point[0]) or
           (mouse_pos[1] < start_point[1]) or
           (mouse_pos[0] > end_point[0]) or
           (mouse_pos[1] > end_point[1])):
            return False
        else:
            return True
        
    def is_over_object(self, game_object):
        return self.is_over_area([game_object.x, game_object.y],
                            [game_object.x + game_object.width,
                             game_object.y + game_object.height])

    def is_on_screen(self):
        return pygame.mouse.get_focused()


    def is_off_screen(self):
        return (not pygame.mouse.get_focused())
