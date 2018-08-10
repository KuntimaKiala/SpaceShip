import pygame as pg 
 

class Ship() :

	def __init__(self, screen) :
		"Initializing the ship and set the start location on the screen" 
		self.screen = screen

		# Loading the ship and get its rectangle of the surface (ship image and screen size)
		self.image = pg.image.load('images/ship.png')
		# Rotate the image 
		self.image  = pg.transform.rotate(self.image, 180)
		#resize Image 
		self.image  = pg.transform.scale(self.image, (50,50))

		self.rect = self.image.get_rect() 
		self.screen_rect = screen.get_rect()

		#Start each new ship at the bottom center of the screen
		self.rect.centerx = float(self.screen_rect.centerx) 
		self.rect.bottom = self.screen_rect.bottom

		#Moving flag
		self.moving_right = False
		self.moving_left  = False

		#Bullet settings
		self.bullet_speed_factor = 1 
		self.bullet_width = 1
		self.bullet_height = 10
		self.bullet_color = 100,0,0
		self.speed_factor = 1
		self.bullet_allowed = 25

	def Update(self) :
		"""Updating the Location of the of the ship based on the flag"""
		if self.moving_right  and self.rect.right < self.screen_rect.right :
			self.rect.centerx += 2.5

		if self.moving_left  and self.rect.left > self.screen_rect.left :
			self.rect.centerx -= 1.5

		self.rect.centerx = self.rect.centerx
		# Control the Range of the Ship 

		




	def blitme(self) :
		""" Draw the ship on the screen on the location choosen in __init__ function """
		self.screen.blit(self.image, self.rect)