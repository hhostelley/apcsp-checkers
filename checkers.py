import sys, pygame
from pygame.locals import *
import os

## PYGAME and Load_Image function are imported code that we do not take credit for
def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class CheckersMain:
    def __init__(self, width=640,height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        self.LoadSprites();
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.StartButton_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):
        self.StartButton = StartButton()
        self.StartButton_sprites = pygame.sprite.RenderPlain((self.StartButton))

class StartButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('start.png',-1)

if __name__ == "__main__":
    MainWindow = CheckersMain()
    MainWindow.MainLoop()
