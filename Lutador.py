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

	images = {}
	
	images['right'] = Image(Point(x, y), "images/editado.png")
	images['idle'] = Image(Point(x, y), "images/editado.png")
	images['up'] = Image(Point(x,y), "images/balrog pulando.png")
	images['down'] = Image(Point(x, y), "images/balrog agachado.png")
	image = images['right']

	def __init__(self, hp, mp, x, y):
		self.hp = hp
		self.mp = mp
		self.x = x
		self.y = y
		
	def getX(self):
		return self.x

	def getY(self):
		return self.y
    
	def getImage(self):
		return self.images['right']
		
	def setX(self, x):
		self.x = x
    
	def setY(self, y):
		self.y = y    
        
	def walk_right(self):
		self.vx = 10
		self.image = self.images['right']
     
	def walk_left(self):
		self.vx = -10
        
	def move(self):
		self.x = self.x + self.vx
		self.y = self.y + self.vy
    
	def jump(self, curr_time):
		self.vx = 10
		self.image = self.images['up']
		print curr_time;
