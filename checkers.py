import sys, pygame
import os
from pygame.locals import *

bg = pygame.image.load('assets/bg.png')
title1 = pygame.image.load('assets/title1.png')
red_piece = pygame.image.load('assets/red_piece.png')
black_piece = pygame.image.load('assets/black_piece.png')
board = pygame.image.load('assets/board.png')
black    = (  0,   0,   0)
BLACK    = (  0,   0,   0)
WHITE    = (255, 255, 255)
BLUE     = (  0,   0, 255)
RED      = (255,   0,   0)
GOLD     = (255, 215,   0)
HIGH     = (160, 190, 255)

##DIRECTIONS##
NORTHWEST = "northwest"
NORTHEAST = "northeast"
SOUTHWEST = "southwest"
SOUTHEAST = "southeast"

class Main:

    def __init__(self, width=1280,height=720):
        pygame.init()
        pygame.display.set_caption("Super Radical Checkers")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        button = False
        intro = True
        while intro:
            pygame.event.pump()
            self.screen.fill((0, 0, 0))
            self.screen.blit(bg,(0,0))
            self.screen.blit(title1,(0,0))
            start = pygame.image.load('assets/start.png').convert_alpha()
            b = self.screen.blit(start,(350,400))
            if button == True:
                GameScene = Game()
                GameScene.Loop2()
                intro = False
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if b.collidepoint(pos):
                        button = True
                        pygame.display.update()


class Game:

    def __init__(self):
        self.graphics = Graphics()
        self.board = Board()

    def update(self):
        self.graphics.update_display(self.board)

    def setup(self):
        self.graphics.setup_window()

    def Loop2(self):
        self.setup()
        while 1:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

class Graphics:
	def __init__(self):
		self.caption = "Checkers"

		self.window_size = 600
		self.screen = pygame.display.set_mode((self.window_size, self.window_size))
		self.background = pygame.image.load('assets/board.png')

		self.square_size = self.window_size / 8
		self.piece_size = self.square_size / 2

		self.message = False

	def setup_window(self):
		pygame.init()
		pygame.display.set_caption(self.caption)

	def update_display(self, board):
		self.screen.blit(self.background, (0,0))
		self.draw_board_pieces(board)

		if self.message:
			self.screen.blit(self.text_surface_obj, self.text_rect_obj)

		pygame.display.update()

#third party code
	def draw_board_squares(self, board):
		for x in xrange(8):
			for y in xrange(8):
				pygame.draw.rect(self.screen, board[x][y].color, (x * self.square_size, y * self.square_size, self.square_size, self.square_size), )

	def draw_board_pieces(self, board):
		for x in xrange(8):
			for y in xrange(8):
				if board.matrix[x][y].occupant != None:
					pygame.draw.circle(self.screen, board.matrix[x][y].occupant.color, self.pixel_coords((x,y)), self.piece_size)

					if board.location((x,y)).occupant.king == True:
						pygame.draw.circle(self.screen, GOLD, self.pixel_coords((x,y)), int (self.piece_size / 1.7), self.piece_size / 4)


	def pixel_coords(self, board_coords):
		return (board_coords[0] * self.square_size + self.piece_size, board_coords[1] * self.square_size + self.piece_size)

	def board_coords(self, (pixel_x, pixel_y)):
		return (pixel_x / self.square_size, pixel_y / self.square_size)

	def draw_message(self, message):
		self.message = True
		self.font_obj = pygame.font.Font('freesansbold.ttf', 44)
		self.text_surface_obj = self.font_obj.render(message, True, HIGH, BLACK)
		self.text_rect_obj = self.text_surface_obj.get_rect()
		self.text_rect_obj.center = (self.window_size / 2, self.window_size / 2)
#end third party code


class Board:
	def __init__(self):
		self.matrix = self.new_board()

# thrid party code
	def new_board(self):
		matrix = [[None] * 8 for i in xrange(8)]
		# The following code block has been adapted from
		# http://itgirl.dreamhosters.com/itgirlgames/games/Program%20Leaders/ClareR/Checkers/checkers.py
		for x in xrange(8):
			for y in xrange(8):
				if (x % 2 != 0) and (y % 2 == 0):
					matrix[y][x] = Square(WHITE)
				elif (x % 2 != 0) and (y % 2 != 0):
					matrix[y][x] = Square(BLACK)
				elif (x % 2 == 0) and (y % 2 != 0):
					matrix[y][x] = Square(WHITE)
				elif (x % 2 == 0) and (y % 2 == 0):
					matrix[y][x] = Square(BLACK)
		for x in xrange(8):
			for y in xrange(3):
				if matrix[x][y].color == BLACK:
					matrix[x][y].occupant = Piece(RED)
			for y in xrange(5, 8):
				if matrix[x][y].color == BLACK:
					matrix[x][y].occupant = Piece(BLUE)

		return matrix

	def board_string(self, board):

		board_string = [[None] * 8] * 8

		for x in xrange(8):
			for y in xrange(8):
				if board[x][y].color == WHITE:
					board_string[x][y] = "WHITE"
				else:
					board_string[x][y] = "BLACK"


		return board_string

	def rel(self, dir, (x,y)):
		if dir == NORTHWEST:
			return (x - 1, y - 1)
		elif dir == NORTHEAST:
			return (x + 1, y - 1)
		elif dir == SOUTHWEST:
			return (x - 1, y + 1)
		elif dir == SOUTHEAST:
			return (x + 1, y + 1)
		else:
			return 0

	def adjacent(self, (x,y)):
		return [self.rel(NORTHWEST, (x,y)), self.rel(NORTHEAST, (x,y)),self.rel(SOUTHWEST, (x,y)),self.rel(SOUTHEAST, (x,y))]

	def location(self, (x,y)):
		return self.matrix[x][y]

#end third party code

class Square:
	def __init__(self, color, occupant = None):
		self.color = color # color is either BLACK or WHITE
		self.occupant = occupant # occupant is a Square object

class Piece:
	def __init__(self, color, king = False):
		self.color = color
		self.king = king

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.MainLoop()
