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
		self.images['idle'] = "images/" + name + "/idle.png"
		self.images['right'] = "images/" + name + "/idle.png"
		self.images['left'] = "images/" + name + "/idle.png"
		self.images['up'] = "images/" + name + "/idle.png"
		self.images['down'] = "images/" + name + "/idle.png"
		self.images['punch1'] = "images/" + name + "/punch1.png"
		self.images['punch2'] = "images/" + name + "/punch2.png"
		self.images['punch3'] = "images/" + name + "/punch3.png"

		self.image = self.images['idle']

		self.start_time = 0
		self.jump_time = 0

		self.jumping = False
		self.punching = False
		self.moving = False
		
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
		self.image = self.images['idle']

	def walk_right(self):
		if(not self.isPunching()):
			self.dx = 10
			self.image = self.images['right']     		
			#self.moving = True

	def walk_left(self):
		if(not self.isPunching()):
			self.dx = -10
			self.image = self.images['left']
	        #self.moving = True

	def move(self):
		self.x = self.x + self.dx
		self.y = self.y + self.dy
		self.dx = 0
		self.moving = False

	def jump(self, start_time):
		pass
		#self.dy = (self.vy * t) + (self.g*(t*t))/2
		

	def punch(self):
		if(not self.isMoving()):
			self.punching = True

	def animate(self, image):
		if(self.punching):
			if(image == self.images['idle']):
				self.image = self.images['punch1']

			if(image == self.images['punch1']):
				print self.image
			
				self.image = self.images['punch2']
				

			if(image == self.images['punch2']):
				print self.image
				
				self.image = self.images['punch3']
				

			if(image == self.images['punch3']):
				print self.image
				
				self.image = self.images['idle']
				self.punching = False