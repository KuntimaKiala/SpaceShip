 
import pygame
from pygame.sprite import Sprite 



class Bullet(Sprite) :
	""" A class of the ship's bullets """ 

	def __init__(self, screen, ship) :
		""" Creating a bullet object at the ship's position"""
		super(Bullet, self).__init__()
		self.screen = screen 

		# Creating a bullet at rect (0,0) and then set correct position 
		self.rect = pygame.Rect(0,0, ship.bullet_width, ship.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top


		# Store the bullet's position as decimal value 
		self.y = float(self.rect.y)


		self.color = ship.bullet_color
		self.speed_factor = ship.speed_factor


	def update(self) :
		""" Move the bullet up the screen """ 
		self.y -=self.speed_factor

		#Update the rec position 
		self.rect.y = self.y 

	def draw_bullet(self) :
		"""Drawing the bullets to the screen """
		#drawing circle   (screen, (rgb colour), (Xpos,Ypos),Diameter,border width)
		pygame.draw.circle(self.screen, self.color, (int(self.rect.x), int(self.y)), 6,5 )

