import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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
		# Create a group of bullets
		self.bullets = pygame.sprite.Group()

	def _check_keydown_events(self, event):
		""" Respond to keypresses """
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# Move the ship to the left
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		""" Respond to key releases """
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _check_events(self):
		""" Respond to keypresses and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)	
			elif event.type == pygame.KEYUP:
				# Stop movement when direction is released
				self._check_keyup_events(event)
	
	def _update_screen(self):
		"""Updates images on the screen and flip to the new screen"""
		self.screen.fill(self.settings.bg_color)
		# Draw the ship to the screen
		self.ship.blitme()
		# Draw each bullet in the group of bullets crated from sprite group class
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# Make the most recently drawn screen visible
		pygame.display.flip()

	def _update_bullets(self):
		""" Update position of bullets and get rid of old bullets """
		# Update bullet positions
		self.bullets.update()
		#Get rid of bullets that have dissapeared.
		for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			#Get rid of bullets that have dissapeared
			self._update_bullets()	
			self._update_screen()

	def _fire_bullet(self):
		""" Create a new bullet and add it ti the bullets group """
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

			

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()

