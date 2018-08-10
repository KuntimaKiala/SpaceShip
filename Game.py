
import numpy as np
import sys
import pygame as pg 
from ShipSpace import Ship 
from input_processing import navegation, update_screen, message_display
from pygame.sprite import Group
class Screen_Display():


	def __init__(self) : 
		# Set the Width and the height of the screen
		self.width = 500
		self.height = 500
		# Set the RGB color of the screen
		self.R = 250
		self.G = 250
		self.B = 250
		self.color =(self.R, self.G, self.B)
		print ("START")
		# The clock of the game ==> the speed
		self.clock = pg.time.Clock() 

	

	def game_loop(self) :
		# Initializes the game and creates a screen object 
		pg.init()
		screen = pg.display.set_mode((self.width,self.height))
		pg.display.set_caption("Alien Invasion")
		# Set the background color

		#Make the Ship 
		ship = Ship(screen)
		#Start the main loop
		#Make a group to store the bullets in
		bullets  = Group()
		while True :

			#Watch for keyboard and mouse events.
			navegation(ship, screen, bullets)

			# Show the Changes 

			ship.Update()
			bullets.update()

			# Get rid of bullets that have disappeared 
			for bullet in bullets.copy() :
				if bullet.rect.bottom <= 0 :
					bullets.remove(bullet)

			#print (len(bullets))		
			#Redraw the screen during each pass of the loop
			screen.fill(self.color)
			update_screen(ship, screen, bullets) 
			ship.blitme()


			# Make the most recently draw screen visible, show the color
			pg.display.flip()
			self.clock.tick(60)

			


