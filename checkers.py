import sys, pygame
from pygame.locals import *
import os

## PYGAME imported

class CheckersMain:
    def __init__(self, width=1280,height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.start_image = pygame.image.load("assets/start.png")
        self.title1_image = pygame.image.load("assets/title1.png")

    def MainLoop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.blit(self.start_image, (355, 450))
            self.screen.blit(self.title1_image, (240, 10))
            pygame.display.flip()


if __name__ == "__main__":
    MainWindow = CheckersMain()
    MainWindow.MainLoop()
