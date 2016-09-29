import time
import Tkinter
from graphics import *

class Lutador():

	def __init__(self, hp, mp, x, y, name):
		self.name = name

		self.hp = hp
		self.mp = mp
		
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.vy = 3
		self.g = -9.8


		self.images = {}
		self.images['idle']   = "images/" + name + "/idle1.png"
		self.images['right']  = "images/" + name + "/idle1.png"
		self.images['left']   = "images/" + name + "/idle1.png"
		self.images['up'] 	  = "images/" + name + "/idle1.png"
		self.images['crouch']   = "images/" + name + "/crouch.png"
		
		self.images['block'] = "images/" + name + "/block.png"
		self.images['c_block'] = "images/" + name + "/c_block.png"

		self.images['punch1'] = "images/" + name + "/punch1.png"
		self.images['punch2'] = "images/" + name + "/punch2.png"
		self.images['punch3'] = "images/" + name + "/punch3.png"

		self.images['c_punch1'] = "images/" + name + "/c_punch1.png"
		self.images['c_punch2'] = "images/" + name + "/c_punch2.png"
		self.images['c_punch3'] = "images/" + name + "/c_punch3.png"

		self.images['kick1'] = "images/" + name + "/kick1.png"
		self.images['kick2'] = "images/" + name + "/kick2.png"
		self.images['kick3'] = "images/" + name + "/kick3.png"

		self.images['c_kick1'] = "images/" + name + "/c_kick1.png"
		self.images['c_kick2'] = "images/" + name + "/c_kick2.png"
		self.images['c_kick3'] = "images/" + name + "/c_kick3.png"

		self.images['idle1'] = "images/" + name + "/idle1.png"
		self.images['idle2'] = "images/" + name + "/idle2.png"
		self.images['idle3'] = "images/" + name + "/idle3.png"
		self.images['idle4'] = "images/" + name + "/idle4.png"

		self.images['hit1'] = "images/" + name + "/hit1.png"
		self.images['hit2'] = "images/" + name + "/hit2.png"
		self.images['hit3'] = "images/" + name + "/hit3.png"
		self.images['hit4'] = "images/" + name + "/hit4.png"
		self.images['c_hit'] = "images/" + name + "/c_hit.png"

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
		self.kicking = False
		self.moving = False
		self.walking = False
		self.hit = False
		self.blocking = False
		self.crouching = False
		self.dead = False

		hitbox_p1X = (self.getX() - 40)
		hitbox_p1Y = (self.getY() + 100)

		hitbox_p2X = (self.getX() + 40)
		hitbox_p2Y = (self.getY() - 100)

		self.hitbox = Rectangle(Point(hitbox_p1X, hitbox_p1Y), Point(hitbox_p2X, hitbox_p2Y))

	def die(self):
		self.dead = True

	def getX(self):
		return self.x

	def getDx(self):
		return self.dx

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

	def isHit(self):
		return self.hit

	def getHp(self):
		return self.hp

	def isKicking(self):
		return self.kicking

	def isBlocking(self):
		return self.blocking

	def isCrouchinf(self):
		return self.crouching

	def isDead(self):
		return self.dead

	def setDx(self, dx):
		self.dx = dx

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y    
        
	def idle(self):
		self.image = self.images['idle1']

	def block(self):
		self.walking = False
		self.blocking = True
		if(self.crouching):
			self.image = self.images['c_block']
		else:
			self.image = self.images['block']
		
	def getHit(self, damage, blocking):
		name_len = len(self.name)

		#Se for o jogador2, move para a direita
		if(self.name[name_len-1] == "2"):
			if(not blocking):
				self.dx = 10
		else:
			if(not blocking):
				self.dx = -10
		
		if(self.crouching):
			self.image = self.images['c_hit']
		else:
			self.image = self.images['hit1']

		self.walking = False
		self.hit = True

		self.hp -= damage
		if(self.hp <= 0):
			self.die()

	def walk_right(self):

		if(self.crouching):
			self.crouching = False
			self.y -=30
			

		if(not self.isPunching() and not self.isBlocking()):
			self.dx = 10
			if("walk" not in self.image):
				self.image = self.images['walk1']
			self.walking = True

	def walk_left(self):
		if(self.crouching):
			self.crouching = False
			self.y -=30			

		if(not self.isPunching() and not self.isBlocking() and not self.crouching):
			self.dx = -10
			if("walk" not in self.image):
				self.image = self.images['walk1']
			self.walking = True

	def crouch(self):
		if(not self.crouching):
			self.crouching = True
			self.y += 30
		self.image = self.images['crouch']

	def move(self):
		distX = self.x + self.dx
		distY = self.y + self.dy
		if(distX >= 0  and distX <= 750):
			self.x = distX
		self.y = self.y + self.dy
		
		if(not self.isHit()):
			self.dx = 0

		self.moving = False
		

	def jump(self, start_time):
		pass
		#self.dy = (self.vy * t) + (self.g*(t*t))/2
		

	def punch(self):
		if(not self.isBlocking()):
			self.walking = False
			self.punching = True
			if(self.crouching):
				self.image = self.images['c_punch1']
			else:
				self.image = self.images['punch1']

	def kick(self):
		if(not self.isBlocking()):
			self.walking = False
			self.kicking = True
			if(self.crouching):
				self.image = self.images['c_kick1']
			else:
				self.image = self.images['kick1']

	def animate(self, image):
		#print image
		if(self.blocking):
			self.blocking = False			

		if(self.punching):
			if(self.crouching):
				if(image == self.images['c_punch1']):
					self.image = self.images['c_punch2']
					
				if(image == self.images['c_punch2']):
					self.image = self.images['c_punch3']

				if(image == self.images['c_punch3']):
					self.image = self.images['crouch']
					self.punching = False

			else:
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
		
		if(self.kicking):
			if(self.crouching):
				if(image == self.images['c_kick1']):
					self.image = self.images['c_kick2']
					
				if(image == self.images['c_kick2']):
					self.image = self.images['c_kick3']
					#self.x+=60

				if(image == self.images['c_kick3']):
					self.image = self.images['crouch']
					#self.x-=60
					self.kicking = False
			else:
				if(image == self.images['kick1']):
					self.image = self.images['kick2']
					
				if(image == self.images['kick2']):
					self.image = self.images['kick3']

				if(image == self.images['kick3']):
					self.image = self.images['idle1']
					self.kicking = False
		
		if(self.hit):
			if(self.crouching):
				self.image = self.images['crouch']
				self.dx = 0
				self.hit = False
			else:
				if(image == self.images['hit1']):
					self.image = self.images['hit2']

				if(image == self.images['hit2']):
					self.image = self.images['hit3']
					
				if(image == self.images['hit3']):
					self.image = self.images['hit4']
		
				if(image == self.images['hit4']):
					self.image = self.images['idle1']
					self.dx = 0
					self.hit = False

		else:

			if(image == self.images['idle1']):
				self.image = self.images['idle2']

			if(image == self.images['idle2']):
				self.image = self.images['idle3']

			if(image == self.images['idle3']):
				self.image = self.images['idle4']

			if(image == self.images['idle4']):
				self.image = self.images['idle1']