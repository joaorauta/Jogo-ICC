import time
import Tkinter
from graphics import *

class Lutador():

	def __init__(self, hp, mp, x, y, name):
		self.hp = hp
		self.mp = mp
		
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.vy = 3
		self.g = -9.8

		self.images = {}
		self.images['idle'] = "images/" + name + "/idle1.png"
		self.images['right'] = "images/" + name + "/idle1.png"
		self.images['left'] = "images/" + name + "/idle1.png"
		self.images['up'] = "images/" + name + "/idle1.png"
		self.images['down'] = "images/" + name + "/idle1.png"

		self.images['punch1'] = "images/" + name + "/punch1.png"
		self.images['punch2'] = "images/" + name + "/punch2.png"
		self.images['punch3'] = "images/" + name + "/punch3.png"

		self.images['idle1'] = "images/" + name + "/idle1.png"
		self.images['idle2'] = "images/" + name + "/idle2.png"
		self.images['idle3'] = "images/" + name + "/idle3.png"
		self.images['idle4'] = "images/" + name + "/idle4.png"

		self.images['walk1'] = "images/" + name + "/walk1.png"
		self.images['walk2'] = "images/" + name + "/walk2.png"
		self.images['walk3'] = "images/" + name + "/walk3.png"
		self.images['walk4'] = "images/" + name + "/walk4.png"
		self.images['walk5'] = "images/" + name + "/walk5.png"

		self.image = self.images['idle1']

		self.start_time = 0
		self.jump_time = 0

		self.jumping = False
		self.punching = False
		self.moving = False
		self.walking = False
		
		hitbox_p1X = (self.getX() - 40)
		hitbox_p1Y = (self.getY() + 100)

		hitbox_p2X = (self.getX() + 40)
		hitbox_p2Y = (self.getY() - 100)

		self.hitbox = Rectangle(Point(hitbox_p1X, hitbox_p1Y), Point(hitbox_p2X, hitbox_p2Y))


	def getX(self):
		return self.x

	def getY(self):
		return self.y
    
	def getImage(self):
		return self.image
	
	def isJumping(self):
		return self.jumping

	def isMoving(self):
		return self.moving

	def isPunching(self):
		return self.punching

	def setX(self, x):
		self.x = x
    
	def setY(self, y):
		self.y = y    
        
	def idle(self):
		self.image = self.images['idle1']

	def walk_right(self):
		if(not self.isPunching()):
			self.dx = 10
			if("walk" not in self.image):
				self.image = self.images['walk1']
			self.walking = True

	def walk_left(self):
		if(not self.isPunching()):
			self.dx = -10
			if("walk" not in self.image):
				self.image = self.images['walk1']
			self.walking = True

	def move(self):
		distX = self.x + self.dx
		distY = self.y + self.dy
		if(distX >= 0  and distX <= 750):
			self.x = distX
		self.y = self.y + self.dy
		self.dx = 0
		self.moving = False

	def jump(self, start_time):
		pass
		#self.dy = (self.vy * t) + (self.g*(t*t))/2
		

	def punch(self):
		self.walking = False
		self.punching = True
		self.image = self.images['punch1']

	def animate(self, image):
		if(self.punching):
			if(image == self.images['punch1']):
				self.image = self.images['punch2']
				
			if(image == self.images['punch2']):
				self.image = self.images['punch3']

			if(image == self.images['punch3']):
				self.image = self.images['idle1']
				self.punching = False

		if(self.walking):
			if(image == self.images['idle1']):
				self.image = self.images['walk1']

			if(image == self.images['walk1']):
				self.image = self.images['walk2']

			if(image == self.images['walk2']):
				self.image = self.images['walk3']

			if(image == self.images['walk3']):
				self.image = self.images['walk4']

			if(image == self.images['walk4']):
				self.image = self.images['walk5']

			if(image == self.images['walk5']):
				self.image = self.images['idle1']
				self.walking = False
		
		else:
			if(image == self.images['idle1']):
				self.image = self.images['idle2']

			if(image == self.images['idle2']):
				self.image = self.images['idle3']

			if(image == self.images['idle3']):
				self.image = self.images['idle4']

			if(image == self.images['idle4']):
				self.image = self.images['idle1']