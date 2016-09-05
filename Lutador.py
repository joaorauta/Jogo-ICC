import time
import Tkinter
from graphics import *

class Lutador():
	hp = 100
	mp = 0
	x = 0
	y = 0
	x0 = 0
	y0 = 0
	vx = 0
	vy = 0
	angle = 60
	time = 0
	

	def __init__(self, hp, mp, x, y):
		self.hp = hp
		self.mp = mp
		self.x = x
		self.y = y
		
		self.images = {}

		self.images['right'] = "images/editado.png"
		self.images['idle'] = "images/editado.png"
		self.images['up'] = "images/balrog pulando.png"
		self.images['down'] = "images/balrog agachado.png"
		
		self.image = self.images['right']
		
	def getX(self):
		return self.x

	def getY(self):
		return self.y
    
	def getImage(self):
		return self.image
		
	def setX(self, x):
		self.x = x
    
	def setY(self, y):
		self.y = y    
        
	def idle(self):
		self.image = self.images['up']

	def walk_right(self):
		self.vx = 10
		self.image = self.images['right']
		
     
	def walk_left(self):
		self.vx = -10
		self.image = self.images['down']
        
	def move(self):
		self.x = self.x + self.vx
		self.y = self.y + self.vy
		self.vx = 0
		self.vy = 0

	def jump(self, curr_time):
		self.vx = 10
		self.image = self.images['up']
		print curr_time;
