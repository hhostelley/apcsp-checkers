import sys, pygame

class CheckersMain:
    def __init__(self, width=640,height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
if __name__ == "__main__":
    MainWindow = CheckersMain()
    MainWindow.MainLoop()
