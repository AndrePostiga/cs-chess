import pygame
from Lib import window
import time

class Timer():
    time_spent1 = 10*60
    time_spent2 = 10*60

    def __init__(self, window: window.Window):
        self.window = window
        self.time1 = time.time()
        self.flag = 0
        pygame.font.init()
        self.text = pygame.font.SysFont(name="monospace",size=35)
        self.textlb = self.text.render("Timer Jogador 1: %d min %d s" % (self.time_spent1 // 60, self.time_spent1 % 60),
                                       True, (0, 0, 0))

        self.text2 = pygame.font.SysFont(name="monospace",size=35)
        self.textlb2 = self.text2.render("Timer Jogador 2: %d min %d s" % (self.time_spent2 // 60, self.time_spent2 % 60),True, (0, 0, 0))

        self.window.screen.blit(self.textlb, (self.window.width - self.textlb.get_width(), self.window.height - self.textlb.get_height()))
        #self.window.screen.blit(self.textlb2, (0, 0))
        #desenhar dois timers um em cima e outro embaixo
    def timeP1(self):
        self.time2 = time.time()
        self.window.screen.blit(self.textlb, (
        self.window.width - self.textlb.get_width(), self.window.height - self.textlb.get_height()))
        #self.window.screen.blit(self.textlb2, (0, 0))
        time_diff = self.time2 - self.time1
        if time_diff >= 0.001:
            self.textlb = self.text.render("Timer Jogador 1: %d min %d s" % (self.time_spent1 // 60, self.time_spent1 % 60),True, (0, 0, 0))
            self.time_spent1 = self.time_spent1 - time_diff
            self.time1 = self.time2

        return


    def timeP2(self):
        self.time2 = time.time()
        self.window.screen.blit(self.textlb, (
        self.window.width - self.textlb.get_width(), self.window.height - self.textlb.get_height()))
        self.window.screen.blit(self.textlb2, (0, 0))
        time_diff = self.time2 - self.time1
        time.sleep(1.1)
        print(time_diff)
        if time_diff >= 0.001:
            self.textlb2 = self.text2.render("Timer Jogador 2: %d min %d s" % (self.time_spent2 // 60, self.time_spent2 % 60),True, (0, 0, 0))
            self.time_spent2 = self.time_spent2 - time_diff
            self.time1 = self.time2



        return

