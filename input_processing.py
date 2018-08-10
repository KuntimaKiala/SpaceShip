
import pygame as pg 
import sys
from bullet import Bullet


# Function that handles the ship's navegation system
def navegation(ship, screen, bullets) :
	

	for event in pg.event.get() :
		# TO QUIT
		if event.type == pg.QUIT :
			sys.exit()
		# TO MOVE RIGHT
		if event.type == pg.KEYDOWN :
			if event.key == pg.K_RIGHT: 
				ship.moving_right =True
			if event.key == pg.K_SPACE :
				#Creating a bullet and adding it to the bullet group created at Game file
				if len(bullets) < ship.bullet_allowed :
					new_bullet = Bullet(screen, ship)
					bullets.add(new_bullet)
				

		# TO STOP MOVING RIGHT		
		if event.type == pg.KEYUP :
			if event.key == pg.K_RIGHT: 
				ship.moving_right =False

		# TO MOVE LEFT
		if event.type == pg.KEYDOWN :
			if event.key == pg.K_LEFT: 
				ship.moving_left =True
		# TO STOP MOVING RIGHT		
		if event.type == pg.KEYUP :
			if event.key == pg.K_LEFT: 
				ship.moving_left =False	
		# TO FIRE THE BULLETS



# Function that redraw the screen 
def update_screen(ship, screen, bullets) :

	for bullet in bullets.sprites() :
		bullet.draw_bullet()



def text_object(text, font) :
	red = (255,0,0)
	black =(0,0,0)
	white =(255,255,255)
	color ={"red" :red, "black" : black, "white": white }
	textSurface = font.render(text, True, color["red"])
	return textSurface, textSurface.get_rect()


def message_display(text, screen) :
	width, height = 500, 500 
	largeText = pg.font.Font("freesansbold.ttf", 50)
	TextSurf, TextRect = text_object(text, largeText)
	TextRect.center = ((width/2), (height/2))
	screen.blit(TextSurf, TextRect)
	

