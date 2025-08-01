import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Overall class to manage game assets and behavior"""
	def __init__(self):
		"""Initialise the game and create game resources"""
		pygame.init()
		self.settings = Settings()
		# Set the screen attribute of the game
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		# Set the background color
		self.bg_color = (self.settings.bg_color)
		self.ship = Ship(self)

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			# Watch for keyboard and mouse events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			# Redraw the scree during each pass through the loop
			self.screen.fill(self.settings.bg_color)
			# Draw the ship to the screen
			self.ship.blitme()
			# Make the most recently drawn screen visible
			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()

