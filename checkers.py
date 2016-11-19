import sys, pygame
import os
from pygame.locals import *

bg = pygame.image.load('assets/bg.png')
title1 = pygame.image.load('assets/title1.png')

class Main:

    def __init__(self, width=1280,height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))



    def hey(self):
        self.screen.blit(title1,(100,100))

    def MainLoop(self):
        button = False
        while 1:
            pygame.event.pump()
            self.screen.fill((0, 0, 0))
            self.screen.blit(bg,(0,0))
            self.screen.blit(title1,(0,0))
            start = pygame.image.load('assets/start.png').convert_alpha()
            b = self.screen.blit(start,(400,400))
            if button == True:
                MainWindow.hey()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if b.collidepoint(pos):
                        button = True
                        pygame.display.update()

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.MainLoop()
