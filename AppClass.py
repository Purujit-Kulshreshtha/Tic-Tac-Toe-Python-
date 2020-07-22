import pygame
import sys
from Settings import *

class App():
	def __init__(self):
		pygame.init()
		self.window = pygame.display.set_mode((WIDTH, HEIGHT))
		self.running = True
		self.state = "playing"

	def run(self):
		while self.running:
			if self.state == "playing":
				self.playing_events()
				self.playing_update()
				self.playing_draw()
		pygame.quit()

	def playing_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False


	def playing_draw(self):
		self.window.fill(BG)

		self.draw_board(self.window)

		pygame.display.update()

	def playing_update(self):
		pass

	def draw_board(self, window):
		for x in range(1, 3):
			pygame.draw.line(window, BLACK, (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1]), (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1] + 450), 3) #vertical line
			pygame.draw.line(window, BLACK, (GRID_TRANS[0], GRID_TRANS[1] + x*(CELL_SIZE)), (GRID_TRANS[0] + 450, GRID_TRANS[1] + x*(CELL_SIZE)), 3) #horizontalline