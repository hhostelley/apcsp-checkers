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
    	self.turn = BLUE
        self.selected_piece = None # a board location.
        self.hop = False
        self.selected_legal_moves = []

    def update(self):
        self.graphics.update_display(self.board, self.selected_legal_moves, self.selected_piece)

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

		self.clock = pygame.time.Clock()

		self.window_size = 600
		self.screen = pygame.display.set_mode((self.window_size, self.window_size))
		self.background = pygame.image.load('assets/board.png')

		self.square_size = self.window_size / 8
		self.piece_size = self.square_size / 2

		self.message = False

	def setup_window(self):
		pygame.init()
		pygame.display.set_caption(self.caption)

	def update_display(self, board, legal_moves, selected_piece):
		self.screen.blit(self.background, (0,0))

		self.highlight_squares(legal_moves, selected_piece)
		self.draw_board_pieces(board)

		if self.message:
			self.screen.blit(self.text_surface_obj, self.text_rect_obj)

		pygame.display.update()
		self.clock.tick(60)

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

	def highlight_squares(self, squares, origin):
		for square in squares:
			pygame.draw.rect(self.screen, HIGH, (square[0] * self.square_size, square[1] * self.square_size, self.square_size, self.square_size))

		if origin != None:
			pygame.draw.rect(self.screen, HIGH, (origin[0] * self.square_size, origin[1] * self.square_size, self.square_size, self.square_size))

	def draw_message(self, message):
		self.message = True
		self.font_obj = pygame.font.Font('freesansbold.ttf', 44)
		self.text_surface_obj = self.font_obj.render(message, True, HIGH, BLACK)
		self.text_rect_obj = self.text_surface_obj.get_rect()
		self.text_rect_obj.center = (self.window_size / 2, self.window_size / 2)

class Board:
	def __init__(self):
		self.matrix = self.new_board()

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

	def blind_legal_moves(self, (x,y)):
		if self.matrix[x][y].occupant != None:

			if self.matrix[x][y].occupant.king == False and self.matrix[x][y].occupant.color == BLUE:
				blind_legal_moves = [self.rel(NORTHWEST, (x,y)), self.rel(NORTHEAST, (x,y))]

			elif self.matrix[x][y].occupant.king == False and self.matrix[x][y].occupant.color == RED:
				blind_legal_moves = [self.rel(SOUTHWEST, (x,y)), self.rel(SOUTHEAST, (x,y))]

			else:
				blind_legal_moves = [self.rel(NORTHWEST, (x,y)), self.rel(NORTHEAST, (x,y)), self.rel(SOUTHWEST, (x,y)), self.rel(SOUTHEAST, (x,y))]

		else:
			blind_legal_moves = []

		return blind_legal_moves

	def legal_moves(self, (x,y), hop = False):
		blind_legal_moves = self.blind_legal_moves((x,y))
		legal_moves = []

		if hop == False:
			for move in blind_legal_moves:
				if hop == False:
					if self.on_board(move):
						if self.location(move).occupant == None:
							legal_moves.append(move)

						elif self.location(move).occupant.color != self.location((x,y)).occupant.color and self.on_board((move[0] + (move[0] - x), move[1] + (move[1] - y))) and self.location((move[0] + (move[0] - x), move[1] + (move[1] - y))).occupant == None: # is this location filled by an enemy piece?
							legal_moves.append((move[0] + (move[0] - x), move[1] + (move[1] - y)))

		else: # hop == True
			for move in blind_legal_moves:
				if self.on_board(move) and self.location(move).occupant != None:
					if self.location(move).occupant.color != self.location((x,y)).occupant.color and self.on_board((move[0] + (move[0] - x), move[1] + (move[1] - y))) and self.location((move[0] + (move[0] - x), move[1] + (move[1] - y))).occupant == None: # is this location filled by an enemy piece?
						legal_moves.append((move[0] + (move[0] - x), move[1] + (move[1] - y)))

		return legal_moves

	def remove_piece(self, (x,y)):
		self.matrix[x][y].occupant = None

	def move_piece(self, (start_x, start_y), (end_x, end_y)):
		self.matrix[end_x][end_y].occupant = self.matrix[start_x][start_y].occupant
		self.remove_piece((start_x, start_y))

		self.king((end_x, end_y))

	def is_end_square(self, coords):
		if coords[1] == 0 or coords[1] == 7:
			return True
		else:
			return False

	def on_board(self, (x,y)):
		if x < 0 or y < 0 or x > 7 or y > 7:
			return False
		else:
			return True


	def king(self, (x,y)):
		if self.location((x,y)).occupant != None:
			if (self.location((x,y)).occupant.color == BLUE and y == 0) or (self.location((x,y)).occupant.color == RED and y == 7):
				self.location((x,y)).occupant.king = True

class Square:
	def __init__(self, color, occupant = None):
		self.color = color # color is either BLACK or WHITE
		self.occupant = occupant # occupant is a Square objec

class Piece:
	def __init__(self, color, king = False):
		self.color = color
		self.king = king

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.MainLoop()
