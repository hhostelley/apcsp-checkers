import sys, pygame
import os
from pygame.locals import *

bg = pygame.image.load('assets/bg.png')
title1 = pygame.image.load('assets/title1.png')
red_piece = pygame.image.load('assets/red_piece.png')
black_piece = pygame.image.load('assets/black_piece.png')
board = pygame.image.load('assets/board.png')
black    = (  0,   0,   0)
WHITE    = (255, 255, 255)
BLUE     = (  0,   0, 255)
RED      = (255,   0,   0)
GOLD     = (255, 215,   0)
HIGH     = (160, 190, 255)

class Main:

    def __init__(self, width=1280,height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def Game(self):
        self.screen.fill(black)
        self.screen.blit(bg,(0,0))
        self.screen.blit(black_piece,(0,0))
        self.screen.blit(red_piece,(100,0))
        self.screen.blit(board,(235,0))

    def MainLoop(self):
        button = False
        while 1:
            pygame.event.pump()
            self.screen.fill((0, 0, 0))
            self.screen.blit(bg,(0,0))
            self.screen.blit(title1,(0,0))
            start = pygame.image.load('assets/start.png').convert_alpha()
            b = self.screen.blit(start,(350,400))
            if button == True:
                MainWindow.Game()
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
